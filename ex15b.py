filename = raw_input("What's the file name?")

txt = open(filename)

print "Here's your file %s:" % filename
print txt.read()
