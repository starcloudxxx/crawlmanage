# coding: utf8

DEBUG=False

SPIDER_HOST = '0.0.0.0'
SPIDER_PORT = 22555

# to find out where the Scrapy logs are stored."
SCRAPYD_LOGS_DIR = ''

# The extension used to locate scrapy log in dashboard, and the order matters
SCRAPYD_LOG_EXTENSIONS = ['.log', '.log.gz', '.gz', '.txt', '']

# Set True to hide Items page and Items column in Dashboard page
HIDE_SCRAPYD_ITEMS = False

# Set True to show jobid in Dashboard page
SHOW_DASHBOARD_JOB_COLUMN = False

#
SCRAPYD_SERVER = '127.0.0.1:6800'

# Set True to disable caching utf8 and stats files in the background periodically
DISABLE_CACHE = True
# Sleep seconds between the end of last round of caching and the start of next round
CACHE_ROUND_INTERVAL = 300
# Sleep seconds between every request while caching
CACHE_REQUEST_INTERVAL = 10
# Set True to delete cached utf8 and stats files at startup
DELETE_CACHE = False