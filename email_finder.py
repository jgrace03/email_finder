#############################################################
#                         Julia Grace                       #
#                       email_finder.py                     #
#                                                           #
#          scrape all email addresses from a website        #
#                                                           #
#############################################################

import sys
import requests  
from BeautifulSoup import BeautifulSoup
import re
import urllib2

website = sys.argv[1]

q = []

if "http://" not in website:
	q.append("http://%s" %(website))
else:
	q.append(website)

req = urllib2.Request(q[0])
res = urllib2.urlopen(req)
finalurl = res.geturl()

domain = finalurl.split("//")[-1].split("/")[0]

alllinks = []
alllinks.append(q[0])
emails = []

while len(q) > 0:

	responce = requests.get(q[0])
	html = responce.content
	soup = BeautifulSoup(html)
	q.remove(q[0])

	#scrape for other web pages
	for link in soup.findAll('a'):
		link = link.get('href')
				
		if link:
			if (link.split("//www.")[-1].split("/")[0] == domain
				or link.split("//")[-1].split("/")[0] == domain):
				if link[0] != 'h':
					link = "http:%s" %(link)
				if link not in alllinks:
					q.append(link)
					alllinks.append(link)

	#scrape for emails
	match = re.findall(r'[\w\.-]+@[\w\.-]+', html)

	for m in match:
		if m not in emails and '.' in m:
			if m[len(m)-1] == '.':
				m = m[:-1]
			emails.append(m)
			print m




