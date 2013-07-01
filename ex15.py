# Import argv
from sys import argv

# Unpacks the argv arguments; 
# sys.argv[0] is always the name of the script
# filename is sys.argv[1]
script, filename = argv

# Open the file specified in the command ("filename" variable)
# Why does it need a name assignment on the left side of the equals sign?
# So that we can reference it later to do more stuff with it, like read the file
txt = open(filename)

# Print this string and fill in with value of variable "filename"
print "Here's your file %r:" % filename
# Read the file that's assigned to "txt"
print txt.read()

# Print this string
print "Type the filename again:"
# Grab user input (preceeded by ">",  and assign it to "file_input"
file_again = raw_input("> ")

# Open file specified by user in file_again input
txt_again = open(file_again)

# Read the file_again file that was opened above and assigned to txt_again
print txt_again.read()
