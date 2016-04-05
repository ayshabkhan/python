from sys import argv

script, filename = argv
# defining user input into command line (ex15.py, ex15_sample.txt)

txt = open(filename)
# tells python to open up the ex15_sample.txt files

print "Here's your file %r:" % filename

print txt.read() # call read function on txt file

# ^ uses argv to get a file name
# v uses raw_input to get a file name

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()