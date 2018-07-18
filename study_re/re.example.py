# coding=utf-8
import re
import urlparse
import urllib2
from bs4 import BeautifulSoup

url = 'http://www.imooc.com/course/list'
url1 = 'http://www.netbian.com/s/liuyifei/'

response = urllib2.urlopen(url1)
buf = response.read()
soup = BeautifulSoup(buf, 'html.parser', from_encoding='utf-8')
# links = soup.find_all('img', src=re.compile(r'//img.+\.jpg'))
links = soup.find_all('img', src=re.compile(r'^http://.+\.jpg$'))
urls = []
for link in links:
    url = link['src']
    urls.append(url)
print urls
full_urls = [urlparse.urljoin('http:', url) for url in urls]
print full_urls
i = 1
for full_url in full_urls:
    with open(str(i) + '.jpg', 'wb') as f:
        response = urllib2.urlopen(full_url)
        buf = response.read()
        f.write(buf)
        i += 1
