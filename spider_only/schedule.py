# coding: utf8
import os
import io
import time
import re
import json
from collections import OrderedDict
import pickle
from pprint import pprint

from flask import Blueprint, render_template, request, url_for, send_from_directory, redirect
from flask import current_app as app

from .vars import SCHEDULE_PATH, DEFAULT_LATEST_VERSION, UA_DICT
from .utils import make_request, json_dumps, slot


bp = Blueprint('schedule', __name__, url_prefix='/')


def prepare_data():
    data = OrderedDict()
    for k, d in [('project', 'projectname'), ('_version', DEFAULT_LATEST_VERSION),
                 ('spider', 'spidername')]:
        data[k] = request.form.get(k, d)
    if data['_version'] == DEFAULT_LATEST_VERSION:
        data.pop('_version')

    data['jobid'] = re.sub(r'[^0-9A-Za-z_-]', '', request.form.get('jobid', '')) or time.strftime('%Y-%m-%d_%H%M%S')

    data['setting'] = []
    ua = UA_DICT.get(request.form.get('USER_AGENT', ''), '')
    if ua:
        data['setting'].append('USER_AGENT="%s"' % ua)

    for key in ['ROBOTSTXT_OBEY', 'CONCURRENT_REQUESTS', 'DOWNLOAD_DELAY']:
        value = request.form.get(key, '')
        if value:
            data['setting'].append("%s=%s" % (key, value))

    additional = request.form.get('additional', '').strip()
    if additional:
        parts = [i.strip() for i in re.split('-d\s+', re.sub(r'\r|\n', ' ', additional)) if i.strip()]
        for part in parts:
            part = re.sub(r'\s*=\s*', '=', part)
            if '=' not in part:
                continue
            m_setting = re.match(r'setting=([A-Z_]{6,31}=.+)', part)  # 'EDITOR' 'DOWNLOADER_CLIENTCONTEXTFACTORY'
            if m_setting:
                data['setting'].append(m_setting.group(1))
                continue
            m_arg = re.match(r'([a-zA-Z_][0-9a-zA-Z_]*)=(.+)', part)
            if m_arg and m_arg.group(1) != 'setting':
                data[m_arg.group(1)] = m_arg.group(2)

    filename = '%s_%s_%s' % (data['project'], data.get('_version', 'default-the-latest-version'), data['spider'])
    filename = '%s.pickle' % re.sub(r'[^0-9A-Za-z_-]', '', filename)
    filepath = os.path.join(SCHEDULE_PATH, filename)
    with io.open(filepath, 'wb') as f:
        f.write(pickle.dumps(data))

    slot.add_data(filename, data)

    return filename, data

def prepare_datasimple(project, spider, job, opt):
    data = OrderedDict()
    data['project'] = project
    data['spider'] = spider
    data['opt'] = opt
    
    data['jobid'] = time.strftime('%Y-%m-%d_%H%M%S')
    if opt == "stop":
        data['jobid'] = job

    data['setting'] = []
    

@bp.route('/<int:node>/<opt>/schedule/<project>/<spider>/<job>/', methods=('POST', 'GET'))
@bp.route('/<int:node>/<opt>/schedule/<project>/<spider>/', methods=('POST', 'GET'))
def schedule(node, project, spider, opt, job=None):

    SCRAPYD_SERVER =app.config.get('SCRAPYD_SERVER','127.0.0.1:6800')
    SCRAPYD_SERVERS_AUTH = app.config.get('SCRAPYD_SERVERS_AUTH', None)

    if project and spider and opt:
        if opt is 'start':
            url = 'http://%s/schedule.json' % SCRAPYD_SERVER
        elif opt is 'stop':
            url = 'http://%s/cancel.json' % SCRAPYD_SERVER
            if not job:
                return redirect(url_for('spiders.spiders',node=node))
        else:
            return redirect(url_for('spiders.spiders',node=node))

        prepare_datasimple(project, spider, job, opt)

        pprint(request.form)
        filename = request.form['filename']
        data = slot.data.get(filename)
        
        if not data:
            filepath = os.path.join(SCHEDULE_PATH, filename)
            with io.open(filepath, 'rb') as f:
                data = pickle.loads(f.read())

        status_code, js = make_request(url, data, auth=SCRAPYD_SERVERS_AUTH)

        if js['status'] == 'ok':
            return redirect(url_for('spiders.spiders',node=node))
        else:
            message = js.get('message', '')
            if message:
                js.update({'message': 'See below'})
            js['info'] = "Maybe the project egg file had been deleted, check in the 'Projects > Manage' page."

            alert = "Fail to schedule, got status: " + js['status']
        

    return redirect(url_for('spiders.spiders',node=node))


@bp.route('/<int:node>/schedule/run/')
def run(node):
    pass
