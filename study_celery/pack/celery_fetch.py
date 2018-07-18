import urllib2
from celery_config import app

@app.task
def fetch_url(url):
	resp = urllib2.urlopen(url)
        print resp.getcode() 

def func(urls):
     for url in urls:
       fetch_url.delay(url)
