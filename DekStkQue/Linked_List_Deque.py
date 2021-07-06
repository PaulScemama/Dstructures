from Deque import Deque
from Linked_List import Linked_List

class Linked_List_Deque(Deque):

  def __init__(self):
    self.__list = Linked_List()   #Create Linked List object

  def __str__(self):
    return str(self.__list)           #return string method from Linked List class 

  def __len__(self):
    return len(self.__list)           #return length method from Linked List class
  
  # DO NOT CHANGE ANYTHING ABOVE THIS LINE
  
  def push_front(self, val):
    if len(self.__list) == 0:         #if list is empty
      self.__list.append_element(val) #append element
    else:
      self.__list.insert_element_at(val, 0)   #insert element at 0
  
  def pop_front(self):
    if len(self.__list) == 0:     #if list is empty
      return                        #return
    else:
      return self.__list.remove_element_at(0) #remove element at 0

  def peek_front(self):
    if len(self.__list) == 0:   #if list is empty
      return  
    return self.__list.get_element_at(0)    #get value at index 0 

  def push_back(self, val):
    self.__list.append_element(val)         #append element j
  
  def pop_back(self):
    if len(self.__list) == 0:     #if list empty
      return
    else:
      return self.__list.remove_element_at(len(self.__list)-1)    #remove element at last inex

  def peek_back(self):
    if len(self.__list) == 0:     #if list empty
      return 
    return self.__list.get_element_at(len(self.__list)-1) #remove element at last index

# Unit tests make the main section unneccessary.
#if __name__ == '__main__':
 
  
