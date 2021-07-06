from Deque import Deque

class Array_Deque(Deque): #INSERT 'Deque' BACK INTO ARRAY_DEQUE() SO LOOKS LIKE: Array_Deque(Deque)

  def __init__(self):
    # capacity starts at 1; we will grow on demand.
    self.__capacity = 1               
    self.__contents = [None] * self.__capacity      #initialize a list with one cell with the value None inside
    self.__front = None                             #initialize front as none
    self.__back = None                        #initialize back as none
    self.__size = 0                         #size counter for values in list
    # TODO replace pass with any additional initializations you need.
    
    
  def __str__(self):
    if len(self) == 0:                                              #if list is empty, return empty brackets
        return '[ ]'
    else:
      a = '[ '                                                      
      i = self.__front
      while i % self.__capacity != self.__back  % self.__capacity:                   #loop through the list between front and back including them                            
          a += str(self.__contents[i % self.__capacity]) + ',' + ' '                 # add each value to the string
          i += 1 
      a += str(self.__contents[self.__back])                                          #add last value to string
      a += ' ]'
      return a
    
  def __len__(self):
    return self.__size          #return size 

  def __grow(self):
    self.__capacity = self.__capacity * 2               #double capacity counter
    larger = [None] * self.__capacity                   #make a new list with double capacity to copy values into
    if self.__size == 1:                                #if size is 1
        for i in range(len(self.__contents)):           #for values in the range of the length of the contents
            larger[i] = self.__contents[i]              #copy the values onto the new list of Nones
    else:
        i = self.__front                      #counter i as front
        j = 0                                 #corresponding counter for new array
        larger[j] = self.__contents[i]        # copy values for first value
        i += 1                                #increment counter
        j += 1                                #increment counter
        while i % self.__size != self.__front:        #while i mod size is not the front               
            larger[j] = self.__contents[i % self.__size]                  #each element in self.__contents is copied onto larger
            i += 1                        #increment size
            j += 1                        #increment size 
    self.__contents = larger                            #now self.__contents = larger
    self.__front = 0                      #front is index 0 
    self.__back = self.__size - 1         #back is the size - 1 index 
    
  def push_front(self, val):
    if self.__capacity == self.__size:                      #do we have enough room to insert another value? if not
        self.__grow()                                       #grow(double the capacity)
    if self.__capacity == 1 and self.__contents == [None]:  #if it's the first cell to be filled after initialization of the Array
        self.__contents[0] = val                            #insert value at index 0
        self.__front = 0                                    #front point to index 0
        self.__back = 0                                     #back point to index 0
        self.__size += 1                                    #increase size by 1 
    else:
        self.__front = (self.__front - 1) % self.__capacity #move front to the 'left' by one, making sure we don't have an index error with circular array
        self.__contents[self.__front] = val                 #insert value into the cell that front is pointing too
        self.__size += 1                                    #increase size by 1 
    
  def pop_front(self):
    if self.__size == 0:                                    #if size is zero: don't do anything
      return  
    elif self.__size == 1:                                  #if size is one
      to_return = self.__contents[self.__front]             #store return value
      self.__contents[self.__front] = None                  #initialize back to None
      self.__front = None                                   #front as None
      self.__back = None                                    #back as None
      self.__size -= 1                                      #decrement size
      return to_return                                      #return the popped value
    else:
      to_return = self.__contents[self.__front]             #store return value
      self.__front = (self.__front + 1) % self.__capacity   #move front cursor to the right modded with capacity
      self.__size -= 1                                      #decrease size 
      return to_return                                      #return the popped value
    
  def peek_front(self):
    if len(self) == 0:                                      #if the array is empty, return
      return
    return self.__contents[self.__front]                    #return the value at the front
    
  def push_back(self, val):
    if self.__capacity == self.__size:                      #do we have enough room to insert another value? if not
        self.__grow()                                       #grow(double the capacity)
    if self.__capacity == 1 and self.__contents == [None]:  #if it's the first cell to be filled after initialization of the Array
        self.__contents[0] = val                            #insert value at index 0
        self.__front = 0                                    #front point to index 0
        self.__back = 0                                     #back point to index 0
        self.__size += 1                                    #increase size by 1 
    else:
        self.__back = (self.__back + 1) % self.__capacity #move front to the 'left' by one, making sure we don't have an index error with circular array
        self.__contents[self.__back] = val                 #insert value into the cell that front is pointing too
        self.__size += 1                                    #increase size by 1 
    

    # TODO replace pass with your implementation, growing the array before
    # pushing if necessary.
    #add to contents
  
  def pop_back(self):
    if self.__size == 0:                                #size is 0?
      return                                    #return
    elif self.__size == 1:                        #is size is 1
      to_return = self.__contents[self.__back]          #save to return the only value
      self.__contents[self.__back] = None                 #set cell as None
      self.__front = None                 #front as None
      self.__back = None                  #back as None
      self.__size -= 1                    #decrement as None
      return to_return                    #return popped value
    else:
      to_return = self.__contents[self.__back]              #save value that you're gonna pop
      self.__back = (self.__back - 1) % self.__capacity     #move back to the left modded with capacity, compressing the list
      self.__size -= 1                                      #decrement size
      return to_return                                      #return the item you popped

  def peek_back(self):
    if len(self) == 0:                      #if nothing in the list, return
      return
    return self.__contents[self.__back]     #return the value at the back cursor

# No main section is necessary. Unit tests take its place.
#if __name__ == '__main__':


