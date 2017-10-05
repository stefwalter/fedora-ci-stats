#!/usr/bin/env python

# Purpose: publish output of ./test-stats to Fedora Wiki. This script is
# scheduled on Centos OpenShift: apps.ci.centos.org. Dependency are installed
# as a part of Job definition. data.txt comes from ./test-stats output.

import mwclient
import os

ua = 'MyWikiTool/0.2 run by User:FedoraUser'
site = mwclient.Site('fedoraproject.org', clients_useragent=ua)
site.login(os.environ.get('WIKI_USER'), os.environ.get('WIKI_PASS'))
page = site.pages['CI/Tests/stat']
page.exists
with open('data.txt', 'r') as myfile:
    text = myfile.read()
page.save(text, 'Current status.')
