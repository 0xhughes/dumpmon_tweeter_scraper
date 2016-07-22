import urllib2
import time
import os
import datetime
import sys
from random import randint

def menu():
	sane = 1
	while sane == 1:
		print "[ - ] Please enter absolute path to output directory: "
		in_path = raw_input()+"\\tweeter_scraper_out"
		if os.path.exists(in_path):
			sane = 0
		else:
			try:
				os.mkdir(in_path)
				sane = 0
			except:
				os.system('cls' if os.name == 'nt' else 'clear')
				print "[ - ] Invalid path, try again."
	return(in_path)

def main(in_path):
	print "[ + ] Gathering information..."
	in_path = in_path
	target_list = []
	done_list = []
	cnt = 0
	
	while True:
		if cnt != 0:
			rand = randint(5,180)
			print "[ - ] Sleeping "+str(rand)+" seconds until check for new items."
			time.sleep(rand)
		try:
			resp = urllib2.urlopen("https://twitter.com/dumpmon")
		except:
			tmp_t = randint(360,720)
			time.sleep(tmp_t)
			print "[ - ] Communication error, sleeping "+str(tmp_t)+" seconds..."
		html = resp.readlines()
		out_log = in_path+"\\out_log.txt"
		out_log_fo = open(out_log, 'a+')
		out_log_items = out_log_fo.readlines()
		
		for done in out_log_items:
			if done.strip() not in done_list:
				done_list.append(done.strip())

		for line in html:
			if "data-expanded-url=" in line:
				startCut = line.find('data-expanded-url=')+18
				endCut = line[startCut:len(line)].find(' class=')+startCut
				target = line[startCut+1:endCut-1]
				target_list.append(target)

		for targ in target_list:
			if targ not in done_list:
				try:
					time.sleep(randint(1,15))
					resp = urllib2.urlopen(targ)
				except urllib2.HTTPError:
					print "[ - ] 404, "+targ+", skipping, "+str(time.strftime("%m%d%y_%H%M%S"))
					out_log_fo.write(targ+"\n")
					continue
				html = resp.read()
				if html.strip() == "Please refresh the page to continue...":
					resp = urllib2.urlopen("http://pastebin.com/"+targ[targ.rfind("=")+1:len(targ)])
					html = resp.read()
					start_raw_cut = html.find('<textarea id="paste_code" class="paste_code" name="paste_code" onkeydown="return catchTab(this,event)">')+103
					end_raw_cut = html[start_raw_cut:len(html)].find('</textarea>')+start_raw_cut
					html = html[start_raw_cut:end_raw_cut]
				time_det = str(time.strftime("%m%d%y_%H%M%S"))
				dump_file = in_path+"\\"+time_det+'.txt'
				dump_file_fo = open(dump_file, 'w')
				dump_file_fo.write(html)
				dump_file_fo.close()
				done_list.append(targ)
				out_log_fo.write(targ+"\n")
				print "[ + ] Dump "+targ+" grabbed @ "+str(time.strftime("%m%d%y_%H%M%S"))
		out_log_fo.close()
		cnt+=1
		print "[ - ] Checked "+str(cnt)+" times."
	
	out_log_fo.close()
			
try:
	main(menu())
except KeyboardInterrupt:
	print "[ - ] Interrupt caught, exiting."
	sys.exit(0)
