#My_First_Project
import os
import requets
from bs4 import BeautifulSoup

#https://play.typeracer.com

'''creating new directory
assigning each directory to a new website/webpage'''

def new_directories(new_directory):
	if not.os.path.exixts(new_directory):
		os.mkdir(new_directory)
		
#queue is nothing but a waiting list of the links on the main webpage.

def data_files(project, url) :
	queue = project + '/queue.txt'
	crawled = project + '/crawled.txt'
	if not os.path.isfile(queue):
		write_file(queue, url)
	if not os.path.isfile(crawled):
		write_file(crawled, url)

def write_file(path, data):
	f = open(path, 'w')
	f.write(data)
	f.close()

def addtofile(path,data):
	f = open(path, 'w')
	f.write(data + '\n')

def deletecontents(path):
	f = open(path, 'w')
	f.close()



