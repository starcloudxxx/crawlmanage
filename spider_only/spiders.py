# -*- coding=utf-8 -*-
import re

from flask import Blueprint, render_template, flash, request
from flask import current_app as app

from .vars import INFO, WARN, pattern_jobs, keys_jobs, WEBSITE_NAME, TEMPLATE_SPIDERS,NAVI_NAME
from .utils import make_request, get_Date_limit, get_Date_Color

bp = Blueprint('spiders', __name__, url_prefix='/')
check_latest_version = True

@bp.route('/<int:node>/spiders/')
def spiders(node):
    """
        params:
        node: navi显示的主要类型序号 
    """
    TEMPLATE = TEMPLATE_SPIDERS
    navis = NAVI_NAME
    title = navis[node-1]['name']

    SCRAPYD_SERVER =app.config.get('SCRAPYD_SERVER','127.0.0.1:6800')
    SCRAPYD_SERVERS_AUTH = app.config.get('SCRAPYD_SERVERS_AUTH', None)

    url = 'http://%s/jobs' % SCRAPYD_SERVER
    auth = SCRAPYD_SERVERS_AUTH
    url_auth = url.replace('http://', 'http://%s:%s@' % auth) if auth else url
    status_code, text = make_request(url, api=False, auth=auth)

    # if status_code != 200 or not re.search(r'Jobs', text):
    #     return render_template(TEMPLATE_RESULT, node=node,
    #                            url=url_auth, status_code=status_code, text=text)

    rows = [dict(zip(keys_jobs, row)) for row in pattern_jobs.findall(text)]
    print(rows)

    website = WEBSITE_NAME[node-1]

    for row in rows[::-1]:
        if not row['start']:
            row['status_text']="等待中"
        elif not row['finish']:
            row['status_text']="运行中"
        else:
            row['status_text']="已完成"
        try:
            spider_name = row['spider']
            website[spider_name].update(row)
        except:
            app.logger.debug("[wrong spider name]-------%s" % str({
                "project":row["project"],
                "spider":row["spider"]
            }))
    
    namelist = [nn for nn in website.keys()]

    result = get_Date_limit(namelist)
    #app.logger.debug("[wrong]-----%s" % str(result))
#    for k,v in result.items():
#        if v[0]:
#            date_string, color_string = get_Date_Color(v[0],v[1])
#            color = {
#                "last_Date":date_string,
#                "color":color_string
#            }
#        else:
#            color = {
#                "last_Date":"无",
#                "color":"#000000"
#            }
#        try:
#            website[k].update(color)
#        except:
#            app.logger.debug("[wrong spider name]-------%s" % str({
#                "project":row["project"],
#                "spider":row["spider"]
#            }))
        
            

    return render_template(TEMPLATE, title=title, navis=navis, all_spiders=website)

