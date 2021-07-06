class Linked_List:
  
  class __Node:
    
    def __init__(self, val):
      self.value = val  #should this be private or public? #the instance of Node called has a value that's passed in as 'val'
      self.next = None  #initialize next as None
      self.previous = None  #initialize previous as None
      
      

  def __init__(self):
    self.__header = Linked_List.__Node(None)   #create a node for header with no value
    self.__trailer = Linked_List.__Node(None)  # create a node for trailer with no value
    self.__header.next = self.__trailer         # header.next points to trailer
    self.__trailer.previous = self.__header     # trailer.previous points to header
    self.__size = 0                            #Initialize size to 0 
    
    

  def __len__(self):
    return self.__size

  
  def __iter__(self):
    # Somebody is about to iterate through the set.
    # initialize an index to begin.
    self.__current = self.__header.next #tried emulating set.py???
    return self
  
  def __next__(self):
    if self.__current is self.__trailer:
      raise StopIteration
    to_return = self.__current.value        #retrieve value at node you are at
    self.__current = self.__current.next           #set yourself up for the next cycle by going next
    return to_return                 #return value 

  def append_element(self, val):
    to_append = Linked_List.__Node(val)            #create Node to append
    to_append.next = self.__trailer                 #point Node to append to trailer
    self.__trailer.previous.next = to_append     #point preceding node to trailer to the new node
    to_append.previous = self.__trailer.previous #point to_append previous to the node before trailer
    self.__trailer.previous = to_append          #point trailer's previous to append object
    self.__size += 1                             #increase size by 1
  
  
  def insert_element_at(self, val, index):
    if index > self.__size - 1 or index < 0:
      raise IndexError 
    to_insert = Linked_List.__Node(val)
    if index < self.__size // 2:                 #deciding to start for loop from header or trailer
      current = self.__header                    #start at header
      for i in range(index):                    #for loop to walk along nodes
        current = current.next
      to_insert.next = current.next             #insertion process
      current.next = to_insert
      current.next.previous = to_insert
      to_insert.previous = current
      self.__size += 1                           #add 1 to size
    else:                                       #deciding to start for loop from header or trailer
      current = self.__trailer                   #start at trailer
      for i in range(self.__size - index):       #for loop to walk along nodes
        current = current.previous
      to_insert.next = current                  #insertion process
      current.previous.next = to_insert
      to_insert.previous = current.previous
      current.previous = to_insert
      self.__size +=1                            #add 1 to size 
  
  def remove_element_at(self, index):
    if index > self.__size - 1 or index < 0: #if index invalid, raise Index Error
      raise IndexError
    else:
      if index < self.__size // 2:          #if index is in the first half of the LL
        current = self.__header             #start at header
        for i in range(index):              #current walk to node before the node of the index passed in 
          current = current.next
        to_return = current.next.value     #save value you're going to remove to return later
        current.next = current.next.next   #unlink
        current.next.previous = current    
        self.__size -= 1                   #subtract 1 from size
        return to_return                   #return value of the node being removed
      else:                                #if index is in the second half or at the exact middle
        current = self.__trailer           #start at trailer
        for i in range(self.__size - (index+1)):    #current walk to the node after the node of the index passed in 
          current = current.previous
        to_return = current.previous.value  #save value you're going to remove to return later
        current.previous = current.previous.previous #unlink
        current.previous.next = current
        self.__size -= 1                    #subtract 1 from size
        return to_return                    #return value of the node being removed
  
  def get_element_at(self, index):
    if index > self.__size - 1 or index < 0:      #check if index is valid
      raise IndexError
    else:
      if index < self.__size // 2:            #if index is in the first half of the LL
        current = self.__header               #start at header
        for i in range(index+1):              #current walk to the node at the index passed in
          current = current.next
        return current.value                  #return value of the node at the index passed in 
      else:                                   #if index is in the second half or at the exact middle
        current = self.__trailer              #start at trailer
        for i in range(self.__size - (index)):  #current walk to the node at the index passed in
          current = current.previous
        return current.value                  #return value of the node at the index passed in
  
  def rotate_left(self):
    if len(self) == 0 or len(self) == 1:
        return 
    self.__header.next = self.__header.next.next              #attach header's next to index 1 node
    self.__header.next.previous.next = self.__trailer         #attach index 0 node's next to trailer
    self.__trailer.previous.next = self.__header.next.previous#attach index size-1 node's next to index 0 node
    self.__header.next.previous = self.__header               #attach index 1 node's previous to header
    self.__trailer.previous.next.previous = self.__trailer.previous #attach index 1 node's previous to index size-1 node
    self.__trailer.previous = self.__trailer.previous.next    #attach trailer's previous to original index 0 node

  def __str__(self):
    if len(self) == 0:                                              #if list is empty, return empty brackets
        return '[ ]'                                                
    else:
        a = '['                                                 #initialize first bracket
        current = self.__header                                 #initialize current walk
        while current.next is not self.__trailer:                 #go through the entire list
            current = current.next                          
            a += ' '+ str(current.value)+','                        #add the values of the nodes in the list
        a = a[0:len(a)-1]                                       #slice to make it look nice
        a += ' ]'                                               #add the back bracket
        return a

    
if __name__ == '__main__':
  a = Linked_List()
#Does appending to the list add an element at the new tail position and increment the size by one?
  a.append_element('B')
  a.append_element('C')
  a.append_element('D')
  a.append_element('E')
  a.append_element('G')
  print(a)
  print(len(a))
#Does inserting an item at a valid index increase the size by one and correctly modify the list's structure?
  a.insert_element_at('F',4)
  a.insert_element_at('A',0)
  print(a)
  print(len(a))
  
#Does inserting an item at an invalid index leave the list completely unchanged? 
  try:
    a.append_element('H')
    a.append_element('I')
    a.insert_element_at('WRONG',9)
  except IndexError:
    print('Index out of bounds! Try an index greater than or equal to zero or less than the size! ')
  print(a)

  try:
    a.insert_element_at('nope',-52)
  except IndexError:
    print('Index out of bounds! Try an index greater than or equal to zero or less than the size! ')
#Does removing an item at a valid index decrease the size by one and correctly modify the list's structure?
  print(a)
  print(len(a))
  print(a.remove_element_at(8)) #should return element it removes
  print(a.remove_element_at(0))
  print(a.remove_element_at(4))
  print(a)
  print(len(a))
#Does removing an item at an invalid index leave the list completely unchanged?
  try:
    a.remove_element_at(2403)
  except IndexError:
    print('Index out of bounds! Try an index greater than or equal to zero or less than the size! ')
  try:
    a.remove_element_at(-1)
  except IndexError:
    print('Index out of bounds! Try an index greater than or equal to zero or less than the size! ')
#Does length always return the number of values stored in the list (not including sentinel nodes)?
  b = Linked_List()
  for val in range(1,11):
    b.append_element(val)
    print(len(b))
  print(len(b))

  c = Linked_List()
  for val in range(1,101):
    c.append_element(val)
  print(len(c))

#Is the string representation of your list correct for a variety of lengths?
  print(b)
  print(c)
#for loop check with iter and next
  d = Linked_List()
  for val in range(0,51,2):
    d.append_element(val)
  for val in d:
    print(val)
#get_element check
  print(d)
  for val in range(len(d)):
    print(d.get_element_at(val))
#rotate_left check 
    #empty list check
  ham = Linked_List()
  ham.rotate_left()
  print(ham)
  #unempty list check
  ham.append_element(11)
  ham.append_element(22)
  ham.append_element(33)
  ham.append_element(44)
  ham.append_element(55)
  ham.rotate_left()
  ham.rotate_left()
  #should expect order to be 33,44,55,11,22
  print(ham)
#len check for all functions
  eggs = Linked_List()
  eggs.append_element(11)
  eggs.insert_element_at('woah',0)
  eggs.get_element_at(1)
  #should expect [woah,11], and length to be 2
  print(eggs)
  print(len(eggs))
  eggs.remove_element_at(1)
  #should expect [woah] and length to be 1
  print(eggs)
  eggs.rotate_left()
  print(len(eggs))
#check for rotate / string mistake 
  blah = Linked_List()
  blah.append_element('ohhhhh')
  print(blah)
  blah.rotate_left()
  print(blah)
  
