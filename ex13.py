from sys import argv
# an import to add an argv modules (aka libraries) to your script.
#argv is an argument variable, which holds the arguments you pass to your python script when you run in

script, first, second, third = argv
#takes what's in argv, unpacks it and assigns it to these variables in order

#just printing as usual
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third