#!/usr/bin/python
#Author: Aditya Swami

import sys, getopt

#define all the constansts needed
char_height = 3;
char_width = 2;

A4_height = 297
A4_width = 210

A3_width = 297
A3_height = 420
tab_replacer = '    '
height_ctr = 0

def print_algo(infilename,outfilename, page_size):
	height_ctr = 0														#counter for calculating the page height

	if page_size == 'A3':
		max_width = A3_width
		max_height = A3_height

	if page_size == 'A4':
		max_width = A4_width
		max_height = A4_height


	outfile  = open(outfilename,'w');

	with open(infilename) as f:
		data = f.readlines()

		for line in data:
			print 'printing in progress'								#to indicate that printing in progress
			line = line.strip()											#remove the spaces at the end
			line = line.replace("	", tab_replacer)					#replace the tab with 4 spaces
			line_len =  len(line)
			total_char_len = line_len * char_width						# to check if the line width to print is greater than the page width. 
																		#If it is, then a separate functon is called which breaks the line into smaller widths to fit inside the page.
			if total_char_len > max_width:
				lines_list = create_print_line(line,max_width)			#the functions will return a list with smaller lines to print
				for lines in lines_list:
					lines = lines.strip()
					outfile.write(lines)
					outfile.write('\n')		
					height_ctr += char_height
					if height_ctr >= max_height:						#check if the content of the page exceeds page heights and call a function to print equal signs
						add_page_break(outfile,max_width)
						height_ctr = 0	
			else:														#it is called when the line width is smaller than page width
				outfile.write(line)
				if line_len > 0:										#to account for the case when the line is empty
					outfile.write('\n')
					height_ctr += char_height
					if height_ctr >= max_height:
						add_page_break(outfile,max_width)
						height_ctr = 0	

#function to add equal signs at the end of page
def add_page_break(outfile,max_width):
	equal_sign = '=' * (max_width/char_width)
	outfile.write(equal_sign)
	outfile.write('\n')

#function to break the a line into multiple line for printing when its width is higher than page's width
#the logic in the functions is that it begins looking at the point 'max_width/char_width' plus an extra space and looks backwards untill a space is encountered. 
#This is to ensure thats words are not broken up across two lines
def create_print_line(line,max_width):
	line_to_print = []
	line_len = len(line)
	start = 0
	ctr = max_width/char_width											#counter to keep track of characters in line		
	while ctr<line_len:
		if line[ctr].isspace() == True:
			tmp_line = line[start:ctr+1]
			tmp_line = tmp_line.strip()									#remove the extra space at the end
			start = ctr + 1												#establish the starting point for the next round
			line_to_print.append(tmp_line)
			ctr += max_width/char_width									#ctr advances by the max_width/char_width amount
		else:
			ctr -= 1
	else:																#this is called when the characters left in the line are less than max_width/char_width and so it gets the last remaining characters 
		tmp_line = line[start:]											
		tmp_line = tmp_line.strip()
		line_to_print.append(tmp_line)

	return line_to_print

def usage():
	print """python printAlgo.py -i <inputfilename> -o <outputfilename> -p <pageSize>"""


if __name__ == '__main__':
	inputfilename = outputfilename = pageSize = None
	try:
		options, other_args = getopt.getopt(sys.argv[1:], 'i:o:p:')
	except getopt.GetoptError, err:
		usage()
		sys.exit(2)

	for opt, arg in options:
		if opt == '-i':
			inputfilename = arg
		elif opt == '-o':
			outputfilename = arg
		elif opt == '-p':
			pageSize = arg
		else:
			assert False, "unhandled option"


	if inputfilename is None or outputfilename is None or pageSize is None:
		usage()
		sys.exit(2)

	print_algo(inputfilename,outputfilename,pageSize)





