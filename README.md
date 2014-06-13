pythonthehardway
================

Working files from Python the Hard Way tutorial for julython (http://www.julython.org/).

```python
from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

print txt.close()
print txt_again.close()
```
