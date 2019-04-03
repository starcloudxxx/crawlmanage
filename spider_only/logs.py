# coding: utf8
import re

from flask import Blueprint, render_template, url_for, request
from flask import current_app as app

from .vars import DEFAULT_LATEST_VERSION, pattern_directory, keys_directory,NAVI_NAME
from .utils import make_request

bp = Blueprint('logs', __name__, url_prefix='/')

@bp.app_template_filter()
def regex_replace(s, find, replace):
    return re.sub(find, replace, s)



@bp.route('/logs/<project>/<spider>/')
def logs(project=None, spider=None):
    
    title = spider+"_LOGS"
    navis = NAVI_NAME

    SCRAPYD_SERVER =app.config.get('SCRAPYD_SERVER','127.0.0.1:6800')
    SCRAPYD_SERVERS_AUTH = app.config.get('SCRAPYD_SERVERS_AUTH', None)

    url = 'http://{}/logs/{}{}'.format(SCRAPYD_SERVER,
                                       '%s/' % project if project else '',
                                       '%s/' % spider if spider else '')
    auth = SCRAPYD_SERVERS_AUTH
    url_auth = url.replace('http://', 'http://%s:%s@' % auth) if auth else url
    status_code, text = make_request(url, api=False, auth=auth)

    # if status_code != 200 or not re.search(r'Directory', text):
    #     return render_template(TEMPLATE_RESULT, node=node,
    #                            url=url_auth, status_code=status_code, text=text)

    rows = [dict(zip(keys_directory, row)) for row in pattern_directory.findall(text)]

    for row in rows:
        if project and spider:
            # <a href="098726cca42b11e8a8b514dda9e91c2f.log">098726cca42b11e8a8b514dda9e91c2f.log</a>
            m = re.search(r'>(.*?)<', row['filename'])
            filename = m.group(1)
            # row['filename'] = filename
            # UnicodeEncodeError: 'ascii' codec can't encode characters in position 57-58: ordinal not in range(128)
            row['filename'] = u'<a class="link" target="_blank" href="{}">{}</a>'.format(
                               url_auth + filename, filename)
            # job = filename.rpartition('.')[0] or filename
            job = filename

            row['url_log_utf8'] = url_for('log.log', opt='utf8', project=project, spider=spider,
                                           job=job, ext='ext')
            row['url_log_stats'] = url_for('log.log', opt='stats', project=project, spider=spider,
                                            job=job, ext='ext')

        else:
            # <a href="proxy/">proxy/</a>
            
            row['filename'] = re.sub(r'href=', 'class="link" href=', row['filename'])


    return render_template('log/logs.html', title=title, navis=navis, project=project, spider=spider, rows=rows, url=url_auth)