# imports
import sys
import fileinput

# initial variables
count = 0
gen_file_obj = fileinput.input(files = sys.argv[1])
text=''
find = sys.argv[2]
replace = sys.argv[3]

# data manipulation
for line in gen_file_obj:
  text += line

# basic logic
for i in range(0, len(text) - len(find) + 1):
  print(text[i:i+len(find)])

# output
