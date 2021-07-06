import unittest
from Deque_Generator import get_deque
from Stack import Stack
from Queue import Queue

class DSQTester(unittest.TestCase):
  
  def setUp(self):
    self.__deque = get_deque()
    self.__stack = Stack()
    self.__queue = Queue()

#DEQUE TESTING

#PUSH FOCUSED TESTING

  def test_empty_deque_string(self):
    self.assertEqual('[ ]', str(self.__deque), 'Empty list should print as "[ ]"')

  def test_push_front_first_value(self):
    self.__deque.push_front('first')
    self.assertEqual('[ first ]', str(self.__deque))
  
  def test_push_back_first_value(self):
    self.__deque.push_back('first')
    self.assertEqual('[ first ]', str(self.__deque))
  
  def test_push_front_two_values(self):
    self.__deque.push_front('B')
    self.__deque.push_front('A')
    self.assertEqual('[ A, B ]', str(self.__deque))

  def test_push_back_two_values(self):
    self.__deque.push_back('A')
    self.__deque.push_back('B')
    self.assertEqual('[ A, B ]', str(self.__deque))

  def test_pushfront_one__pushback_one(self):
    self.__deque.push_front('A')
    self.__deque.push_back('B')
    self.assertEqual('[ A, B ]', str(self.__deque))

  def test_pushfront_two__pushback_two(self):
    self.__deque.push_front('B')
    self.__deque.push_back('C')
    self.__deque.push_front('A')
    self.__deque.push_back('D')
    self.assertEqual('[ A, B, C, D ]', str(self.__deque))

#POP FOCUSED TESTING

  def test_pop_front_empty_list_return_val(self):
    returned = self.__deque.pop_front()
    self.assertEqual(None, returned)
  
  def test_pop_front_empty_list_str_rep(self):
    self.__deque.pop_front()
    self.assertEqual('[ ]', str(self.__deque))
  
  def test_pop_back_empty_list_return_val(self):
    returned = self.__deque.pop_back()
    self.assertEqual(None, returned)
  
  def test_pop_back_empty_list_str_rep(self):
    self.__deque.pop_back()
    self.assertEqual('[ ]', str(self.__deque))

  def test_pop_front_one_item_after_push_front_return_val(self):
    self.__deque.push_front('A')
    returned = self.__deque.pop_front()
    self.assertEqual('A', returned)

  def test_pop_front_one_item_after_push_front_str_rep(self):
    self.__deque.push_front('A')
    self.__deque.pop_front()
    self.assertEqual('[ ]', str(self.__deque))

  def test_pop_front_one_item_after_push_back_return_val(self):
    self.__deque.push_back('A')
    returned = self.__deque.pop_front()
    self.assertEqual('A', returned)

  def test_pop_front_one_item_after_push_back_str_rep(self):
    self.__deque.push_back('A')
    self.__deque.pop_front()
    self.assertEqual('[ ]', str(self.__deque))

  def test_pop_back_one_item_after_push_front_return_val(self):
    self.__deque.push_front('A')
    returned = self.__deque.pop_back()
    self.assertEqual('A', returned)

  def test_pop_back_one_item_after_push_front_str_rep(self):
    self.__deque.push_front('A')
    self.__deque.pop_back()
    self.assertEqual('[ ]', str(self.__deque))
 
  def test_pop_back_one_item_after_push_back_return_val(self):
    self.__deque.push_back('A')
    returned = self.__deque.pop_back()
    self.assertEqual('A', returned)

  def test_pop_back_one_item_after_push_back_str_rep(self):
    self.__deque.push_back('A')
    self.__deque.pop_back()
    self.assertEqual('[ ]', str(self.__deque))

  def test_pop_front_of_two_items_after_push_front_return_val(self):
    self.__deque.push_front('2')
    self.__deque.push_front('1')
    returned = self.__deque.pop_front()
    self.assertEqual('1', returned)
  
  def test_pop_front_of_two_items_after_push_front_string_rep(self):
    self.__deque.push_front('2')
    self.__deque.push_front('1')
    self.__deque.pop_front()
    self.assertEqual('[ 2 ]', str(self.__deque))

  def test_pop_front_two_items_after_push_back_return_val(self):
    self.__deque.push_back('1')
    self.__deque.push_back('2')
    returned = self.__deque.pop_front()
    self.assertEqual('1', returned)

  def test_pop_front_of_two_items_after_push_back_string_rep(self):
    self.__deque.push_back('1')
    self.__deque.push_back('2')
    self.__deque.pop_front()
    self.assertEqual('[ 2 ]', str(self.__deque))
  
  def test_pop_back_of_two_items_after_push_front_return_val(self):
    self.__deque.push_front('2')
    self.__deque.push_front('1')
    returned = self.__deque.pop_back()
    self.assertEqual('2', returned)
  
  def test_pop_back_of_two_items_after_push_front_string_rep(self):
    self.__deque.push_front('2')
    self.__deque.push_front('1')
    self.__deque.pop_back()
    self.assertEqual('[ 1 ]', str(self.__deque))

  def test_pop_back_of_two_items_after_push_back_return_val(self):
    self.__deque.push_back('1')
    self.__deque.push_back('2')
    returned = self.__deque.pop_back()
    self.assertEqual('2', returned)

  def test_pop_back_of_two_items_after_push_back_string_rep(self):
    self.__deque.push_back('1')
    self.__deque.push_back('2')
    self.__deque.pop_back()
    self.assertEqual('[ 1 ]', str(self.__deque))

  def test_pop_front_two_items_to_empty_list(self):
    self.__deque.push_front('B')
    self.__deque.push_front('A')
    self.__deque.pop_front()
    self.__deque.pop_front()
    self.assertEqual('[ ]', str(self.__deque))

  def test_pop_back_two_items_to_empty_list(self):
    self.__deque.push_front('B')
    self.__deque.push_front('A')
    self.__deque.pop_back()
    self.__deque.pop_back()
    self.assertEqual('[ ]', str(self.__deque))

  def test_pop_backfront_two_items_to_empty_list(self):
    self.__deque.push_front('B')
    self.__deque.push_front('A')
    self.__deque.pop_front()
    self.__deque.pop_back()
    self.assertEqual('[ ]', str(self.__deque))

  

#PEEK FOCUSED TESTING

  def test_peek_front_empty_list_return_val(self):
    returned = self.__deque.peek_front()
    self.assertEqual(None, returned)

  def test_peek_front_empty_list_str_rep(self):
    self.__deque.peek_front()
    self.assertEqual('[ ]', str(self.__deque))

  def test_peek_back_empty_list_return_val(self):
    returned = self.__deque.peek_back()
    self.assertEqual(None, returned)

  def test_peek_back_empty_list_str_rep(self):
    self.__deque.peek_back()
    self.assertEqual('[ ]', str(self.__deque))

  def test_peek_front_one_item_list_return_val(self):
    self.__deque.push_front('hello')
    returned = self.__deque.peek_front()
    self.assertEqual('hello', returned)
  
  def test_peek_front_one_item_list_str_rep(self):
    self.__deque.push_back('hello')
    self.__deque.peek_front()
    self.assertEqual('[ hello ]', str(self.__deque))


  def test_peek_back_one_item_list_return_val(self):
    self.__deque.push_back('hello')
    returned = self.__deque.peek_back()
    self.assertEqual('hello', returned)

  def test_peek_back_one_item_list_str_rep(self):
    self.__deque.push_front('hello')
    self.__deque.peek_back()
    self.assertEqual('[ hello ]', str(self.__deque))
  
  
  def test_peek_front_2_item_list_return_val(self):
    self.__deque.push_front('hello')
    self.__deque.push_back('world')
    returned = self.__deque.peek_front()
    self.assertEqual('hello', returned)
  
  def test_peek_front_2_item_list_str_rep(self):
    self.__deque.push_back('hello')
    self.__deque.push_front('why')
    self.__deque.peek_front()
    self.assertEqual('[ why, hello ]', str(self.__deque))

  def test_peek_back_2_item_list_return_val(self):
    self.__deque.push_back('hello')
    self.__deque.push_back('world')
    returned = self.__deque.peek_back()
    self.assertEqual('world', returned)
  
  def test_peek_back_2_item_list_str_rep(self):
    self.__deque.push_front('hello')
    self.__deque.push_front('why')
    self.__deque.peek_back()
    self.assertEqual('[ why, hello ]', str(self.__deque))
  
#LENGTH TESTING

  def test_len_after_no_items_added(self):
    self.assertEqual(0, len(self.__deque))
  
  def test_len_after_push_front_one_item_added(self):
    self.__deque.push_front('project3')
    self.assertEqual(1, len(self.__deque))
  
  def test_len_after_push_back_one_item_added(self):
    self.__deque.push_back('project3')
    self.assertEqual(1, len(self.__deque))
  
  def test_len_after_pop_front_one_item_added(self):
    self.__deque.push_front('project3')
    self.__deque.pop_front()
    self.assertEqual(0, len(self.__deque))
  
  def test_len_after_pop_back_one_item_added(self):
    self.__deque.push_back('project3')
    self.__deque.pop_back()
    self.assertEqual(0, len(self.__deque))



#EXTRA STR TEST
  def test_string_after_bunch_of_items_added_push_back_and_front(self):
    self.__deque.push_front('1')
    self.__deque.push_front('2')
    self.__deque.push_back('3')
    self.__deque.push_front('4')
    self.__deque.push_back('5')
    self.__deque.push_back('6')
    self.assertEqual('[ 4, 2, 1, 3, 5, 6 ]', str(self.__deque))

  def test_string_after_bunch_of_items_added_push_pop_back_and_front(self):
    self.__deque.push_front('1')
    self.__deque.push_front('2')
    self.__deque.push_back('3')
    self.__deque.pop_front()
    self.__deque.push_front('4')
    self.__deque.pop_back()
    self.__deque.push_back('5')
    self.__deque.push_back('6')
    self.assertEqual('[ 4, 1, 5, 6 ]', str(self.__deque))

  


#STACK TESTING

#PUSH FOCUSED TESTING

  def test_empty_stack_string(self):
    self.assertEqual('[ ]', str(self.__stack), 'Empty list should print as "[ ]"')

  def test_push_first_value(self):
    self.__stack.push('first')
    self.assertEqual('[ first ]', str(self.__stack))
  
  def test_push_two_values(self):
    self.__stack.push('B')
    self.__stack.push('A')
    self.assertEqual('[ A, B ]', str(self.__stack))



#POP FOCUSED TESTING

  def test_pop_empty_list_return_val(self):
    returned = self.__stack.pop()
    self.assertEqual(None, returned)
  
  def test_pop_empty_list_str_rep(self):
    self.__stack.pop()
    self.assertEqual('[ ]', str(self.__stack))
  
  def test_pop_one_item_after_push_return_val(self):
    self.__stack.push('A')
    returned = self.__stack.pop()
    self.assertEqual('A', returned)

  def test_pop_one_item_after_push_str_rep(self):
    self.__stack.push('A')
    self.__stack.pop()
    self.assertEqual('[ ]', str(self.__stack))

  def test_pop_of_two_items_after_push_return_val(self):
    self.__stack.push('2')
    self.__stack.push('1')
    returned = self.__stack.pop()
    self.assertEqual('1', returned)
  
  def test_pop_of_two_items_after_push_string_rep(self):
    self.__stack.push('2')
    self.__stack.push('1')
    self.__stack.pop()
    self.assertEqual('[ 2 ]', str(self.__stack))

  def test_pop_of_two_items_after_push_one_item_str_rep(self):
    self.__stack.push('1')
    self.__stack.pop()
    self.__stack.pop()
    self.assertEqual('[ ]', str(self.__stack))


  def test_pop_two_items_to_empty_stack(self):
    self.__stack.push('B')
    self.__stack.push('A')
    self.__stack.pop()
    self.__stack.pop()
    self.assertEqual('[ ]', str(self.__stack))


  

#PEEK FOCUSED TESTING

  def test_peek_empty_list_return_val(self):
    returned = self.__stack.peek()
    self.assertEqual(None, returned)

  def test_peek_empty_list_str_rep(self):
    self.__stack.peek()
    self.assertEqual('[ ]', str(self.__stack))


  def test_peek_one_item_list_return_val(self):
    self.__stack.push('hello')
    returned = self.__stack.peek()
    self.assertEqual('hello', returned)
  
  def test_peek_one_item_list_str_rep(self):
    self.__stack.push('hello')
    self.__stack.peek()
    self.assertEqual('[ hello ]', str(self.__stack))


  def test_peek_front_2_item_list_return_val_stck(self):
    self.__stack.push('hello')
    self.__stack.push('world')
    returned = self.__stack.peek()
    self.assertEqual('world', returned)
  
  def test_peek_front_2_item_list_str_rep_stck(self):
    self.__stack.push('hello')
    self.__stack.push('why')
    self.__stack.peek()
    self.assertEqual('[ why, hello ]', str(self.__stack))

#LENGTH FOCUSED TESTING

  def test_len_after_no_items_added_stck(self):
    self.assertEqual(0, len(self.__stack))
  
  def test_len_after_push_front_one_item_added_stck(self):
    self.__stack.push('project3')
    self.assertEqual(1, len(self.__stack))
  

  def test_len_after_bunch_of_items_added_push_stck(self):
    self.__stack.push('project3')
    self.__stack.push('project3')
    self.__stack.push('project3')
    self.__stack.push('project3')
    self.__stack.push('project3')
    self.__stack.push('project3')
    self.assertEqual(6, len(self.__stack))

  def test_len_after_bunch_of_items_pushed_popped(self):
    self.__stack.push('1')
    self.__stack.push('2')
    self.__stack.push('3')
    self.__stack.pop()
    self.__stack.push('4')
    self.__stack.pop()
    self.__stack.push('5')
    self.__stack.push('6')
    self.assertEqual(4, len(self.__stack))
#EXTRA STR TEST
  def test_string_after_bunch_of_items_added_push(self):
    self.__stack.push('1')
    self.__stack.push('2')
    self.__stack.push('3')
    self.__stack.push('4')
    self.__stack.push('5')
    self.__stack.push('6')
    self.assertEqual('[ 6, 5, 4, 3, 2, 1 ]', str(self.__stack))


  def test_string_after_bunch_of_items_added_push_pop(self):
    self.__stack.push('1')
    self.__stack.push('2')
    self.__stack.push('3')
    self.__stack.pop()
    self.__stack.push('4')
    self.__stack.pop()
    self.__stack.push('5')
    self.__stack.push('6')
    self.assertEqual('[ 6, 5, 2, 1 ]', str(self.__stack))




#QUEUE TESTING

#ENQUEUE FOCUSED TESTING

  def test_empty_stack_string(self):
    self.assertEqual('[ ]', str(self.__queue))

  def test_enqueue_first_value(self):
    self.__queue.enqueue('first')
    self.assertEqual('[ first ]', str(self.__queue))
  
  def test_enqueue_two_values(self):
    self.__queue.enqueue('B')
    self.__queue.enqueue('A')
    self.assertEqual('[ B, A ]', str(self.__queue))



#DEQUEUE FOCUSED TESTING

  def test_dequeue_empty_list_return_val(self):
    returned = self.__queue.dequeue()
    self.assertEqual(None, returned)
  
  def test_dequeue_empty_list_str_rep(self):
    self.__queue.dequeue()
    self.assertEqual('[ ]', str(self.__queue))
  
  def test_dequeue_one_item_after_enqueue_return_val(self):
    self.__queue.enqueue('A')
    returned = self.__queue.dequeue()
    self.assertEqual('A', returned)

  def test_dequeue_one_item_after_enqueue_str_rep(self):
    self.__queue.enqueue('A')
    self.__queue.dequeue()
    self.assertEqual('[ ]', str(self.__queue))

  def test_dequeue_of_two_items_after_enqueue_return_val(self):
    self.__queue.enqueue('2')
    self.__queue.enqueue('1')
    returned = self.__queue.dequeue()
    self.assertEqual('2', returned)
  
  def test_dequeue_of_two_items_after_enqueue_string_rep(self):
    self.__queue.enqueue('2')
    self.__queue.enqueue('1')
    self.__queue.dequeue()
    self.assertEqual('[ 1 ]', str(self.__queue))

  def test_dequeue_two_items_to_empty_list(self):
    self.__queue.enqueue('B')
    self.__queue.enqueue('A')
    self.__queue.dequeue()
    self.__queue.dequeue()
    self.assertEqual('[ ]', str(self.__queue))

  def test_dequeue_two_items_from_one_item_list(self):
    self.__queue.enqueue('A')
    self.__queue.dequeue()
    self.__queue.dequeue()
    self.assertEqual('[ ]', str(self.__queue))


  

#PEEK FOCUSED TESTING

  def test_peek_empty_list_return_val_queue(self):
    returned = self.__queue.peek()
    self.assertEqual(None, returned)

  def test_peek_empty_list_str_rep_queue(self):
    self.__queue.peek()
    self.assertEqual('[ ]', str(self.__queue))


  def test_peek_one_item_list_return_val_queue(self):
    self.__queue.enqueue('hello')
    returned = self.__queue.peek()
    self.assertEqual('hello', returned)
  
  def test_peek_one_item_list_str_rep_queue(self):
    self.__queue.enqueue('hello')
    self.__queue.peek()
    self.assertEqual('[ hello ]', str(self.__queue))


  def test_peek_2_item_list_return_val_queue(self):
    self.__queue.enqueue('hello')
    self.__queue.enqueue('world')
    returned = self.__queue.peek()
    self.assertEqual('hello', returned)
  
  def test_peek_2_item_list_str_rep_queue(self):
    self.__queue.enqueue('hello')
    self.__queue.enqueue('why')
    self.__queue.peek()
    self.assertEqual('[ hello, why ]', str(self.__queue))

#LENGTH FOCUSED TESTING

  def test_len_after_no_items_added_queue(self):
    self.assertEqual(0, len(self.__queue))
  
  def test_len_after_push_front_one_item_added_queue(self):
    self.__queue.enqueue('project3')
    self.assertEqual(1, len(self.__queue))

  def test_len_after_bunch_of_items_added_push_back_and_front_queue(self):
    self.__queue.enqueue('project3')
    self.__queue.enqueue('project3')
    self.__queue.enqueue('project3')
    self.__queue.enqueue('project3')
    self.__queue.enqueue('project3')
    self.__queue.enqueue('project3')
    self.assertEqual(6, len(self.__queue))

  def test_len_after_bunch_of_items_pushed_popped_queue(self):
    self.__queue.enqueue('project3')
    self.__queue.enqueue('project3')
    self.__queue.dequeue()
    self.__queue.enqueue('project3')
    self.__queue.enqueue('project3')
    self.__queue.dequeue()
    self.__queue.enqueue('project3')
    self.__queue.enqueue('project3')
    self.assertEqual(4, len(self.__queue))

#EXTRA STR TESTING

  def test_len_after_bunch_of_items_added_push_back_and_front_queue(self):
    self.__queue.enqueue('1')
    self.__queue.enqueue('2')
    self.__queue.enqueue('3')
    self.__queue.enqueue('4')
    self.__queue.enqueue('5')
    self.__queue.enqueue('6')
    self.assertEqual('[ 1, 2, 3, 4, 5, 6 ]', str(self.__queue))

  def test_len_after_bunch_of_items_pushed_popped_queue(self):
    self.__queue.enqueue('1')
    self.__queue.enqueue('2')
    self.__queue.dequeue()
    self.__queue.enqueue('3')
    self.__queue.enqueue('4')
    self.__queue.dequeue()
    self.__queue.enqueue('5')
    self.__queue.enqueue('6')
    self.assertEqual('[ 3, 4, 5, 6 ]', str(self.__queue))

if __name__ == '__main__':
  unittest.main()

