#Program to pull movie data from Github
#Pat Carroll 

import codecs
import re
import urllib2
import json
import time
import datetime
import sys
from collections import Counter
from datetime import datetime
from collections import Counter

reload(sys) 
sys.setdefaultencoding( "utf-8" )

open('d3_info.txt', 'w').close()
open('raw_json.txt', 'w').close()

#User inputs query and api key
api_key = '96555ebfd4f2d41ea630eb9a974a7109'
query = 'life'
first_date=[]
page = 1
result = []
current_time = time.strftime('%c')
print current_time
commit = []
difference = 0


while difference < 365:
	url = 'https://api.github.com/repos/mbostock/d3/commits'
	final_url = url + "?page=" + str(page)
	json_obj = urllib2.urlopen(final_url)
	data = json.load(json_obj)
	with open('raw_json.txt', 'a') as file:
		file.write(str(data))
	for item in data:
		commit = datetime.strptime(item['commit']['author']['date'], "%Y-%m-%dT%H:%M:%SZ")
		commit = commit.strftime('%c')
		difference = (datetime.strptime(current_time, '%c') - datetime.strptime(commit, '%c')).days
		if difference < 365:
			with open('d3_info.txt', 'a') as file:
				file.write(str(commit) + '\n')
	page = page + 1
	time.sleep(1.0)

week_number = []
day_number = []
with open('d3_info.txt') as myfile:
	count = sum(1 for line in myfile)
	

f = open( "d3_info.txt", "r" )
a = []
weeks = []
for line in f:
	a = time.strptime(line.strip('\n'),"%c")
	weeks = time.strftime("%U", a)
	days = time.strftime('%A', a)
	week_number.append(weeks)
	day_number.append(days)

w = Counter(week_number)
d = Counter(day_number)

print 'The total number of commits in the last year is: ' + str(count)
print 'The week with the most commits in the last year was: ' + str(w.most_common(1))
print 'The day of the week with the most commits is: ' + str(d.most_common(1))

