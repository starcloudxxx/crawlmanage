# coding: utf8
import time
import json

from flask import Blueprint
from flask import current_app as app

from .vars import DEFAULT_LATEST_VERSION
from .utils import make_request, json_dumps

bp = Blueprint('api', __name__, url_prefix='/')
API_MAP = dict(start='schedule', stop='cancel', forcestop='cancel')
INFO = """Maybe it's caused by failing to compare versions, \
see INFO in the "Projects > Upload" page, \
and solve the problem in the "Projects > Manage" page."""


@bp.route('/api/<opt>/<project>/<version_spider_job>/', methods=('POST', 'GET'))
@bp.route('/api/<opt>/<project>/', methods=('POST', 'GET'))
@bp.route('/api/<opt>/', methods=('POST', 'GET'))
def api(opt, project=None, version_spider_job=None):
    SCRAPYD_SERVER = app.config.get('SCRAPYD_SERVER', '127.0.0.1:6800')
    SCRAPYD_SERVERS_AUTH = app.config.get('SCRAPYD_SERVERS_AUTH', None)

    url = 'http://{}/{}.json'.format(SCRAPYD_SERVER, API_MAP.get(opt, opt))
    if opt in ['listversions', 'listjobs']:
        url += '?project=%s' % project
    elif opt == 'listspiders':
        if version_spider_job == DEFAULT_LATEST_VERSION:
            url += '?project=%s' % project
        else:
            # Should be _version
            url += '?project=%s&_version=%s' % (project, version_spider_job)

    data = {'project': project}
    if opt == 'start':
        data['spider'] = version_spider_job
        data['jobid'] = time.strftime('%Y-%m-%d_%H%M%S')
    elif opt in ['stop', 'forcestop']:
        data['job'] = version_spider_job
    elif opt == 'delversion':
        data['version'] = version_spider_job
    elif opt == 'delproject':
        pass
    else:
        data = None

    timeout = 5 if opt == 'daemonstatus' else 60
    log = False if opt == 'daemonstatus' else True

    times = 2 if opt == 'forcestop' else 1
    for t in range(times):
        status_code, js = make_request(url, data, timeout=timeout, log=log, auth=SCRAPYD_SERVERS_AUTH)
        if times != 1:
            js['times'] = times
            time.sleep(2)

    if opt == 'listversions' and js['status'] != 'ok':
        js['info'] = INFO

    return json_dumps(js)
