# coding: utf8
import os
import re

CWD = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(CWD, 'data')
UPLOAD_PATH = os.path.join(CWD, 'data/upload')
CACHE_PATH = os.path.join(CWD, 'data/cache')
DEPLOY_PATH = os.path.join(CWD, 'data/deploy')
SCHEDULE_PATH = os.path.join(CWD, 'data/schedule')

for p in [DATA_PATH, UPLOAD_PATH, CACHE_PATH, DEPLOY_PATH, SCHEDULE_PATH]:
    if not os.path.isdir(p):
        os.mkdir(p)

INFO = 'info'
WARN = 'warning'
DEFAULT_LATEST_VERSION = "default: the latest version"


UA_DICT = {
    'chrome': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
    'iOS': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1',
    'iPad': 'Mozilla/5.0 (iPad; CPU OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
    'Android': 'Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36',
}

#template_address
TEMPLATE_INDEX = 'index.html'
TEMPLATE_SPIDERS = 'spiders.html'

#navi name
NAVI_NAME = [
    {
        "node":1,
        "name":"新闻媒体"
    },
    {
        "node":2,
        "name":"原始文献"
    },
    {
        "node":3,
        "name":"学术论文"
    }
]

#for website
WEBSITE_NAME = {
    "1":[
        {
            "order" : 1,
            "name" : "人民网",
            "language": "中文",
            "url":"http://www.people.com.cn/",
            "link" : "http://www.people.com.cn/",
            "project":"universalspider",
            "spider":"people"
        },
        {
            "order" : 2,
            "name" : "光明网",
            "language": "中文",
            "url":"http://www.gmw.cn/",
            "link" : "http://www.gmw.cn/",
            "project":None,
            "spider":None
        },
        {
            "order" : 3,
            "name" : "环球网",
            "language": "中文",
            "url":"http://www.huanqiu.com/",
            "link" : "http://www.huanqiu.com/",
            "project":None,
            "spider":None
        },
        {
            "order" : 4,
            "name" : "新华网",
            "language": "中文",
            "url":"http://www.xinhuanet.com/",
            "link" : "http://www.xinhuanet.com/",
            "project":None,
            "spider":None
        },
        {
            "order" : 5,
            "name" : "人民日报",
            "language": "中文",
            "url":"http://paper.people.com.cn/",
            "link" : "http://paper.people.com.cn/rmrb/html/2018-10/24/nbs.D110000renmrb_01.htm",
            "project":None,
            "spider":None
        },
        {
            "order" : 6,
            "name" : "光明日报",
            "language": "中文",
            "url":"http://epaper.gmw.cn/",
            "link" : "http://epaper.gmw.cn/gmrb/html/2018-10/24/nbs.D110000gmrb_01.htm",
            "project":None,
            "spider":None
        },
        {
            "order" : 7,
            "name" : "中国社会科学报",
            "language": "中文",
            "url":"http://www.csstoday.so/",
            "link" : "http://www.csstoday.so/",
            "project":None,
            "spider":None
        },        
        {
            "order" : 8,
            "name" : "环球时报",
            "language": "中文",
            "url":"http://www.jdqu.com/",
            "link" : "http://www.jdqu.com/bklist-11.html",
            "project":None,
            "spider":None
        },        
        {
            "order" : 9,
            "name" : "中国网",
            "language": "中文",
            "url": "http://www.china.com.cn/",
            "link" : "http://www.china.com.cn/",
            "project":None,
            "spider":None
        },
        {
            "order" : 10,
            "name" : "澎湃新闻",
            "language": "中文",
            "url": "https://www.thepaper.cn/",
            "link" : "https://www.thepaper.cn/",
            "project":None,
            "spider":None
        }
    ],
    "2":[
        {
            "order" : 1,
            "name" : "上海市人民市政府",
            "language": "中文",
            "url" : "http://www.shanghai.gov.cn/",
            "link" : "http://www.shanghai.gov.cn/",
            "project":None,
            "spider":None
        },
        {
            "order" : 2,
            "name" : "北京市人民政府",
            "language": "中文",
            "url": "http://www.beijing.gov.cn/",
            "link" : "http://www.beijing.gov.cn/",
            "project":None,
            "spider":None
        },
        {
            "order" : 3,
            "name" : "浙江政务服务网",
            "language": "中文",
            "url": "http://www.zjzwfw.gov.cn/",
            "link" : "http://www.zjzwfw.gov.cn/",
            "project":None,
            "spider":None
        },
        {
            "order" : 4,
            "name" : "江苏省人民政府",
            "language": "中文",
            "url": "http://www.jiangsu.gov.cn/",
            "link" : "http://www.jiangsu.gov.cn/",
            "project":None,
            "spider":None
        },
        {
            "order" : 5,
            "name" : "教育部",
            "language": "中文",
            "url": "http://www.moe.gov.cn/",
            "link" : "http://www.moe.gov.cn/",
            "project":None,
            "spider":None
        },
        {
            "order" : 6,
            "name" : "科技部",
            "language": "中文",
            "url": "http://www.most.gov.cn/",
            "link" : " http://www.most.gov.cn/",
            "project":None,
            "spider":None
        }       
    ],
    "3":[
        {
            "order" : 1,
            "name" : "中国知网",
            "language": "中文",
            "url":"http://epub.cnki.net/kns/default.htm",
            "link" : "http://epub.cnki.net/kns/default.htm",
            "project":None,
            "spider":None
        },
        {
            "order" : 2,
            "name" : "维普中文期刊服务平台",
            "language": "中文",
            "url":"http://qikan.cqvip.com/",
            "link" : "http://qikan.cqvip.com/",
            "project":None,
            "spider":None
        },
        {
            "order" : 3,
            "name" : "国际论坛",
            "language": "中文",
            "url":"http://qikan.cqvip.com...",
            "link" : "http://qikan.cqvip.com/journal/summary.aspx?gch=91406X&from=journal_journalsearch",
            "project":None,
            "spider":None
        },
        {
            "order" : 4,
            "name" : "世界经济与政治",
            "language": "中文",
            "url":"http://qikan.cqvip.com...",
            "link" : "http://qikan.cqvip.com/journal/summary.aspx?gch=92442X&from=journal_journalsearch",
            "project":None,
            "spider":None
        },
        {
            "order" : 5,
            "name" : "外交评论",
            "language": "中文",
            "url":"http://qikan.cqvip.com...",
            "link" : "http://qikan.cqvip.com/journal/summary.aspx?gch=90401A&from=journal_journalsearch",
            "project":None,
            "spider":None
        }
    ]
}
WEBSITE_ORDER = {
    "1":[
        {
            "project":"universalspider",
            "spider":"people"
        },
        {
            "project":None,
            "spider":None
        },
        {
            "project":None,
            "spider":None
        },
        {
            "project":None,
            "spider":None
        },
        {
            "project":None,
            "spider":None
        },
        {
            "project":None,
            "spider":None
        },
        {
            "project":None,
            "spider":None
        },
        {
            "project":None,
            "spider":None
        },
        {
            "project":None,
            "spider":None
        },
        {
            "project":None,
            "spider":None
        }
    ],
    "2":[
        {
            "project":None,
            "spider":None
        },
        {
            "project":None,
            "spider":None
        },
        {
            "project":None,
            "spider":None
        },
        {
            "project":None,
            "spider":None
        },
        {
            "project":None,
            "spider":None
        },
        {
            "project":None,
            "spider":None
        }
    ],
    "3":[
        {
            "project":None,
            "spider":None
        },
        {
            "project":None,
            "spider":None
        },
        {
            "project":None,
            "spider":None
        },
        {
            "project":None,
            "spider":None
        },
        {
            "project":None,
            "spider":None
        }
    ]
}




# For dashboard
pattern_jobs = re.compile(r"""<tr>
                        <td>(?P<Project>.*?)</td>
                        <td>(?P<Spider>.*?)</td>
                        <td>(?P<Job>.*?)</td>
                        (?:<td>(?P<PID>.*?)</td>)?
                        (?:<td>(?P<Start>.*?)</td>)?
                        (?:<td>(?P<Runtime>.*?)</td>)?
                        (?:<td>(?P<Finish>.*?)</td>)?
                        (?:<td>(?P<Log>.*?)</td>)?
                        (?:<td>(?P<Items>.*?)</td>)?
                        </tr>
                    """, re.X)
keys_jobs = ['project', 'spider', 'job', 'pid', 'start', 'runtime', 'finish', 'log', 'items']

# For run.py
# r'^(?:(?:(.*?)\:)(?:(.*?)@))?(.*?)(?:\:(.*?))?(?:#(.*?))?$'
pattern_scrapyd_server = re.compile(r"""
                        ^
                        (?:
                            (?:(.*?)\:)     # username:
                            (?:(.*?)@)      # password@
                        )?
                        (.*?)               # ip
                        (?:\:(.*?))?        # :port
                        (?:\#(.*?))?        # #group
                        $
                    """, re.X)

# For directory
pattern_directory = re.compile(r"""<tr\sclass="(?P<odd_even>odd|even)">\n
                                   \s+<td>(?P<filename>.*?)</td>\n
                                   \s+<td>(?P<size>.*?)</td>\n
                                   \s+<td>(?P<content_type>.*?)</td>\n
                                   \s+<td>(?P<content_encoding>.*?)</td>\n
                                </tr>
                                """, re.X)

keys_directory = ['odd_even', 'filename', 'size', 'content_type', 'content_encoding']
