#############################################################
#				         Julia Grace						#
#					   email_finder.py					    #
#															#
#           scrape all email addresses from a website       #
#															#
#############################################################

import sys
import requests  
from BeautifulSoup import BeautifulSoup
import re

website = sys.argv[1]
q = []
q.append("http://www.%s" %(website))
alllinks = []
alllinks.append(q[0])
emails = []

while len(q) > 0:

	#check that address is valid
	while "//" not in q[0]:
		q.remove(q[0])
		if len(q) == 0:
			break

	if len(q) == 0:
		break

	responce = requests.get(q[0])
	html = responce.content
	soup = BeautifulSoup(html)
	q.remove(q[0])

	#scrape for other web pages
	for link in soup.findAll('a'):
		link = link.get('href')
		
		if link:
			if website in link and '%' not in link and 'pdf' not in link:
				if link[0] != 'h':
					link = "http:%s" %(link)
				if link not in alllinks:
					q.append(link)
					alllinks.append(link)

	#scrape for emails
	match = re.findall(r'[\w\.-]+@[\w\.-]+', html)

	for m in match:
		if m not in emails and m[len(m)-1] != '.' and '.' in m:
			emails.append(m)
			print m




