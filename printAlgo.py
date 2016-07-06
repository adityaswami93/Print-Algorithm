#!/usr/bin/python

import sys, getopt

char_height = 3;
char_width = 2;

A4_height = 297
A4_width = 210

A3_width = 297
A3_height = 420

def print_algo(infilename,outfilename, page_size):
	i = 0
	starting_space_removed = False
	width_ctr = 0
	height_ctr = 0

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
			i = i + 1
			line = line.strip()
			#words = line.split();
			#print line[0]
			#for letter in line:
				#if letter == ' ' and !starting_space_removed:
			line_len = len(line)
			total_char_len = line_len * char_width

			if total_char_len > max_width:
				lines_list = create_print_line(line,max_width)
				for lines in lines_list:
					outfile.write(lines)
					outfile.write('\n')	
			else:
				outfile.write(line)
				if line_len > 0:
					outfile.write('\n')

			height_ctr += char_height
			if height_ctr >= max_height:
				equal_sign = '=' * (max_width/char_width)
				outfile.write(equal_sign)
				outfile.write('\n')
				height_ctr = 0


def create_print_line(line,max_width):
	line_to_print = []
	line_len = len(line)
	start = 0
	ctr = max_width/char_width - 1

	while ctr<line_len:
		if line[ctr] != ' ':
			ctr -= 1
		else:
			tmp_line = line[start:ctr]
			print tmp_line
			tmp_line.split()
			start = ctr + 1
			line_to_print.append(tmp_line)
			ctr += max_width/char_width
	else:
		tmp_line = line[start:]
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

		print "1yes"


	if inputfilename is None or outputfilename is None or pageSize is None:
		usage()
		sys.exit(2)

	print "yes"

	print_algo(inputfilename,outputfilename,pageSize)





