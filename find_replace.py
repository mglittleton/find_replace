# imports
import sys

# initial variables
count = 0
file = sys.argv[1] # filename, first argument
find = sys.argv[2] # search string, second argument
replace = sys.argv[3] # replacement string, third argument

# data manipulation
text = ''
with open(file, 'r') as rf: # open the file and read it as a list 'lines'
  lines = rf.readlines()
for line in lines: # convert the list into a single text string
  text += line

# basic logic
for i in range(0, len(text) - len(find) + 1): # moving one character at a time, look at potential matches
  search_str = text[i:i+len(find)]
  if (search_str == find): # if match found, break text into three pieces (not incl search string), then combine them with the replacement string
    text1 = text[0:i]
    text2 = text[i + len(search_str):len(text)]
    text = ''.join([text1, replace, text2])
    count += 1

# output
with open(file, 'w') as wf:
  wf.write(text)

print("Num of found instances:", count) # need to output num of finds and num of replace, but should be the same (?)
print("Num of replaced instances:", count)


"""
Things to consider:
very short files, less than the length of the search string - checked
search strings wrapping lines - obv. doesn't work, but should it? edge cases not listed
should search strings be case-dependent
search string at end of file - checked
search string at beginning of file - checked
"""
