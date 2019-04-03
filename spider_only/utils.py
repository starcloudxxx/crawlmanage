# coding: utf8
import re
import json
import time
import datetime
from pprint import pprint
import pymssql
from .vars import (SQLSERV_DB, SQLSERV_HOST, SQLSERV_PSWD, SQLSERV_TABLE, 
                        SQLSERV_USER)

import requests
from flask import current_app as app

session = requests.Session()


def make_request(url, data=None, timeout=60, api=True, log=True, auth=None):
    """
    :param api: return dict if set True, else text
    """
    try:
        if log:
            if 'addversion.json' in url and data:
                app.logger.debug('>>>>> %s %s %s' % ('POST' if data else 'GET', url,
                                                     {'project': data.get('project'), 'version': data.get('project'),
                                                      'egg': "%s bytes binary egg file" % len(data.get('egg'))}))
            else:
                app.logger.debug('>>>>> %s %s %s' % ('POST' if data else 'GET', url, data or ''))
                if data:
                    pprint(data)
        if data:
            r = session.post(url, data=data, timeout=timeout, auth=auth)
        else:
            r = session.get(url, timeout=timeout, auth=auth)
        r.encoding = 'utf8'
    except Exception as err:
        if log:
            app.logger.error('!!!!! %s %s' % (err.__class__.__name__, err))
        if api:
            return -1, {'url': url, 'auth': auth, 'status_code': -1,
                        'status': 'error', 'message': str(err)}
        else:
            return -1, str(err)
    else:
        if api:
            try:
                r_json = r.json()
            except json.JSONDecodeError: # When Scrapyd server reboot, listprojects got 502 html
                r_json = {'status': 'error', 'message': r.text}
            finally:
                if log:
                    sign = '!!!!! ' if (r.status_code != 200 or r_json.get('status') != 'ok') else '<<<<< '
                    app.logger.debug('%s%s %s' % (sign, r.status_code, r_json))
                r_json.update(dict(url=url, auth=auth, status_code=r.status_code))

                return r.status_code, r_json
        else:
            if r.status_code == 200:
                front = r.text[:min(100, len(r.text))].replace('\n', '')
                back = r.text[-min(100, len(r.text)):].replace('\n', '')
                if log:
                    app.logger.debug('<<<<< %s %s\n...%s' % (r.status_code, front, back))
            else:
                if log:
                    app.logger.debug('!!!!! %s %s' % (r.status_code, r.text))

            return r.status_code, r.text


def json_dumps(obj):
    return json.dumps(obj, ensure_ascii=False, indent=4, sort_keys=True)

def get_Date_limit(namelist):
    cnx = pymssql.connect()
    cur = cnx.cursor()

    result = {}

    sql_string = "SELECT last_date, FROM " + SQLSERV_TABLE + " WHERE name=%s" 
    for nn in namelist:

        if cur.execute(sql_string, nn):
            aldata = cur.fetchone()
            last_Date = aldata[0]
            daylimit = aldata[1]
            result.setdefault(nn,[last_Date,daylimit])
        else:
            result.setdefault(nn,[None,None])
    
    return result


def get_Date_Color(last_date, limit):
    last_Date = last_date
    now_Date = datetime.datetime.now()
    time_delta = now_Date - last_Date
    Days = time_delta.days
    Seconds = time_delta.seconds

    color_Style = [
        "#228B22","#FFD700","#FF0000"
    ]
    if Days == 0:
        Hours = int(Seconds/3600)
        if Hours == 0:
            return "1小时内", 
        return str(Hours)+"小时前", 

    day_Limit = limit.split(",")
    for i in range(0,3):
        if Days < int(day_Limit[i]):
            return str(Days)+"天前", color_Style[i]

    return "超出爬取上限", color_Style[2]

# coding: utf8
from collections import OrderedDict


class Slot:
    def __init__(self, limit_egg=10, limit_data=10):
        self.limit_egg = limit_egg
        self.limit_data = limit_data
        self._egg = OrderedDict()
        self._data = OrderedDict()

    @property
    def egg(self):
        return self._egg

    @property
    def data(self):
        return self._data

    def add_egg(self, key, value):
        self._egg[key] = value
        if len(self._egg) > self.limit_egg:
            self._egg.popitem(last=False)


    def add_data(self, key, value):
        self._data[key] = value
        if len(self._data) > self.limit_data:
            self._data.popitem(last=False)

slot = Slot()




pattern_datetime = '\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}'
# 2018-06-25 18:12:49 [scrapy.extensions.logstats] INFO: Crawled 2318 pages (at 2 pages/min), scraped 68438 items (at 60 items/min)
pattern_datas = re.compile(r"""\n(?P<time_>%s).*?
                            Crawled\s(?P<pages>\d+)\s+pages\s
                            \(at\s(?P<pages_min>\d+)\spages/min\),\s
                            scraped\s(?P<items>\d+)\sitems\s
                            \(at\s(?P<items_min>\d+)\sitems/min\)
                            """ % pattern_datetime, re.X)

pattern_datas_germany = re.compile(r"""\n(?P<time_>%s).*?\[\w+\].*?
                            Crawled\s(?P<pages>\d+)\s+pages\s
                            \(at\s(?P<pages_min>\d+)\spages/min\),\s
                            scraped\s(?P<items>\d+)\sitems\s
                            \(at\s(?P<items_min>\d+)\sitems/min\)
                            """ % pattern_datetime, re.X)


patterns = [
    '\]\sCRITICAL:',
    '\]\sERROR:',
    '\]\sWARNING:',
    'Retrying\s<',
    'Redirecting\s\(',
    'Ignoring\sresponse\s<',
]
pattern_logs_count_list = []
for p in patterns:
    pattern = re.compile(r"""\n
                            (\d{4}[^\n]*?%s.*?)
                            (?=\n\d{4}[^\n]*?(?:DEBUG|INFO|WARNING|ERROR|CRITICAL))
                        """ % p, re.S | re.X)
    pattern_logs_count_list.append(pattern)



def parse_log(text, kwargs):
    fake_time = '2018-01-01 00:00:01'
    lines = re.split('\r*\n', text)

    def re_search_final_match(pattern, default='', step=-1):
        for line in lines[::step]:
            m = re.search(pattern, line)
            if m:
                return line
        else:
            return default

    kwargs['first_log_time'] = re_search_final_match(r'^%s' % pattern_datetime, step=1)[:19] or fake_time
    kwargs['last_log_time'] = re_search_final_match(r'^%s' % pattern_datetime)[:19] or fake_time
    first_log_datetime = datetime.datetime.strptime(kwargs['first_log_time'], '%Y-%m-%d %H:%M:%S')
    last_log_datetime = datetime.datetime.strptime(kwargs['last_log_time'], '%Y-%m-%d %H:%M:%S')
    kwargs['last_log_timestamp'] = time.mktime(last_log_datetime.timetuple())
    kwargs['elasped'] = str(last_log_datetime - first_log_datetime)

    kwargs['head_lines'] = '\n'.join(lines[:50])
    kwargs['tail_lines'] = '\n'.join(lines[-50:])

    # Extract datas for chart
    datas = pattern_datas_germany.findall(text)


    # str(time_) to avoid [u'2018-08-22 18:43:05', 0, 0, 0, 0] in js using python2
    kwargs['datas'] = [[str(time_), int(pages), int(pages_min), int(items), int(items_min)]
                       for (time_, pages, pages_min, items, items_min) in datas]
    kwargs['crawled_pages'] = datas[-1][1] if datas else 0
    kwargs['scraped_items'] = datas[-1][3] if datas else 0

    # Extract only last log
    last_tuples = [
        # ('resuming_crawl', 'Resuming\scrawl'),
        ('last_offsite', 'Filtered\soffsite'),
        ('last_duplicate', 'Filtered\sduplicate'),
        ('last_crawl', 'Crawled\s\(\d+'),
        ('last_scrape', 'Scraped\sfrom\s'),
        ('last_item', '^\{.*\}'),
        ('last_stat', 'Crawled\s\d+\spages'),
    ]
    last_matchs = [('resuming_crawl', re_search_final_match('Resuming\scrawl', step=1))]
    for k, v in last_tuples:
        ret = re_search_final_match(v)
        last_matchs.append((k, ret))
        if k == 'last_crawl':
            last_crawl_datetime = datetime.datetime.strptime(ret[:19] or fake_time, '%Y-%m-%d %H:%M:%S')
        elif k == 'last_scrape':
            last_scrape_datetime = datetime.datetime.strptime(ret[:19] or fake_time, '%Y-%m-%d %H:%M:%S')

    kwargs['last_crawl_timestamp'] = time.mktime(last_crawl_datetime.timetuple())
    kwargs['last_scrape_timestamp'] = time.mktime(last_scrape_datetime.timetuple())
    kwargs['last_matchs'] = last_matchs

    # Extract log count and details
    logs_count_tuples = [
        ('log_critical_logs', 'log_critical_logs_details', 'log_critical_count'),
        ('log_error_logs', 'log_error_logs_details', 'log_error_count'),
        ('log_warning_logs', 'log_warning_logs_details', 'log_warning_count'),
        ('retry_logs', 'retry_logs_details', 'retry_count'),
        ('redirect_logs', 'redirect_logs_details', 'redirect_count'),
        ('ignore_logs', 'ignore_logs_details', 'ignore_count'),
    ]
    text += '2018 DEBUG'
    re_matchs = []
    for idx, (pattern, (log_title, log_details, log_count)) in enumerate(
            zip(pattern_logs_count_list, logs_count_tuples)):
        matchs = pattern.findall(text)
        count = len(matchs)
        kwargs[log_count] = count

        re_matchs.append({
            'log_title': log_title,
            'log_details': log_details,
            'count': count,
            'line': matchs[-1] if matchs else '',
            # 'lines': '\n'.join(matchs) #if idx < 3 else '',
            'lines': matchs
        })
    kwargs['re_matchs'] = re_matchs
