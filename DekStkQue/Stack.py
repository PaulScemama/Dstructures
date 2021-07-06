from Deque_Generator import get_deque

class Stack:

  def __init__(self):
    self.__dq = get_deque()       #create deque

  def __str__(self):
    return str(self.__dq)     #return string method from either array or Linked List implementation

  def __len__(self):
    return len(self.__dq) #return length method from either array or Linked List implementation

  def push(self, val):
    self.__dq.push_front(val) #return push_front from either array or Linked List implementation

  def pop(self):
    return self.__dq.pop_front()  #return pop_front method from either array or Linked List implementation

  def peek(self):
    return self.__dq.peek_front() #return peek_front method from either array or Linked List implementation

# Unit tests make the main section unneccessary.
#if __name__ == '__main__':

