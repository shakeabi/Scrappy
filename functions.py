#Require output stream
import os

#Create a new project for every website you crawl..
def create_project_dir(directory):
	if not os.path.exists(directory):
		print('Creating project' + directory)
		os.makedirs(directory)

#Create queue and crawled files..
def create_data_files(baseURL, projectName):
		queue = projectName + '/queue.txt'
		crawled = projectName + '/crawled.txt'
		if not os.path.isfile(queue):
			write_file(queue, baseURL)
		if not os.path.isfile(crawled):
			write_file(crawled, '')

#Create a new file
def write_file(path, data):
		f = open(path, 'w')
		f.write(data)
		f.close()
			
#Append data
def append_file(path, data):
		f = open(path, 'a')
		f.write(data+'\n')
		f.close()

#Delete data
def delete_file(path):
		f = open(path, 'w')
		f.write('')
		f.close()

#Add stuff to set-unique
def file_to_set(fileName):
		returnData = set()
		with open(fileName, 'rt') as f:
			for line in f:
				returnData.add(line.replace('\n',''))
		return returnData

#Take the set with unique elements and replace the file
def set_to_file(links, file):
		delete_file(file)
		for link in sorted(links):
				append_file(file, link)