import sys

#Expand Python classes path with your app's path
sys.path.insert(0,"F:/ApacheDirectory/base/wsgi")

from spider_only.run import main
application = main()

