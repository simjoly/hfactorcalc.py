#! /usr/bin/env python3

#--------------------------------------------------
#
# h-factor calculator
#
# Copyright (c) 2014, Simon Joly
# All rights reserved.
#
# credits: uses scholar.py (github.com/ckreibich)
#
#--------------------------------------------------


# Import modules
import csv
import os
import argparse
import time
import sys
import random
import datetime

# Parser
parser = argparse.ArgumentParser(description='Calculare h-factor from a list of publications.')
parser.add_argument("-t","--timelag", dest='timelag', default=10, help="Maximum time delay (sec) between two queries to Google Scholar. The exact time is estimated with a random number generator.")
parser.add_argument("filename", type=str, help='name of the file containning the publications')
parser.add_argument("-q", "--quiet", help="quiet mode", action="store_true")
args = parser.parse_args()

# Global variables
currentyear = datetime.date.today().year
thetitles = []
thecitations = []
thecitations5y = []
statusbarlength = 20

# Instantiations
random.seed();

# Main script
with open(args.filename, encoding='utf-8', newline='') as csvfile:
	titles = csv.reader(csvfile, delimiter='|', quotechar='\'', quoting=csv.QUOTE_NONE)
	if args.quiet:
		print("")
		print(' Searching [',end="")
		print(' '*statusbarlength,end="")
		print(']',end="",)
		print('\b'*(statusbarlength+1),end="",flush=True)
		steps = float(len(list(csv.reader(open(args.filename))))/statusbarlength)
		i=1
		j=1
	for row in titles:
		n = random.random()*args.timelag;
		time.sleep(n); 
		if not args.quiet:
			print(row[0])
		thetitles.append(row[0])

		# Extract citations for each publication
		os.system("python scholar.py -A \"" + row[0] + "\" -c 1 --csv > temp.csv")
		with open('temp.csv', encoding='utf-8', newline='') as csvfile:
			citations = csv.reader(csvfile, delimiter='|', quotechar='\'', quoting=csv.QUOTE_NONE)
			for cit in citations:
				if not args.quiet:
					print(" -> citations: " + cit[3])
				thecitations.append(int(cit[3]))

		# Extract citations within the last five years
		n = random.random()*args.timelag;
		time.sleep(n);
		os.system("python scholar.py -A \"" + row[0] + "\" -c 1 --after=" + str(currentyear-5) + " --csv > temp.csv")
		with open('temp.csv', encoding='utf-8', newline='') as csvfile:
			citations = csv.reader(csvfile, delimiter='|', quotechar='\'', quoting=csv.QUOTE_NONE)
			for cit in citations:
				if not args.quiet:
					print(" -> citations (5y): " + cit[3])
				thecitations5y.append(int(cit[3]))
		if args.quiet:
			if int(i/steps) == j:
				print('.',end="",flush=True)
				j=j+1
			i=i+1
if args.quiet:
	print(']  Done!')
os.system("rm temp.csv")
thecitations.sort(reverse=True)

# Calculate the h-factor
hfactor=[]
i=1
for num in thecitations:
	if i > num:
		hfactor=i-1
		break
	else:
		i=i+1

# Calculate 5 years h-factor
thecitations5y.sort(reverse=True)
hfactor5y=[]
i=1
for num in thecitations5y:
	if i > num:
		hfactor5y=i-1
		break
	else:
		i=i+1

# Output results
print("\n Number of titles: " + str(len(thecitations)))
print(" h-factor: " + str(hfactor))
print(" 5 years h-factor: " + str(hfactor5y) + "\n")


