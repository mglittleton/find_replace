First instinct basic code (not legit code):

text_of_file = (input file's text as a string)
search_string = (input search string)
repl_string = (input repl_string)
count = 0

search_chars = ['char1', 'char2', 'char3'...] #list of characters, in order, of search string

if len(text_of_file) < len(search_string):
  skip to the end and return 0

for char in text_of_file: #stopping search_chars.len short of the end
  if char == search_chars[0]:
    look at the next char and compare to search_chars[1] and so on
    if matching text string found:
      count += 1
      cut text_of_file and strip out search_string
      add in repl_string

save the new text_of_file

print(count, count) #output of found search parameters should equal exactly the replacement occurrences
