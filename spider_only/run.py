# coding: utf8
import os
import sys
from shutil import copyfile
import re
import argparse
import subprocess
import shutil
import json

from flask import request, Response

from spider_only.vars import CACHE_PATH, DEFAULT_LATEST_VERSION, pattern_scrapyd_server
from spider_only import create_app

CWD = os.path.dirname(os.path.abspath(__file__))


def main():

    app = create_app()

    app.config.from_pyfile('settings.py')
    args = app.config
    check_args(args)
    update_app_config(app.config, args)

    print(">>> Visit ScrapydWeb at http://{host}:{port} or http://127.0.0.1:{port}".format(
        host='IP-OF-THE-HOST-WHERE-Spiderweb-RUNS-ON', port=app.config['SPIDER_PORT']))

    return app
    # app.run(host=app.config['SPIDER_HOST'], port=app.config['SPIDER_PORT'])  # , debug=True)


def check_args(args):
    print(">>> Reading settings from command line: %s" % args)

    scrapyd_logs_dir = args['SCRAPYD_LOGS_DIR']
    if scrapyd_logs_dir:
        if not os.path.isdir(scrapyd_logs_dir):
            sys.exit("!!! scrapyd_logs_dir NOT found: %s" % scrapyd_logs_dir)
        else:
            print(">>> Using scrapyd_logs_dir: %s" % scrapyd_logs_dir)

    if args['DELETE_CACHE']:
        if os.path.isdir(CACHE_PATH):
            shutil.rmtree(CACHE_PATH, ignore_errors=True)
            print(">>> Cache utf8 and stats files deleted")
        else:
            print("!!! Cache dir NOT found: %s" % CACHE_PATH)

def update_app_config(config, args):
    # scrapyd_server would be None if -ss not passed in
    if not args['SCRAPYD_SERVER']:
        args['SCRAPYD_SERVER']= config.get('SCRAPYD_SERVER') or '127.0.0.1:6800'

    config.update(dict(
        SCRAPYD_SERVER=args['SCRAPYD_SERVER'],
        SCRAPYD_LOGS_DIR=args['SCRAPYD_LOGS_DIR'],
    ))

    # action='store_true': default False
    if args['DISABLE_CACHE']:
        config['DISABLE_CACHE'] = True
    if args['DELETE_CACHE']:
        config['DELETE_CACHE'] = True
    if args['DEBUG']:
        config['DEBUG'] = True


if __name__ == "__main__":
    main()