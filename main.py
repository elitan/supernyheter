import urllib2
import re
from BeautifulSoup import BeautifulSoup

urls = ['http://aftonbladet.se', 'http://www.svd.se', 'http://dn.se', 'http://svt.se/nyheter', 'http://www.tv4.se/nyheterna', 'http://idg.se']


for url in urls:
	soup = BeautifulSoup(urllib2.urlopen(url).read().lower())
	print(url)
	print(len(soup.body.findAll(text=re.compile('super'))))
	