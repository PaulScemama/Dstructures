import sys # for sys.argv, the command-line arguments
from Stack import Stack

def delimiter_check(filename):
  a = Stack()   #create stack object
  open_delimeters = ['[', '{', '(']           #create open delimeters list
  closing_delimeters = [']', '}', ')']        #create closing delimeters list
  with open(filename, 'r', encoding = 'UTF8') as file: #open file
    text = file.read()      #read file into text
    for item in text:       #for character in text
      #print(item)
      if item in open_delimeters:   #if character is an open delimiter
        #print(item, 'this should be open delim')
        a.push(item)      #push that item onto the stack
      elif item in closing_delimeters:    #if character is a closing delimiter
        if len(a) == 0:         #a closing delimiter could never come first if it's balance so if the stack is empty
          return False        #return false
        b = a.pop()         #else, pop element from stack
        #print(b, item)        
        if open_delimeters.index(b) != closing_delimeters.index(item):      #since lists correpond with index, if index of the first is not the index of the second
          return False        #return false
    if len(a) == 0:     #if the stack is emptied out
      return True       #return true
    return False        #else, return false 




      
  # TODO replace pass with an implementation that returns True
  # if the delimiters (), [], and {} are balanced and False otherwise.


if __name__ == '__main__':
  # The list sys.argv contains everything the user typed on the command 
  # line after the word python. For example, if the user types
  # python Delimiter_Check.py file_to_check.py
  # then printing the contents of sys.argv shows
  # ['Delimiter_Check.py', 'file_to_check.py']
  if len(sys.argv) < 2:
    # This means the user did not provide the filename to check.
    # Show the correct usage.
    print('Usage: python Delimiter_Check.py file_to_check.py')
  else:
    if delimiter_check(sys.argv[1]):
      print('The file contains balanced delimiters.')
    else:
      print('The file contains IMBALANCED DELIMITERS.')


