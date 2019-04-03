import sys

#Expand Python classes path with your app's path
sys.path.insert(0,"D:/ApacheDirectory/base/wsgi")

from spider_only.run import main
main()

from flask import current_app as application