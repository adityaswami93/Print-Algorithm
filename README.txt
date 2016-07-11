Printing Algorithm

Overview of Algorithm
The Algorithm grabs all the data from the input file and processes it line by line. The tabs in the line are replaced by 4 spaces. It checks whether the lines exceeds the page width and if not, then the line is written as it is. If it does, then a function is called that breaks the line into lines of smaller widths to fit into page width. In this function, the line checks at the end of page width whether there is a space and keeps on going backwards from that point until a space is encountered. Then the line is written to the output file from start until the last space encountered with spaces at the end and beginning removed. The processes repeated until the all parts of line are broken down and written to the file. Meanwhile, the algorithm also check whether the line has exceeded the page height and it calls a function to print equal signs if it does. 

Instructions for running the Algorithm.

1) To run the algorithm, call the function print_algo in python in the following manner - 
python printAlgo.py -i <inputfilename> -o <outputfilename> -p <pageSize>
where -i represents the input file name, -o the output file name and -p represents the page size. You can also indicate the directory for the input and output file directry from the position where printAlgo.py is stored.

For example - python printAlgo.py -i print_input/0.in  -o test.txt -p A4

