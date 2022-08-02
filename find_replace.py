# imports
import sys
import fileinput

# initial variables
count = 0
gen_file_obj = fileinput.input(files = sys.argv[1])
text=''

# data manipulation
for line in gen_file_obj:
  text += line

# basic logic

# output
print (text)