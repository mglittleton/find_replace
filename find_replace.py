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
  search_str = text[i:i+len(find)]
  if (search_str == find):
    text1 = text[0:i]
    text2 = text[i + len(search_str):len(text)]
    print (text1)
    print (text2)

# output