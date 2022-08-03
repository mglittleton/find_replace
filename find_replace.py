# imports
import sys

# initial variables
count = 0
file = sys.argv[1]
find = sys.argv[2]
replace = sys.argv[3]

# data manipulation
gen_file = open(file, 'r+')
text = gen_file.read()

# basic logic
for i in range(0, len(text) - len(find) + 1):
  search_str = text[i:i+len(find)]
  if (search_str == find):
    text1 = text[0:i]
    text2 = text[i + len(search_str):len(text)]
    text = ''.join([text1, replace, text2])
    count += 1

# output
with open(file, "r") as fp:
  lines = fp.readlines()
  for line in lines:
    print (line)
# gen_file.write(text)
print(count)
gen_file.close()