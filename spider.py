from urllib.request import urlopen
from linkfinder import LinkFinder
from functions import *

class Spider:

	#Static vars
	project_name = ''
	base_url = ''
	domain_name = ''
	queue_file = ''
	crawled_file = ''

	#Work with vars and save it in files for later 
	queue = set()
	crawled = set()

	def __init__(self, project_name, base_url, domain_name):
		Spider.project_name = project_name
		Spider.base_url = base_url
		Spider.domain_name = domain_name
		Spider.queue_file = project_name+'/queue.txt'
		Spider.crawled_file = project_name+'/crawled.txt'
		self.initialise()
		self.crawl_page('fs', Spider.base_url)

	@staticmethod
	def initialise():
		create_project_dir(Spider.project_name)
		create_data_files(Spider.base_url, Spider.project_name)
		Spider.queue = file_to_set(Spider.queue_file)
		Spider.crawled = file_to_set(Spider.crawled_file)

	@staticmethod
	def crawl_page(thread_name, page_url):
		if page_url not in Spider.crawled:
			print(thread_name + 'now working on ' + page_url)
			print('Queue:' + str(len(Spider.queue)) + '|' + 'Crawled:'+ str(len(Spider.crawled)))
			Spider.add_links_to_queue(Spider.gather_links(page_url))
			Spider.queue.remove(page_url)
			Spider.crawled.add(page_url)
			Spider.update_files()

	@staticmethod
	def gather_links(page_url):
		html_readable = ''
		try:
			response = urlopen(page_url)
			print(response)
			if response.getheader('Content-Type') == 'text/html':
				html_binary = response.read()
				html_readable = html_binary.decode('utf-8')
			finder = LinkFinder(Spider.base_url, page_url)
			finder.feed(html_readable)
		except Exception as e:
			print('Cannot crawl this page' + page_url)
			return set()

		return finder.return_page_links()

	@staticmethod
	def add_links_to_queue(links):
		for url in links:
			if url in Spider.queue or url in Spider.crawled:
				continue
			#Just to not screwup my laptops
			if Spider.domain_name not in url:
				continue

			Spider.queue.add(url)

	@staticmethod
	def update_files():
		set_to_file(Spider.queue, Spider.queue_file)
		set_to_file(Spider.crawled, Spider.crawled_file)