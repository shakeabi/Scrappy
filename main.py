#Web Crawler

import threading
from queue import Queue
from spider import Spider
from functions import *
from domain import *

PROJECT_NAME = 'fast'
BASE_URL = 'http://www.fast.com' 
DOMAIN_NAME = get_domain_name(BASE_URL)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NO_OF_THREADS = 8

queue = Queue()
Spider(PROJECT_NAME, BASE_URL, DOMAIN_NAME)

def create_jobs():
	for link in file_to_set(QUEUE_FILE):
		queue.put(link)
	queue.join()
	crawl()

def create_spiders():
	for _ in range(NO_OF_THREADS):
		t = threading.Thread(target=job)
		t.daemon=True
		t.start()

def job():
	while True:
		url = queue.get()
		Spider.crawl_page(threading.current_thread().name, url)
		queue.task_done()

# Main
def crawl():
	print('CRAWL: WORKS!!')
	queued_links = file_to_set(QUEUE_FILE)
	if len(queued_links) > 0:
		print(str(queued_links)+ ' links in queue')
		create_jobs()


create_spiders()
crawl()