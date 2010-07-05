'''
Created on Jul 3, 2010

@author: Zachary Witte (zacwitte@gmail.com)
'''

import urllib2
import logging
import json
from time import sleep
from Queue import Queue
from threading import Thread

class PyFlickrStreamr(object):
    baseurl = 'http://api.flickr.com/services/rest/?method=flickr.photos.getRecent&format=json&nojsoncallback=1'
    url = baseurl
    q = Queue()
    apikey = None
    extras = set(['date_upload'])
    last_id = 0
    thread = None
    sleeptime = 2
    per_page=100
    stop = False
    
    def __init__(self, apikey, extras=None, sleeptime=2, per_page=100):
        self.apikey = apikey
        if extras:
            self.extras.update(set(extras))
        self.sleeptime = sleeptime
        self.per_page = per_page
        self.url += '&api_key='+apikey+"&per_page="+str(per_page)+'&extras='+','.join(self.extras)
        self.url += '&page='+str(1000/per_page) #get the last page (most recent)
        self.thread = Thread(target=self.getter)
        self.thread.start()
    
    def __del__(self):
        self.stop = True
        self.thread.join()
    
    def getter(self):
        while not self.stop:
            self.request_next()
            sleep(self.sleeptime)
    
    def request_next(self):
        logging.debug("Requesting URL:    "+self.url)
        req = urllib2.urlopen(self.url)
        data = req.read()
        req.close()
        jsondata = json.loads(data)
        added=0
        if jsondata['stat'] != 'ok':
            raise Exception("API Error: "+str(jsondata))
        
        for item in jsondata['photos']['photo']:
            if item['id'] <= self.last_id:
                continue
            self.last_id = item['id']
            self.q.put(item)
            added += 1
        
        if added == self.per_page:
            logging.warning("PyFlickrStreamr may have missed one or more items in between API calls. Try decreasing the sleeptime paramater or increasing the per_page parameter")
    
    def __iter__(self):
        return self
    
    def next(self):
        n = self.q.get()
        self.q.task_done()
        return n

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    fs = PyFlickrStreamr('your_api_key_here', extras=['date_upload','url_m'])
    for row in fs:
        print str(row['id'])+"   "+row['url_m']
    