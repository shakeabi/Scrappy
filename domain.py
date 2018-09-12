from urllib.request import urlparse

def get_domain_name(url):
	try:
		results = get_sub_domain_name(url).split('.')
		if results[-1] in ('com', 'net', 'org'):
			returnData = results[-2] + '.' + results[-1]
		else:
			returnData = results[-3] + '.' + results[-2] + '.' + results[-1]
		return returnData
	except:
		return ''

def get_sub_domain_name(url):
	try:
		return urlparse(url).netloc
	except: 
		return ''