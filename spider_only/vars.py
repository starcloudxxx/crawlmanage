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
        "name":"智库报告"
    },
    {
        "node":4,
        "name":"学术论文"
    }
]

#for website 
#spider is same as name , and must be unique
WEBSITE_NAME = [
    {
        "people":{
            "order" : 1,
            "name" : "人民网",
            "language": "中文",
            "url":"http://www.people.com.cn/",
            "link" : "http://www.people.com.cn/",
            "project":"universalspider",
            "spider":"people"
        },
        "gmw":{
            "order" : 2,
            "name" : "光明网",
            "language": "中文",
            "url":"http://www.gmw.cn/",
            "link" : "http://www.gmw.cn/",
            "project":"universalspider",
            "spider":"china"
        },
        "huanqiu":{
            "order" : 3,
            "name" : "环球网",
            "language": "中文",
            "url":"http://www.huanqiu.com/",
            "link" : "http://www.huanqiu.com/",
            "project":"universalspider",
            "spider":"huanqiu"
        },
        "xinhua":{
            "order" : 4,
            "name" : "新华网",
            "language": "中文",
            "url":"http://www.xinhuanet.com/",
            "link" : "http://www.xinhuanet.com/",
            "project":"universalspider",
            "spider":"china"
        },
        "rmrb":{
            "order" : 5,
            "name" : "人民日报",
            "language": "中文",
            "url":"http://paper.people.com.cn/",
            "link" : "http://paper.people.com.cn/rmrb/html/2018-10/24/nbs.D110000renmrb_01.htm",
            "project":"universalspider",
            "spider":"rmrb"
        },
        "gmrb":{
            "order" : 6,
            "name" : "光明日报",
            "language": "中文",
            "url":"http://epaper.gmw.cn/",
            "link" : "http://epaper.gmw.cn/gmrb/html/2018-10/24/nbs.D110000gmrb_01.htm",
            "project":"universalspider",
            "spider":"china"
        },
        "cssn":{
            "order" : 7,
            "name" : "中国社会科学报",
            "language": "中文",
            "url":"http://www.csstoday.so/",
            "link" : "http://www.csstoday.so/",
            "project":"universalspider",
            "spider":"cssn"
        },        
        "hqsb":{
            "order" : 8,
            "name" : "环球时报",
            "language": "中文",
            "url":"http://www.jdqu.com/",
            "link" : "http://www.jdqu.com/bklist-11.html",
            "project":"universalspider",
            "spider":"universalspider"
        },        
        "china":{
            "order" : 9,
            "name" : "中国网",
            "language": "中文",
            "url": "http://www.china.com.cn/",
            "link" : "http://www.china.com.cn/",
            "project":"universalspider",
            "spider":"china"
        },
        "thepaper":{
            "order" : 10,
            "name" : "澎湃新闻",
            "language": "中文",
            "url": "https://www.thepaper.cn/",
            "link" : "https://www.thepaper.cn/",
            "project":"universalspider",
            "spider":"china"
        },
        "tagesschau":{
            "order" : 11,
            "name" : "tagesschau.de",
            "language": "德文",
            "url": "https://www.tagesschau.de/",
            "link" : "https://www.tagesschau.de/",
            "project":"universalspider",
            "spider":"tagess"
        },
        "sueddeutsche":{
            "order" : 12,
            "name" : "SUEDDEUTSCHE ZEITUNG",
            "language": "德文",
            "url": "https://www.sueddeutsche.de/",
            "link" : "https://www.sueddeutsche.de/",
            "project":"universalspider",
            "spider":"china"
        },
        "spiegel":{
            "order" : 13,
            "name" : "SPIEGEL ONLINE",
            "language": "德文",
            "url":"http://www.spiegel.de/",
            "link" : "http://www.spiegel.de/",
            "project":"universalspider",
            "spider":"china"
        },
        "zeit":{
            "order" : 14,
            "name" : "ZEIT ONLINE",
            "language": "德文",
            "url": "https://www.zeit.de/",
            "link" : "https://www.zeit.de/",
            "project":"universalspider",
            "spider":"universalspider"
        },
        "faz":{
            "order" : 15,
            "name" : "Franffurter Allgemeine",
            "language": "德文",
            "url": "http://www.faz.net/",
            "link" : "http://www.faz.net/",
            "project":"universalspider",
            "spider":"universalspider"
        },
        "welt":{
            "order" : 16,
            "name" : "WeLT",
            "language": "德文",
            "url": "https://www.welt.de/",
            "link" : "https://www.welt.de/",
            "project":"universalspider",
            "spider":"universalspider"
        },
        "handelsblatt":{
            "order" : 17,
            "name" : "Handelsblatt",
            "language": "德文",
            "url": "http://www.handelsblatt.de/",
            "link" : "http://www.handelsblatt.de/",
            "project":"universalspider",
            "spider":"universalspider"
        },
        "focus":{
            "order" : 18,
            "name" : "FOCUS ONLINE",
            "language": "德文",
            "url": "https://www.focus.de/",
            "link" : "https://www.focus.de/",
            "project":"universalspider",
            "spider":"universalspider"
        },
        "tagesspiegel":{
            "order" : 19,
            "name" : "DER TAGESSPIEGEL",
            "language": "德文",
            "url": "http://www.tagesspiegel.de/",
            "link" : "http://www.tagesspiegel.de/",
            "project":"universalspider",
            "spider":"universalspider"
        },
        "huffpost":{
            "order" : 20,
            "name" : "HUFFPOST",
            "language": "德文",
            "url": "http://www.huffingtonpost.de/",
            "link" : "http://www.huffingtonpost.de/",
            "project":"universalspider",
            "spider":"universalspider"
        },
        "nytimes":{
            "order" : 21,
            "name" : "The New York Times",
            "language": "英文",
            "url": "http://www.nytimes.com/",
            "link" : "http://www.nytimes.com/",
            "project":"universalspider",
            "spider":"universalspider"
        },
        "euobserver":{
            "order" : 22,
            "name" : "euobserver",
            "language": "英文",
            "url": "https://euobserver.com/",
            "link" : "https://euobserver.com/",
            "project":"universalspider",
            "spider":"universalspider"
        },	
        "ft":{
            "order" : 23,
            "name" : "FINANCIAL TIMES",
            "language": "英文",
            "url": "https://www.ft.com/",
            "link" : "https://www.ft.com/",
            "project":"universalspider",
            "spider":"universalspider"
        },	
        "reuters":{
            "order" : 24,
            "name" : "REUTERS",
            "language": "英文",
            "url": "http://www.reuters.com/",
            "link" : "http://www.reuters.com/",
            "project":"universalspider",
            "spider":"universalspider"
        },
        "thediplomat":{
            "order" : 25,
            "name" : "THE DIPLOMAT",
            "language": "英文",
            "url": "https://thediplomat.com/",
            "link" : "https://thediplomat.com/",
            "project":"universalspider",
            "spider":"universalspider"
        }
    },
    {
        "fmprc":{
            "order" : 1,
            "name" : "外交部",
            "language": "中文",
            "url" : "https://www.fmprc.gov.cn/web/",
            "link" : "https://www.fmprc.gov.cn/web/",
            "project":"universalspider",
            "spider":"fmprc"
        },
        "most":{
            "order" : 2,
            "name" : "科技部",
            "language": "中文",
            "url": "http://www.most.gov.cn/",
            "link" : "http://www.most.gov.cn/",
            "project":"universalspider",
            "spider":"most"
        },
        "miit":{
            "order" : 3,
            "name" : "工信部",
            "language": "中文",
            "url": "http://www.miit.gov.cn/",
            "link" : "http://www.miit.gov.cn/",
            "project":"universalspider",
            "spider":"miit"
        },
        "moe":{
            "order" : 4,
            "name" : "教育部",
            "language": "中文",
            "url": "http://www.moe.gov.cn/",
            "link" : "http://www.moe.gov.cn/",
            "project":"universalspider",
            "spider":"china"
        },
        "bundesregierung":{
            "order" : 5,
            "name" : "Bundesregierung",
            "language": "德文",
            "url": "https://www.bundesregierung.de/breg-de",
            "link" : "https://www.bundesregierung.de/breg-de",
            "project":"universalspider",
            "spider":"china"
        },
        "auswaertiges":{
            "order" : 6,
            "name" : "Auswartiges Amt Seitennavigation",
            "language": "德文",
            "url": "https://www.auswaertiges-amt.de/de/",
            "link" : "https://www.auswaertiges-amt.de/de/",
            "project":"universalspider",
            "spider":"china"
        },
        "bmwi":{
            "order" : 7,
            "name" : "Bundesministerium fur Wirtschaft und Energie",
            "language": "德文",
            "url": "https://www.bmwi.de/Navigation/DE/Home/home.html",
            "link" : "https://www.bmwi.de/Navigation/DE/Home/home.html",
            "project":"universalspider",
            "spider":"china"
        },        
        "bundestag":{
            "order" : 8,
            "name" : "Deutscher Bundestag",
            "language": "德文",
            "url": "https://www.bundestag.de/",
            "link" : "https://www.bundestag.de/",
            "project":"universalspider",
            "spider":"china"
        },        
        "euunion":{
            "order" : 9,
            "name" : "European Union",
            "language": "英文",
            "url": "https://europa.eu/european-union/index_en",
            "link" : "https://europa.eu/european-union/index_en",
            "project":"universalspider",
            "spider":"china"
        },
        "euparliament":{
            "order" : 10,
            "name" : "European Parliament",
            "language": "英文",
            "url": "http://www.europarl.europa.eu/portal/en",
            "link" : "http://www.europarl.europa.eu/portal/en",
            "project":"universalspider",
            "spider":"china"
        },
        "eucommission":{
            "order" : 11,
            "name" : "European Commission",
            "language": "英文",
            "url": "https://ec.europa.eu/commission/index_en",
            "link" : "https://ec.europa.eu/commission/index_en",
            "project":"universalspider",
            "spider":"china"
        },
        "diplo":{
            "order" : 12,
            "name" : "Deutsche Vertretungen in China",
            "language": "德文",
            "url": "https://china.diplo.de/",
            "link" : "https://china.diplo.de/",
            "project":"universalspider",
            "spider":"china"
        },
        "botschaft":{
            "order" : 13,
            "name" : "中华人民共和国驻德意志联邦共和国大使馆",
            "language": "中文",
            "url": "http://www.china-botschaft.de/det/",
            "link" : "http://www.china-botschaft.de/det/",
            "project":"universalspider",
            "spider":"china"
        }
    },
    {
        "swp":{
            "order" : 1,
            "name" : "SWP",
            "language": "德文",
            "url" : "https://www.swp-berlin.org/",
            "link" : "https://www.swp-berlin.org/",
            "project":"universalspider",
            "spider":"swp"
        },
        "gigahamburg":{
            "order" : 2,
            "name" : "GIGA",
            "language": "德文",
            "url" : "https://www.giga-hamburg.de/",
            "link" : "https://www.giga-hamburg.de/",
            "project":"universalspider",
            "spider":"china"
        },
        "dgap":{
            "order" : 3,
            "name" : "DGAP",
            "language": "德文",
            "url" : "https://dgap.org/",
            "link" : "https://dgap.org/",
            "project":"universalspider",
            "spider":"china"
        },
        "merics":{
            "order" : 4,
            "name" : "merics",
            "language": "德文",
            "url" : "https://www.merics.org/cn/",
            "link" : "https://www.merics.org/cn/",
            "project":"universalspider",
            "spider":"china"
        },
        "kas":{
            "order" : 5,
            "name" : "Konrad Adenauer Stiftung",
            "language": "德文",
            "url" : "http://www.kas.de/",
            "link" : "http://www.kas.de/",
            "project":"universalspider",
            "spider":"china"
        },
        "fes":{
            "order" : 6,
            "name" : "Friedrich Ebert Stiftung",
            "language": "德文",
            "url" : "http://www.fes.de/",
            "link" : "http://www.fes.de/",
            "project":"universalspider",
            "spider":"china"
        },
        "ecfr":{
            "order" : 7,
            "name" : "European council on foreign relations",
            "language": "英文",
            "url" : "http://www.ecfr.eu/",
            "link" : "http://www.ecfr.eu/",
            "project":"universalspider",
            "spider":"china"
        },
        "gmfus":{
            "order" : 8,
            "name" : "GMF",
            "language": "英文",
            "url" : "http://www.gmfus.org",
            "link" : "http://www.gmfus.org",
            "project":"universalspider",
            "spider":"china"
        },
        "foreignaffairs":{
            "order" : 9,
            "name" : "Foreign Affairs",
            "language": "英文",
            "url" : "https://www.foreignaffairs.com",
            "link" : "https://www.foreignaffairs.com",
            "project":"universalspider",
            "spider":"china"
        }      
    },
    {
        "ozyj":{
            "order" : 1,
            "name" : "欧洲研究",
            "language": "中文",
            "url":"http://qikan.cqvip.com...",
            "link" : "http://qikan.cqvip.com/journal/summary.aspx?gch=92440B&from=journal_journalsearch",
            "project":"universalspider",
            "spider":"china"
        },
        "dgyj":{
            "order" : 2,
            "name" : "德国研究",
            "language": "中文",
            "url":"http://qikan.cqvip.com...",
            "link" : "http://qikan.cqvip.com/journal/summary.aspx?gch=82454X&from=journal_journalsearch",
            "project":"universalspider",
            "spider":"china"
        },
        "gjlt":{
            "order" : 3,
            "name" : "国际论坛",
            "language": "中文",
            "url":"http://qikan.cqvip.com...",
            "link" : "http://qikan.cqvip.com/journal/summary.aspx?gch=91406X&from=journal_journalsearch",
            "project":"universalspider",
            "spider":"china"
        },
        "sjjjyzz":{
            "order" : 4,
            "name" : "世界经济与政治",
            "language": "中文",
            "url":"http://qikan.cqvip.com...",
            "link" : "http://qikan.cqvip.com/journal/summary.aspx?gch=92442X&from=journal_journalsearch",
            "project":"universalspider",
            "spider":"china"
        },
        "gjwtyj":{
            "order" : 5,
            "name" : "国际问题研究",
            "language": "中文",
            "url":"http://qikan.cqvip.com...",
            "link" : "http://qikan.cqvip.com/journal/summary.aspx?gch=94094X&from=journal_journalsearch",
            "project":"universalspider",
            "spider":"china"
        },
        "xdgjgx":{
            "order" : 6,
            "name" : "现代国际关系",
            "language": "中文",
            "url":"http://qikan.cqvip.com...",
            "link" : "http://qikan.cqvip.com/journal/summary.aspx?gch=81437X&from=journal_journalsearch",
            "project":"universalspider",
            "spider":"china"
        },
        "wjpl":{
            "order" : 7,
            "name" : "外交评论",
            "language": "中文",
            "url":"http://qikan.cqvip.com...",
            "link" : "http://qikan.cqvip.com/journal/summary.aspx?gch=90401A&from=journal_journalsearch",
            "project":"universalspider",
            "spider":"china"
        },        
        "gjzw":{
            "order" : 8,
            "name" : "国际展望",
            "language": "中文",
            "url":"http://qikan.cqvip.com...",
            "link" : "http://qikan.cqvip.com/journal/summary.aspx?gch=95355X&from=journal_journalsearch",
            "project":"universalspider",
            "spider":"china"
        },        
        "fwecpo":{
            "order" : 9,
            "name" : "世界经济与政治论坛",
            "language": "中文",
            "url": "http://qikan.cqvip.com...",
            "link" : "http://qikan.cqvip.com/journal/summary.aspx?gch=96476A&from=journal_journalsearch",
            "project":"universalspider",
            "spider":"china"
        },
        "ipos":{
            "order" : 10,
            "name" : "国际政治研究",
            "language": "中文",
            "url": "http://qikan.cqvip.com...",
            "link" : "http://qikan.cqvip.com/journal/summary.aspx?gch=82189X&from=journal_journalsearch",
            "project":"universalspider",
            "spider":"china"
        },
        "cwoso":{
            "order" : 11,
            "name" : "当代世界与社会主义",
            "language": "中文",
            "url": "http://qikan.cqvip.com...",
            "link" : "http://qikan.cqvip.com/journal/summary.aspx?gch=81866X&from=journal_journalsearch",
            "project":"universalspider",
            "spider":"china"
        },
        "zfas":{
            "order" : 12,
            "name" : "ZEITSCHRIFT FUR AUSSEN- UND SICHERHEITSPOLITI",
            "language": "德文",
            "url": "https://link.springer.com...",
            "link" : "https://link.springer.com/journal/volumesAndIssues/12399",
            "project":"universalspider",
            "spider":"china"
        },
        "jcms":{
            "order" : 13,
            "name" : "JOURNAL OF COMMON MARKET STUDIES",
            "language": "英文",
            "url":"http://web.b.ebscohost.com/ehost...",
            "link" : "http://web.b.ebscohost.com/ehost/command/detail?vid=0&sid=e395bf23-0212-426a-b2cf-30db4a08b898%40sessionmgr120&bdata=JnNpdGU9ZWhvc3QtbGl2ZQ%3d%3d#jid=CMS&db=bth",
            "project":"universalspider",
            "spider":"china"
        },
        "wepo":{
            "order" : 14,
            "name" : "WEST EUROPEAN POLITICS",
            "language": "英文",
            "url": "http://web.a.ebscohost.com/...",
            "link" : "http://web.a.ebscohost.com/ehost/command/detail?vid=0&sid=35d48b2c-1cbd-4678-91be-e3c954c2004c%40sdc-v-sessmgr02&bdata=JnNpdGU9ZWhvc3QtbGl2ZQ%3d%3d#jid=WEP&db=a9h",
            "project":"universalspider",
            "spider":"china"
        },
        "gposo":{
            "order" : 15,
            "name" : "GERMAN POLITICS AND SOCIETY",
            "language": "英文",
            "url": "http://web.b.ebscohost.com/ehost...",
            "link" : "http://web.b.ebscohost.com/ehost/command/detail?vid=11&sid=1aecb95d-f082-4e86-9998-74c02e984622%40sessionmgr120&bdata=JnNpdGU9ZWhvc3QtbGl2ZQ%3d%3d#jid=9GJ&db=a9h",
            "project":"universalspider",
            "spider":"china"
        },
        "gpo":{
            "order" : 16,
            "name" : "GERMAN POLITICS",
            "language": "英文",
            "url": "http://web.b.ebscohost.com/ehost...",
            "link" : "http://web.b.ebscohost.com/ehost/command/detail?vid=0&sid=0cbc090c-7181-441d-9ab7-a37ddae7ef9b%40sessionmgr104&bdata=JnNpdGU9ZWhvc3QtbGl2ZQ%3d%3d#jid=6ZO&db=a9h",
            "project":"universalspider",
            "spider":"china"
        }
    }
]


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


SQLSERV_HOST = "localhost"
#SQLSERV_PORT = 
SQLSERV_USER = "fordate"
SQLSERV_PSWD = "lab760"
SQLSERV_DB = "Vip_TongJi"
SQLSERV_TABLE = "config_rules"