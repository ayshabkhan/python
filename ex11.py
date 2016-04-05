print "How old are you?", # commas at end so print doesn't end line with a newline character /n and go to the next line
age = raw_input() # presents a prompt to the user and gets input
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

 print "So you're %r old, %r tall and %r heavy." % (age, height, weight)
# formats the string to return data the user input