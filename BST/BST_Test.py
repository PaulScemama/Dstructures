import unittest
from Binary_Search_Tree import Binary_Search_Tree


class BSTTester(unittest.TestCase):

    def setUp(self):
        self.__BST = Binary_Search_Tree()
    

#We will integrate our traversal testing
#Insertion Testing

    def test_inserting_nothing_in_order(self):
        self.assertEqual('[ ]', str(self.__BST))
        self.assertEqual([ ], self.__BST.to_list())

    def test_inserting_nothing_post_order(self):
        returned = self.__BST.post_order()
        self.assertEqual('[ ]', returned)

    def test_inserting_nothing_pre_order(self):
        returned = self.__BST.pre_order()
        self.assertEqual('[ ]', returned)

    def test_insertion_single_in_order(self):
        self.__BST.insert_element(50)
        self.assertEqual('[ 50 ]', str(self.__BST))
        self.assertEqual([ 50 ], self.__BST.to_list())

    def test_insertion_single_post_order(self):
        self.__BST.insert_element(50)
        returned = self.__BST.post_order()
        self.assertEqual('[ 50 ]', returned)

    def test_insertion_single_pre_order(self):
        self.__BST.insert_element(50)
        returned = self.__BST.pre_order()
        self.assertEqual('[ 50 ]', returned)

    def test_insertion_two_values_smaller_than_root_in_order(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(25)
        self.assertEqual( '[ 25, 50 ]', str(self.__BST))
        self.assertEqual([ 25, 50 ], self.__BST.to_list())

    def test_insertion_two_values_smaller_than_root_post_order(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(25)
        returned = self.__BST.post_order()
        self.assertEqual( '[ 25, 50 ]', returned)

    def test_insertion_two_values_smaller_than_root_pre_order(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(25)
        returned = self.__BST.pre_order()
        self.assertEqual( '[ 50, 25 ]', returned)
    
    def test_insertion_two_values_bigger_than_root_in_order(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(75)
        self.assertEqual('[ 50, 75 ]', str(self.__BST))
        self.assertEqual([ 50, 75 ], self.__BST.to_list())

    def test_insertion_two_values_bigger_than_root_post_order(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(75)
        returned = self.__BST.post_order()
        self.assertEqual('[ 75, 50 ]', returned)

    def test_insertion_two_values_bigger_than_root_pre_order(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(75)
        returned = self.__BST.pre_order()
        self.assertEqual('[ 50, 75 ]', returned)

    def test_insertion_three_values_in_order(self):
        self.__BST.insert_element(100)
        self.__BST.insert_element(193)
        self.__BST.insert_element(78)
        self.assertEqual('[ 78, 100, 193 ]', str(self.__BST))
        self.assertEqual([ 78, 100, 193 ], self.__BST.to_list())

    def test_insertion_three_values_post_order(self):
        self.__BST.insert_element(100)
        self.__BST.insert_element(193)
        self.__BST.insert_element(78)
        returned = self.__BST.post_order()
        self.assertEqual('[ 78, 193, 100 ]', returned)

    def test_insertion_three_values_pre_order(self):
        self.__BST.insert_element(100)
        self.__BST.insert_element(193)
        self.__BST.insert_element(78)
        returned = self.__BST.pre_order()
        self.assertEqual('[ 100, 78, 193 ]', returned)

    def test_insertion_four_values_heavy_left_in_order(self):
        self.__BST.insert_element(100)
        self.__BST.insert_element(101)
        self.__BST.insert_element(73)
        self.__BST.insert_element(75)
        self.assertEqual('[ 73, 75, 100, 101 ]', str(self.__BST))
        self.assertEqual([ 73, 75, 100, 101 ], self.__BST.to_list())


    def test_insertion_four_values_heavy_left_post_order(self):
        self.__BST.insert_element(100)
        self.__BST.insert_element(101)
        self.__BST.insert_element(73)
        self.__BST.insert_element(75)
        returned = self.__BST.post_order()
        self.assertEqual('[ 75, 73, 101, 100 ]', returned)
    
    def test_insertion_four_values_heavy_left_pre_order(self):
        self.__BST.insert_element(100)
        self.__BST.insert_element(101)
        self.__BST.insert_element(73)
        self.__BST.insert_element(75)
        returned = self.__BST.pre_order()
        self.assertEqual('[ 100, 73, 75, 101 ]', returned)
    
    def test_insertion_four_values_heavy_right_in_order(self):
        self.__BST.insert_element(100)
        self.__BST.insert_element(101)
        self.__BST.insert_element(73)
        self.__BST.insert_element(102)
        self.assertEqual('[ 73, 100, 101, 102 ]', str(self.__BST))
        self.assertEqual([ 73, 100, 101, 102 ], self.__BST.to_list())


    def test_insertion_four_values_heavy_right_post_order(self):
        self.__BST.insert_element(100)
        self.__BST.insert_element(101)
        self.__BST.insert_element(73)
        self.__BST.insert_element(102)
        returned = self.__BST.post_order()
        self.assertEqual('[ 73, 102, 101, 100 ]', returned)

    def test_insertion_four_values_heavy_right_pre_order(self):
        self.__BST.insert_element(100)
        self.__BST.insert_element(101)
        self.__BST.insert_element(73)
        self.__BST.insert_element(102)
        returned = self.__BST.pre_order()
        self.assertEqual('[ 100, 73, 101, 102 ]', returned)

    def test_insertion_7_values_perfect_in_order(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(75)
        self.__BST.insert_element(25)
        self.__BST.insert_element(80)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(15)
        self.assertEqual('[ 15, 25, 30, 50, 70, 75, 80 ]', str(self.__BST))
        self.assertEqual([ 15, 25, 30, 50, 70, 75, 80 ], self.__BST.to_list())

    def test_insertion_7_values_perfect_post_order(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(75)
        self.__BST.insert_element(25)
        self.__BST.insert_element(80)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(15)
        returned = self.__BST.post_order()
        self.assertEqual('[ 15, 30, 25, 70, 80, 75, 50 ]', returned)

    def test_insertion_7_values_perfect_pre_order(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(75)
        self.__BST.insert_element(25)
        self.__BST.insert_element(80)
        self.__BST.insert_element(70)
        self.__BST.insert_element(30)
        self.__BST.insert_element(15)
        returned = self.__BST.pre_order()
        self.assertEqual('[ 50, 25, 15, 30, 75, 70, 80 ]', returned)

    def test_insertion_only_left_in_order(self):
        self.__BST.insert_element(9)
        self.__BST.insert_element(8)
        self.__BST.insert_element(7)
        self.__BST.insert_element(6)
        self.__BST.insert_element(5)
        self.__BST.insert_element(4)
        self.__BST.insert_element(3)
        self.assertEqual('[ 3, 4, 5, 6, 7, 8, 9 ]', str(self.__BST))
        self.assertEqual([ 3, 4, 5, 6, 7, 8, 9 ], self.__BST.to_list())

    def test_insertion_only_left_post_order(self):
        self.__BST.insert_element(9)
        self.__BST.insert_element(8)
        self.__BST.insert_element(7)
        self.__BST.insert_element(6)
        self.__BST.insert_element(5)
        self.__BST.insert_element(4)
        self.__BST.insert_element(3)
        returned = self.__BST.post_order()
        self.assertEqual('[ 3, 5, 4, 7, 9, 8, 6 ]', returned)

    def test_insertion_only_left_pre_order(self):
        self.__BST.insert_element(9)
        self.__BST.insert_element(8)
        self.__BST.insert_element(7)
        self.__BST.insert_element(6)
        self.__BST.insert_element(5)
        self.__BST.insert_element(4)
        self.__BST.insert_element(3)
        returned = self.__BST.pre_order()
        self.assertEqual('[ 6, 4, 3, 5, 8, 7, 9 ]', returned)
    
    def test_insert_only_right_in_order(self):
        self.__BST.insert_element(1)
        self.__BST.insert_element(2)
        self.__BST.insert_element(3)
        self.__BST.insert_element(4)
        self.__BST.insert_element(5)
        self.__BST.insert_element(6)
        self.__BST.insert_element(7)  
        self.assertEqual('[ 1, 2, 3, 4, 5, 6, 7 ]', str(self.__BST)) 
        self.assertEqual([ 1, 2, 3, 4, 5, 6, 7 ], self.__BST.to_list()) 

    def test_insert_only_right_post_order(self):
        self.__BST.insert_element(1)
        self.__BST.insert_element(2)
        self.__BST.insert_element(3)
        self.__BST.insert_element(4)
        self.__BST.insert_element(5)
        self.__BST.insert_element(6)
        self.__BST.insert_element(7) 
        returned = self.__BST.post_order() 
        self.assertEqual('[ 1, 3, 2, 5, 7, 6, 4 ]', returned) 

    def test_insert_only_right_pre_order(self):
        self.__BST.insert_element(1)
        self.__BST.insert_element(2)
        self.__BST.insert_element(3)
        self.__BST.insert_element(4)
        self.__BST.insert_element(5)
        self.__BST.insert_element(6)
        self.__BST.insert_element(7) 
        returned = self.__BST.pre_order() 
        self.assertEqual('[ 4, 2, 1, 3, 6, 5, 7 ]', returned) 

    def test_insert_duplicate_ignore_in_order(self): 
        with self.assertRaises(ValueError):
            self.__BST.insert_element(1)
            self.__BST.insert_element(1)
        self.assertEqual('[ 1 ]', str(self.__BST))
        self.assertEqual([ 1 ], self.__BST.to_list())

    def test_insert_duplicate_ignore_post_order(self): 
        with self.assertRaises(ValueError):
            self.__BST.insert_element(1)
            self.__BST.insert_element(1)
        returned = self.__BST.post_order()
        self.assertEqual('[ 1 ]', returned)

    def test_insert_duplicate_ignore_pre_order(self): 
        with self.assertRaises(ValueError):
            self.__BST.insert_element(1)
            self.__BST.insert_element(1)
        returned = self.__BST.pre_order()
        self.assertEqual('[ 1 ]', returned)

#Removal Testing

    def test_removal_leaf_minimum_nodes_in_order(self):
        self.__BST.insert_element(50)
        self.__BST.remove_element(50)
        self.assertEqual('[ ]', str(self.__BST))
        self.assertEqual([ ], self.__BST.to_list())


    def test_removal_leaf_minimum_nodes_post_order(self):
        self.__BST.insert_element(50)
        self.__BST.remove_element(50)
        returned = self.__BST.post_order()
        self.assertEqual('[ ]', returned)

    def test_removal_leaf_minimum_nodes_pre_order(self):
        self.__BST.insert_element(50)
        self.__BST.remove_element(50)
        returned = self.__BST.pre_order()
        self.assertEqual('[ ]', returned)

    def test_removal_leaf_large_tree_in_order(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(75)
        self.__BST.insert_element(25)
        self.__BST.insert_element(100)
        self.__BST.insert_element(35)
        self.__BST.remove_element(35)
        self.assertEqual('[ 25, 50, 75, 100 ]', str(self.__BST))
        self.assertEqual([ 25, 50, 75, 100 ], self.__BST.to_list())

    def test_removal_leaf_large_tree_post_order(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(75)
        self.__BST.insert_element(25)
        self.__BST.insert_element(100)
        self.__BST.insert_element(35)
        self.__BST.remove_element(35)
        returned = self.__BST.post_order()
        self.assertEqual('[ 25, 100, 75, 50 ]', returned)

    def test_removal_leaf_large_tree_pre_order(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(75)
        self.__BST.insert_element(25)
        self.__BST.insert_element(100)
        self.__BST.insert_element(35)
        self.__BST.remove_element(35)
        returned = self.__BST.pre_order()
        self.assertEqual('[ 50, 25, 75, 100 ]', returned)

    def test_removal_one_child_minimum_nodes_in_order(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(35)
        self.__BST.remove_element(50)
        self.assertEqual('[ 35 ]', str(self.__BST))
        self.assertEqual([ 35 ], self.__BST.to_list())

    def test_removal_one_child_minimum_nodes_post_order(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(35)
        self.__BST.remove_element(50)
        returned = self.__BST.post_order()
        self.assertEqual('[ 35 ]', returned)

    def test_removal_one_child_minimum_nodes_pre_order(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(35)
        self.__BST.remove_element(50)
        returned = self.__BST.pre_order()
        self.assertEqual('[ 35 ]', returned)

    def test_removal_one_child_large_tree_in_order(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(75)
        self.__BST.insert_element(25)
        self.__BST.insert_element(100)
        self.__BST.insert_element(35)
        self.__BST.remove_element(25)
        self.assertEqual('[ 35, 50, 75, 100 ]', str(self.__BST))
        self.assertEqual([ 35, 50, 75, 100 ], self.__BST.to_list())

    def test_removal_one_child_large_tree_post_order(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(75)
        self.__BST.insert_element(25)
        self.__BST.insert_element(100)
        self.__BST.insert_element(35)
        self.__BST.remove_element(25)
        returned = self.__BST.post_order()
        self.assertEqual('[ 35, 100, 75, 50 ]', returned)

    def test_removal_one_child_large_tree_pre_order(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(75)
        self.__BST.insert_element(25)
        self.__BST.insert_element(100)
        self.__BST.insert_element(35)
        self.__BST.remove_element(25)
        returned = self.__BST.pre_order()
        self.assertEqual('[ 50, 35, 75, 100 ]', returned)

    def test_removal_two_children_minimum_nodes_in_order(self):
        self.__BST.insert_element(103)
        self.__BST.insert_element(101)
        self.__BST.insert_element(105)
        self.__BST.remove_element(103)
        self.assertEqual('[ 101, 105 ]', str(self.__BST))
        self.assertEqual([ 101, 105 ], self.__BST.to_list())

    def test_removal_two_children_minimum_nodes_post_order(self):
        self.__BST.insert_element(103)
        self.__BST.insert_element(101)
        self.__BST.insert_element(105)
        self.__BST.remove_element(103)
        returned = self.__BST.post_order()
        self.assertEqual('[ 101, 105 ]', returned)

    def test_removal_two_children_minimum_nodes_pre_order(self):
        self.__BST.insert_element(103)
        self.__BST.insert_element(101)
        self.__BST.insert_element(105)
        self.__BST.remove_element(103)
        returned = self.__BST.pre_order()
        self.assertEqual('[ 105, 101 ]', returned)

    def test_removal_two_children_large_tree_v1_in_order(self):
        self.__BST.insert_element(36)
        self.__BST.insert_element(43)
        self.__BST.insert_element(23)
        self.__BST.insert_element(25)
        self.__BST.insert_element(7)
        self.__BST.insert_element(28)
        self.__BST.remove_element(23)
        self.assertEqual('[ 7, 25, 28, 36, 43 ]', str(self.__BST))
        self.assertEqual([ 7, 25, 28, 36, 43 ], self.__BST.to_list())

    def test_removal_two_children_large_tree_v1_post_order(self):
        self.__BST.insert_element(36)
        self.__BST.insert_element(43)
        self.__BST.insert_element(23)
        self.__BST.insert_element(25)
        self.__BST.insert_element(7)
        self.__BST.insert_element(28)
        self.__BST.remove_element(23)
        returned = self.__BST.post_order()
        self.assertEqual('[ 7, 28, 43, 36, 25 ]', returned)

    def test_removal_two_children_large_tree_v1_pre_order(self):
        self.__BST.insert_element(36)
        self.__BST.insert_element(43)
        self.__BST.insert_element(23)
        self.__BST.insert_element(25)
        self.__BST.insert_element(7)
        self.__BST.insert_element(28)
        self.__BST.remove_element(23)
        returned = self.__BST.pre_order()
        self.assertEqual('[ 25, 7, 36, 28, 43 ]', returned)

    def test_removal_two_children_large_tree__v2_in_order(self):
        self.__BST.insert_element(36)
        self.__BST.insert_element(43)
        self.__BST.insert_element(23)
        self.__BST.insert_element(25)
        self.__BST.insert_element(7)
        self.__BST.insert_element(24)
        self.__BST.remove_element(23)
        self.assertEqual('[ 7, 24, 25, 36, 43 ]', str(self.__BST))
        self.assertEqual([ 7, 24, 25, 36, 43 ], self.__BST.to_list())

    def test_removal_two_children_large_tree_v2_post_order(self):
        self.__BST.insert_element(36)
        self.__BST.insert_element(43)
        self.__BST.insert_element(23)
        self.__BST.insert_element(25)
        self.__BST.insert_element(7)
        self.__BST.insert_element(24)
        self.__BST.remove_element(23)
        returned = self.__BST.post_order()
        self.assertEqual('[ 7, 24, 43, 36, 25 ]', returned)

    def test_removal_two_children_large_tree_v2_pre_order(self):
        self.__BST.insert_element(36)
        self.__BST.insert_element(43)
        self.__BST.insert_element(23)
        self.__BST.insert_element(25)
        self.__BST.insert_element(7)
        self.__BST.insert_element(24)
        self.__BST.remove_element(23)
        returned = self.__BST.pre_order()
        self.assertEqual('[ 25, 24, 7, 36, 43 ]', returned)

    def test_removal_no_children_intensive_in_order(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.insert_element(20)
        self.__BST.insert_element(10)
        self.__BST.remove_element(10)
        self.__BST.remove_element(20)
        self.__BST.remove_element(30)
        self.assertEqual('[ 50 ]', str(self.__BST))
        self.assertEqual([ 50 ], self.__BST.to_list())

    def test_removal_no_children_intensive_post_order(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.insert_element(20)
        self.__BST.insert_element(10)
        self.__BST.remove_element(10)
        self.__BST.remove_element(20)
        self.__BST.remove_element(30)
        returned = self.__BST.post_order()
        self.assertEqual('[ 50 ]', returned)

    def test_removal_no_children_intensive_pre_order(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.insert_element(20)
        self.__BST.insert_element(10)
        self.__BST.remove_element(10)
        self.__BST.remove_element(20)
        self.__BST.remove_element(30)
        returned = self.__BST.pre_order()
        self.assertEqual('[ 50 ]', returned)

    def test_removal_one_child_intensive_in_order_left(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.insert_element(20)
        self.__BST.insert_element(10)
        self.__BST.remove_element(20)
        self.__BST.remove_element(30)
        self.__BST.remove_element(50)
        self.assertEqual('[ 10 ]', str(self.__BST))
        self.assertEqual([ 10 ], self.__BST.to_list())

    def test_removal_one_child_intensive_post_order_left(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.insert_element(20)
        self.__BST.insert_element(10)
        self.__BST.remove_element(20)
        self.__BST.remove_element(30)
        self.__BST.remove_element(50)
        returned = self.__BST.post_order()
        self.assertEqual('[ 10 ]', returned)

    def test_removal_one_child_intensive_pre_order_left(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(30)
        self.__BST.insert_element(20)
        self.__BST.insert_element(10)
        self.__BST.remove_element(20)
        self.__BST.remove_element(30)
        self.__BST.remove_element(50)
        returned = self.__BST.pre_order()
        self.assertEqual('[ 10 ]', returned)

    def test_removal_one_child_intensive_in_order_right(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(60)
        self.__BST.insert_element(70)
        self.__BST.insert_element(80)
        self.__BST.remove_element(70)
        self.__BST.remove_element(60)
        self.__BST.remove_element(50)
        self.assertEqual('[ 80 ]', str(self.__BST))
        self.assertEqual([ 80 ], self.__BST.to_list())

    def test_removal_one_child_intensive_post_order_right(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(60)
        self.__BST.insert_element(70)
        self.__BST.insert_element(80)
        self.__BST.remove_element(70)
        self.__BST.remove_element(60)
        self.__BST.remove_element(50)
        returned = self.__BST.post_order()
        self.assertEqual('[ 80 ]', returned)

    def test_removal_one_child_intensive_pre_order_right(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(60)
        self.__BST.insert_element(70)
        self.__BST.insert_element(80)
        self.__BST.remove_element(70)
        self.__BST.remove_element(60)
        self.__BST.remove_element(50)
        returned = self.__BST.pre_order()
        self.assertEqual('[ 80 ]', returned)

    def test_removal_two_children_intensive_in_order(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(25)
        self.__BST.insert_element(75)
        self.__BST.insert_element(80)
        self.__BST.insert_element(73)
        self.__BST.insert_element(30)
        self.__BST.insert_element(23)
        self.__BST.remove_element(25)
        self.__BST.remove_element(75)
        self.__BST.remove_element(50)
        self.assertEqual('[ 23, 30, 73, 80 ]', str(self.__BST))
        self.assertEqual([ 23, 30, 73, 80 ], self.__BST.to_list())

    def test_removal_two_children_intensive_post_order(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(25)
        self.__BST.insert_element(75)
        self.__BST.insert_element(80)
        self.__BST.insert_element(73)
        self.__BST.insert_element(30)
        self.__BST.insert_element(23)
        self.__BST.remove_element(25)
        self.__BST.remove_element(75)
        self.__BST.remove_element(50)
        returned = self.__BST.post_order()
        self.assertEqual('[ 23, 30, 80, 73 ]', returned)

    def test_removal_two_children_intensive_pre_order(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(25)
        self.__BST.insert_element(75)
        self.__BST.insert_element(80)
        self.__BST.insert_element(73)
        self.__BST.insert_element(30)
        self.__BST.insert_element(23)
        self.__BST.remove_element(25)
        self.__BST.remove_element(75)
        self.__BST.remove_element(50)
        returned = self.__BST.pre_order()
        self.assertEqual('[ 73, 30, 23, 80 ]', returned)

    def test_remove_unfound_empty_list_ignore_in_order(self):
        with self.assertRaises(ValueError):
            self.__BST.remove_element(4)
        self.assertEqual('[ ]', str(self.__BST)) 
        self.assertEqual([ ], self.__BST.to_list())    

    def test_remove_unfound_empty_list_ignore_post_order(self):
        with self.assertRaises(ValueError):
            self.__BST.remove_element(4)
        returned = self.__BST.post_order()
        self.assertEqual('[ ]', returned)

    def test_remove_unfound_empty_list_ignore_pre_order(self):
        with self.assertRaises(ValueError):
            self.__BST.remove_element(4)
        returned = self.__BST.pre_order()
        self.assertEqual('[ ]', returned)

    def test_remove_unfound_ignore_in_order(self): 
        with self.assertRaises(ValueError):
            self.__BST.insert_element(1)
            self.__BST.remove_element(4)
        self.assertEqual('[ 1 ]', str(self.__BST))
        self.assertEqual([ 1 ], self.__BST.to_list())

    def test_remove_unfound_ignore_post_order(self): 
        with self.assertRaises(ValueError):
            self.__BST.insert_element(1)
            self.__BST.remove_element(4)
        returned = self.__BST.post_order()
        self.assertEqual('[ 1 ]', returned)

    def test_remove_unfound_ignore_pre_order(self): 
        with self.assertRaises(ValueError):
            self.__BST.insert_element(1)
            self.__BST.remove_element(4)
        returned = self.__BST.pre_order()
        self.assertEqual('[ 1 ]', returned)



    
#Height Testing

    def test_height_of_empty_tree(self):
        returned = self.__BST.get_height()
        self.assertEqual(0, returned)

    def test_height_after_single_insertion(self):
        self.__BST.insert_element(38)
        returned = self.__BST.get_height()
        self.assertEqual(1, returned)

    def test_height_after_single_insertion_then_removal(self):
        self.__BST.insert_element(38)
        self.__BST.remove_element(38)
        returned = self.__BST.get_height()
        self.assertEqual(0, returned)

    def test_height_after_two_insertions_left_heavy(self):
        self.__BST.insert_element(38)
        self.__BST.insert_element(35)
        returned = self.__BST.get_height()
        self.assertEqual(2, returned)

    def test_height_after_two_insertions_right_heavy(self):
        self.__BST.insert_element(38)
        self.__BST.insert_element(40)
        returned = self.__BST.get_height()
        self.assertEqual(2, returned)

    def test_height_after_two_insertions_left_heavy_and_removal_leaf(self):
        self.__BST.insert_element(38)
        self.__BST.insert_element(35)
        self.__BST.remove_element(35)
        returned = self.__BST.get_height()
        self.assertEqual(1, returned) 

    def test_height_after_two_insertions_right_heavy_and_removal_leaf(self):
        self.__BST.insert_element(38)
        self.__BST.insert_element(40)
        self.__BST.remove_element(40)
        returned = self.__BST.get_height()
        self.assertEqual(1, returned) 

    def test_height_after_removal_root_no_change_in_height(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(25)
        self.__BST.insert_element(75)
        self.__BST.remove_element(50)
        returned = self.__BST.get_height()
        self.assertEqual(2, returned)

    def test_height_after_removal_leaf_no_change_in_height(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(25)
        self.__BST.insert_element(75)
        self.__BST.remove_element(25)
        returned = self.__BST.get_height()
        self.assertEqual(2, returned)

    def test_height_of_3_perfect_tree(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(25)
        self.__BST.insert_element(75)
        self.__BST.insert_element(80)
        self.__BST.insert_element(73)
        self.__BST.insert_element(30)
        self.__BST.insert_element(23)
        returned = self.__BST.get_height()
        self.assertEqual(3, returned)

    def test_height_of_3_perfect_tree_then_removal_all_leaf(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(25)
        self.__BST.insert_element(75)
        self.__BST.insert_element(80)
        self.__BST.insert_element(73)
        self.__BST.insert_element(30)
        self.__BST.insert_element(23)
        self.__BST.remove_element(23)
        self.__BST.remove_element(30)
        self.__BST.remove_element(73)
        self.__BST.remove_element(80)
        returned = self.__BST.get_height()
        self.assertEqual(2, returned)

    def test_height_of_3_perfect_tree_then_removal_all_inner_nodes_two_gens(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(25)
        self.__BST.insert_element(75)
        self.__BST.insert_element(80)
        self.__BST.insert_element(73)
        self.__BST.insert_element(30)
        self.__BST.insert_element(23)
        self.__BST.remove_element(25)
        self.__BST.remove_element(75)
        self.__BST.remove_element(30)
        self.__BST.remove_element(80)
        returned = self.__BST.get_height()
        self.assertEqual(2, returned)

    def test_height_of_2_perfect_tree_remove_right_child(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(25)
        self.__BST.insert_element(75)
        self.__BST.remove_element(75)
        self.assertEqual(2, self.__BST.get_height())

    def test_height_of_2_perfect_tree_remove_left_child(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(25)
        self.__BST.insert_element(75)
        self.__BST.remove_element(75)
        self.assertEqual(2, self.__BST.get_height())

    def test_height_of_2_perfect_tree_remove_parent(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(25)
        self.__BST.insert_element(75)
        self.__BST.remove_element(75)
        self.assertEqual(2, self.__BST.get_height())

    def test_height_2_left_tree_remove_parent(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(25)
        self.__BST.remove_element(50)
        self.assertEqual(1, self.__BST.get_height())

#BALANCED HEIGHT TESTING  

#INSERTION
    def test_height_single_rotation_left_floater_is_none___at_root(self):
        self.__BST.insert_element(73)
        self.__BST.insert_element(75)
        self.__BST.insert_element(100)
        self.assertEqual(2, self.__BST.get_height())
    
    def test_single_rotation_left_floater_is_none___at_root_in_order(self):
        self.__BST.insert_element(73)
        self.__BST.insert_element(75)
        self.__BST.insert_element(100)
        self.assertEqual('[ 73, 75, 100 ]', str(self.__BST))
        self.assertEqual([ 73, 75, 100 ], self.__BST.to_list())

    def test_single_rotation_left_floater_is_none___at_root_post(self):
        self.__BST.insert_element(73)
        self.__BST.insert_element(75)
        self.__BST.insert_element(100)
        returned = self.__BST.post_order()
        self.assertEqual('[ 73, 100, 75 ]', returned)

    def test_single_rotation_left_floater_is_none___at_root_pre(self):
        self.__BST.insert_element(73)
        self.__BST.insert_element(75)
        self.__BST.insert_element(100)
        returned = self.__BST.pre_order()
        self.assertEqual('[ 75, 73, 100 ]', returned)
        
    def test_height_single_rotation_right_floater_is_none___at_root(self):
        self.__BST.insert_element(101)
        self.__BST.insert_element(100)
        self.__BST.insert_element(75)
        self.assertEqual(2, self.__BST.get_height())

    def test_height_single_rotation_right_floater_is_none___at_root_in(self):
        self.__BST.insert_element(101)
        self.__BST.insert_element(100)
        self.__BST.insert_element(75)
        self.assertEqual('[ 75, 100, 101 ]', str(self.__BST))
        self.assertEqual([ 75, 100, 101 ], self.__BST.to_list())

    def test_height_single_rotation_right_floater_is_none___at_root_post(self):
        self.__BST.insert_element(101)
        self.__BST.insert_element(100)
        self.__BST.insert_element(75)
        returned = self.__BST.post_order()
        self.assertEqual('[ 75, 101, 100 ]', returned)

    def test_height_single_rotation_right_floater_is_none___at_root_pre(self):
        self.__BST.insert_element(101)
        self.__BST.insert_element(100)
        self.__BST.insert_element(75)
        returned = self.__BST.pre_order()
        self.assertEqual('[ 100, 75, 101 ]', returned)

    def test_height_single_rotation_left_w_floater(self):
        self.__BST.insert_element(73)
        self.__BST.insert_element(70)
        self.__BST.insert_element(75)
        self.__BST.insert_element(74)
        self.__BST.insert_element(100)
        self.__BST.insert_element(101)
        self.assertEqual(3, self.__BST.get_height())

    def test_height_single_rotation_left_w_floater_in(self):
        self.__BST.insert_element(73)
        self.__BST.insert_element(70)
        self.__BST.insert_element(75)
        self.__BST.insert_element(74)
        self.__BST.insert_element(100)
        self.__BST.insert_element(101)
        self.assertEqual('[ 70, 73, 74, 75, 100, 101 ]', str(self.__BST))
        self.assertEqual([ 70, 73, 74, 75, 100, 101 ], self.__BST.to_list())

    def test_height_single_rotation_left_w_floater_post(self):
        self.__BST.insert_element(73)
        self.__BST.insert_element(70)
        self.__BST.insert_element(75)
        self.__BST.insert_element(74)
        self.__BST.insert_element(100)
        self.__BST.insert_element(101)
        returned = self.__BST.post_order()
        self.assertEqual('[ 70, 74, 73, 101, 100, 75 ]', returned)

    def test_height_single_rotation_left_w_floater_pre(self):
        self.__BST.insert_element(73)
        self.__BST.insert_element(70)
        self.__BST.insert_element(75)
        self.__BST.insert_element(74)
        self.__BST.insert_element(100)
        self.__BST.insert_element(101)
        returned = self.__BST.pre_order()
        self.assertEqual('[ 75, 73, 70, 74, 100, 101 ]', returned)

    def test_height_single_rotation_right_w_floater(self):
        self.__BST.insert_element(101)
        self.__BST.insert_element(102)
        self.__BST.insert_element(97)
        self.__BST.insert_element(98)
        self.__BST.insert_element(75)
        self.__BST.insert_element(73)
        self.assertEqual(3, self.__BST.get_height())


    def test_height_rotate_right_left_without_floater_first_rotate(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(35)
        self.__BST.insert_element(75)
        self.__BST.insert_element(77)
        self.__BST.insert_element(73)
        self.__BST.insert_element(65)
        self.assertEqual(3, self.__BST.get_height())

    def test_height_rotate_right_left_without_floater_first_rotate_in(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(35)
        self.__BST.insert_element(75)
        self.__BST.insert_element(77)
        self.__BST.insert_element(73)
        self.__BST.insert_element(65)
        self.assertEqual('[ 35, 50, 65, 73, 75, 77 ]', str(self.__BST))
        self.assertEqual([ 35, 50, 65, 73, 75, 77 ], self.__BST.to_list())

    def test_height_rotate_right_left_without_floater_first_rotate_post(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(35)
        self.__BST.insert_element(75)
        self.__BST.insert_element(77)
        self.__BST.insert_element(73)
        self.__BST.insert_element(65)
        returned = self.__BST.post_order()
        self.assertEqual('[ 35, 65, 50, 77, 75, 73 ]', returned)
 
 
    def test_height_rotate_right_left_without_floater_first_rotate_pre(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(35)
        self.__BST.insert_element(75)
        self.__BST.insert_element(77)
        self.__BST.insert_element(73)
        self.__BST.insert_element(65)
        returned = self.__BST.pre_order()
        self.assertEqual('[ 73, 50, 35, 65, 75, 77 ]', returned)


    def test_height_rotate_right_left_with_floater_first_rotate(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(35)
        self.__BST.insert_element(75)
        self.__BST.insert_element(73)
        self.__BST.insert_element(77)
        self.__BST.insert_element(74)
        self.assertEqual(3, self.__BST.get_height())

    def test_height_rotate_right_left_with_floater_first_rotate_in(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(35)
        self.__BST.insert_element(75)
        self.__BST.insert_element(73)
        self.__BST.insert_element(77)
        self.__BST.insert_element(74)
        self.assertEqual('[ 35, 50, 73, 74, 75, 77 ]', str(self.__BST))
        self.assertEqual([ 35, 50, 73, 74, 75, 77 ], self.__BST.to_list())

    def test_height_rotate_right_left_with_floater_first_rotate_post(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(35)
        self.__BST.insert_element(75)
        self.__BST.insert_element(73)
        self.__BST.insert_element(77)
        self.__BST.insert_element(74)
        returned = self.__BST.post_order()
        self.assertEqual('[ 35, 50, 74, 77, 75, 73 ]', returned)

    def test_height_rotate_right_left_with_floater_first_rotate_pre(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(35)
        self.__BST.insert_element(75)
        self.__BST.insert_element(73)
        self.__BST.insert_element(77)
        self.__BST.insert_element(74)
        returned = self.__BST.pre_order()
        self.assertEqual('[ 73, 50, 35, 75, 74, 77 ]', returned )


    def test_height_rotate_left_right_without_floater_first_rotate(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(75)
        self.__BST.insert_element(35)
        self.__BST.insert_element(40)
        self.__BST.insert_element(44)
        self.assertEqual(3, self.__BST.get_height()) 

    def test_height_rotate_left_right_without_floater_first_rotate_in(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(75)
        self.__BST.insert_element(35)
        self.__BST.insert_element(40)
        self.__BST.insert_element(44)
        self.assertEqual('[ 35, 40, 44, 50, 75 ]', str(self.__BST)) 
        self.assertEqual([ 35, 40, 44, 50, 75 ], self.__BST.to_list()) 

    def test_height_rotate_left_right_without_floater_first_rotate_post(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(75)
        self.__BST.insert_element(35)
        self.__BST.insert_element(40)
        self.__BST.insert_element(44)
        returned = self.__BST.post_order()
        self.assertEqual('[ 35, 44, 40, 75, 50 ]', returned) 

    def test_height_rotate_left_right_without_floater_first_rotate_pre(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(75)
        self.__BST.insert_element(35)
        self.__BST.insert_element(40)
        self.__BST.insert_element(44)
        returned = self.__BST.pre_order()
        self.assertEqual('[ 50, 40, 35, 44, 75 ]', returned) 

    def test_height_rotate_left_right_with_floater_first_rotate(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(75)
        self.__BST.insert_element(35)
        self.__BST.insert_element(40)
        self.__BST.insert_element(30)
        self.__BST.insert_element(45)
        self.assertEqual(3, self.__BST.get_height()) 

    def test_height_rotate_left_right_with_floater_first_rotate_in(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(75)
        self.__BST.insert_element(35)
        self.__BST.insert_element(40)
        self.__BST.insert_element(30)
        self.__BST.insert_element(45)
        self.assertEqual('[ 30, 35, 40, 45, 50, 75 ]', str(self.__BST)) 
        self.assertEqual([ 30, 35, 40, 45, 50, 75 ], self.__BST.to_list())

    def test_height_rotate_left_right_with_floater_first_rotate_post(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(75)
        self.__BST.insert_element(35)
        self.__BST.insert_element(40)
        self.__BST.insert_element(30)
        self.__BST.insert_element(45)
        returned = self.__BST.post_order()
        self.assertEqual('[ 30, 35, 45, 75, 50, 40 ]', returned) 

    def test_height_rotate_left_right_with_floater_first_rotate_pre(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(75)
        self.__BST.insert_element(35)
        self.__BST.insert_element(40)
        self.__BST.insert_element(30)
        self.__BST.insert_element(45)
        returned = self.__BST.pre_order()
        self.assertEqual('[ 40, 35, 30, 50, 45, 75 ]', returned) 


    def test_height_rotate_right_left_deep_imbalanceV1(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(10)
        self.__BST.insert_element(60)
        self.__BST.insert_element(5)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(25)
        self.__BST.insert_element(50)
        self.__BST.insert_element(80) 
        self.__BST.insert_element(22)
        self.assertEqual(4, self.__BST.get_height())  

    def test_height_rotate_right_left_deep_imbalanceV1_in(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(10)
        self.__BST.insert_element(60)
        self.__BST.insert_element(5)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(25)
        self.__BST.insert_element(50)
        self.__BST.insert_element(80) 
        self.__BST.insert_element(22)
        self.assertEqual('[ 5, 10, 20, 22, 25, 30, 50, 60, 70, 80 ]', str(self.__BST))  
        self.assertEqual([ 5, 10, 20, 22, 25, 30, 50, 60, 70, 80 ], self.__BST.to_list())

    def test_height_rotate_right_left_deep_imbalanceV1_post(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(10)
        self.__BST.insert_element(60)
        self.__BST.insert_element(5)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(25)
        self.__BST.insert_element(50)
        self.__BST.insert_element(80) 
        self.__BST.insert_element(22)
        returned = self.__BST.post_order()
        self.assertEqual('[ 5, 10, 22, 25, 20, 50, 80, 70, 60, 30 ]', returned)  

    def test_height_rotate_right_left_deep_imbalanceV1_pre(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(10)
        self.__BST.insert_element(60)
        self.__BST.insert_element(5)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(25)
        self.__BST.insert_element(50)
        self.__BST.insert_element(80) 
        self.__BST.insert_element(22)
        returned = self.__BST.pre_order()
        self.assertEqual('[ 30, 20, 10, 5, 25, 22, 60, 50, 70, 80 ]', returned)  



    def test_height_rotate_right_left_deep_imbalanceV2(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(10)
        self.__BST.insert_element(60)
        self.__BST.insert_element(5)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(25)
        self.__BST.insert_element(50)
        self.__BST.insert_element(80) 
        self.__BST.insert_element(27)
        self.assertEqual(4, self.__BST.get_height())


    def test_height_rotate_right_left_deep_imbalanceV2_in(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(10)
        self.__BST.insert_element(60)
        self.__BST.insert_element(5)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(25)
        self.__BST.insert_element(50)
        self.__BST.insert_element(80) 
        self.__BST.insert_element(27)
        self.assertEqual('[ 5, 10, 20, 25, 27, 30, 50, 60, 70, 80 ]', str(self.__BST))
        self.assertEqual([ 5, 10, 20, 25, 27, 30, 50, 60, 70, 80 ], self.__BST.to_list())


    def test_height_rotate_right_left_deep_imbalanceV2_post(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(10)
        self.__BST.insert_element(60)
        self.__BST.insert_element(5)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(25)
        self.__BST.insert_element(50)
        self.__BST.insert_element(80) 
        self.__BST.insert_element(27)
        returned = self.__BST.post_order()
        self.assertEqual('[ 5, 10, 27, 25, 20, 50, 80, 70, 60, 30 ]', returned)


    def test_height_rotate_right_left_deep_imbalanceV2_pre(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(10)
        self.__BST.insert_element(60)
        self.__BST.insert_element(5)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(25)
        self.__BST.insert_element(50)
        self.__BST.insert_element(80) 
        self.__BST.insert_element(27)
        returned = self.__BST.pre_order()
        self.assertEqual('[ 30, 20, 10, 5, 25, 27, 60, 50, 70, 80 ]', returned)


    def test_height_rotate_right_left_deep_imbalanceV3(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(10)
        self.__BST.insert_element(60)
        self.__BST.insert_element(5)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(25)
        self.__BST.insert_element(50)
        self.__BST.insert_element(80) 
        self.__BST.insert_element(40)
        self.assertEqual(4, self.__BST.get_height())

    def test_height_rotate_right_left_deep_imbalanceV3_in(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(10)
        self.__BST.insert_element(60)
        self.__BST.insert_element(5)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(25)
        self.__BST.insert_element(50)
        self.__BST.insert_element(80) 
        self.__BST.insert_element(40)
        self.assertEqual('[ 5, 10, 20, 25, 30, 40, 50, 60, 70, 80 ]', str(self.__BST))
        self.assertEqual([ 5, 10, 20, 25, 30, 40, 50, 60, 70, 80 ], self.__BST.to_list())

    def test_height_rotate_right_left_deep_imbalanceV3_post(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(10)
        self.__BST.insert_element(60)
        self.__BST.insert_element(5)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(25)
        self.__BST.insert_element(50)
        self.__BST.insert_element(80) 
        self.__BST.insert_element(40)
        returned = self.__BST.post_order()
        self.assertEqual('[ 5, 10, 25, 20, 40, 50, 80, 70, 60, 30 ]', returned)

    def test_height_rotate_right_left_deep_imbalanceV3_pre(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(10)
        self.__BST.insert_element(60)
        self.__BST.insert_element(5)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(25)
        self.__BST.insert_element(50)
        self.__BST.insert_element(80) 
        self.__BST.insert_element(40)
        returned = self.__BST.pre_order()
        self.assertEqual('[ 30, 20, 10, 5, 25, 60, 50, 40, 70, 80 ]', returned)


          
    def test_height_rotate_right_left_deep_imbalanceV4(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(10)
        self.__BST.insert_element(60)
        self.__BST.insert_element(5)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(25)
        self.__BST.insert_element(50)
        self.__BST.insert_element(80) 
        self.__BST.insert_element(55)
        self.assertEqual(4, self.__BST.get_height())

    def test_height_rotate_right_left_deep_imbalanceV4_in(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(10)
        self.__BST.insert_element(60)
        self.__BST.insert_element(5)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(25)
        self.__BST.insert_element(50)
        self.__BST.insert_element(80) 
        self.__BST.insert_element(55)
        self.assertEqual('[ 5, 10, 20, 25, 30, 50, 55, 60, 70, 80 ]', str(self.__BST))
        self.assertEqual([ 5, 10, 20, 25, 30, 50, 55, 60, 70, 80 ], self.__BST.to_list())

    def test_height_rotate_right_left_deep_imbalanceV4_post(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(10)
        self.__BST.insert_element(60)
        self.__BST.insert_element(5)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(25)
        self.__BST.insert_element(50)
        self.__BST.insert_element(80) 
        self.__BST.insert_element(55)
        returned = self.__BST.post_order()
        self.assertEqual('[ 5, 10, 25, 20, 55, 50, 80, 70, 60, 30 ]', returned)

    def test_height_rotate_right_left_deep_imbalanceV4_pre(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(10)
        self.__BST.insert_element(60)
        self.__BST.insert_element(5)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(25)
        self.__BST.insert_element(50)
        self.__BST.insert_element(80) 
        self.__BST.insert_element(55)
        returned = self.__BST.pre_order()
        self.assertEqual('[ 30, 20, 10, 5, 25, 60, 50, 55, 70, 80 ]', returned)



    def test_height_rotate_right_left_deep_imbalanceV5(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(10)
        self.__BST.insert_element(60)
        self.__BST.insert_element(5)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(25)
        self.__BST.insert_element(50)
        self.__BST.insert_element(80) 
        self.__BST.insert_element(75)
        self.assertEqual(4, self.__BST.get_height())


    def test_height_rotate_right_left_deep_imbalanceV5_in(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(10)
        self.__BST.insert_element(60)
        self.__BST.insert_element(5)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(25)
        self.__BST.insert_element(50)
        self.__BST.insert_element(80) 
        self.__BST.insert_element(75)
        self.assertEqual('[ 5, 10, 20, 25, 30, 50, 60, 70, 75, 80 ]', str(self.__BST))
        self.assertEqual([ 5, 10, 20, 25, 30, 50, 60, 70, 75, 80 ], self.__BST.to_list())

    def test_height_rotate_right_left_deep_imbalanceV5_post(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(10)
        self.__BST.insert_element(60)
        self.__BST.insert_element(5)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(25)
        self.__BST.insert_element(50)
        self.__BST.insert_element(80) 
        self.__BST.insert_element(75)
        returned = self.__BST.post_order()
        self.assertEqual('[ 5, 10, 25, 50, 30, 70, 80, 75, 60, 20 ]', returned)

    def test_height_rotate_right_left_deep_imbalanceV5_pre(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(10)
        self.__BST.insert_element(60)
        self.__BST.insert_element(5)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(25)
        self.__BST.insert_element(50)
        self.__BST.insert_element(80) 
        self.__BST.insert_element(75)
        returned = self.__BST.pre_order()
        self.assertEqual('[ 20, 10, 5, 60, 30, 25, 50, 75, 70, 80 ]', returned)

    def test_height_rotate_right_left_deep_imbalanceV6(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(10)
        self.__BST.insert_element(60)
        self.__BST.insert_element(5)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(25)
        self.__BST.insert_element(50)
        self.__BST.insert_element(80) 
        self.__BST.insert_element(90)
        self.assertEqual(4, self.__BST.get_height())
        
    def test_height_rotate_right_left_deep_imbalanceV6_in(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(10)
        self.__BST.insert_element(60)
        self.__BST.insert_element(5)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(25)
        self.__BST.insert_element(50)
        self.__BST.insert_element(80) 
        self.__BST.insert_element(90)
        self.assertEqual('[ 5, 10, 20, 25, 30, 50, 60, 70, 80, 90 ]', str(self.__BST))
        self.assertEqual([ 5, 10, 20, 25, 30, 50, 60, 70, 80, 90 ], self.__BST.to_list())

    def test_height_rotate_right_left_deep_imbalanceV6_post(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(10)
        self.__BST.insert_element(60)
        self.__BST.insert_element(5)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(25)
        self.__BST.insert_element(50)
        self.__BST.insert_element(80) 
        self.__BST.insert_element(90)
        returned = self.__BST.post_order()
        self.assertEqual('[ 5, 10, 25, 50, 30, 70, 90, 80, 60, 20 ]', returned)

    def test_height_rotate_right_left_deep_imbalanceV6_pre(self):
        self.__BST.insert_element(20)
        self.__BST.insert_element(10)
        self.__BST.insert_element(60)
        self.__BST.insert_element(5)
        self.__BST.insert_element(30)
        self.__BST.insert_element(70)
        self.__BST.insert_element(25)
        self.__BST.insert_element(50)
        self.__BST.insert_element(80) 
        self.__BST.insert_element(90)
        returned = self.__BST.pre_order()
        self.assertEqual('[ 20, 10, 5, 60, 30, 25, 50, 80, 70, 90 ]', returned)

    def test_height_rotate_left_right_deep_imbalanceV1(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(55)
        self.__BST.insert_element(20)
        self.__BST.insert_element(60)
        self.__BST.insert_element(15)
        self.__BST.insert_element(35)
        self.__BST.insert_element(10)
        self.__BST.insert_element(25)
        self.__BST.insert_element(40) 
        self.__BST.insert_element(45)
        self.assertEqual(4, self.__BST.get_height())


    def test_height_rotate_left_right_deep_imbalanceV1_in(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(55)
        self.__BST.insert_element(20)
        self.__BST.insert_element(60)
        self.__BST.insert_element(15)
        self.__BST.insert_element(35)
        self.__BST.insert_element(10)
        self.__BST.insert_element(25)
        self.__BST.insert_element(40) 
        self.__BST.insert_element(45)
        self.assertEqual('[ 10, 15, 20, 25, 35, 40, 45, 50, 55, 60 ]', str(self.__BST))
        self.assertEqual([ 10, 15, 20, 25, 35, 40, 45, 50, 55, 60 ], self.__BST.to_list())

    def test_height_rotate_left_right_deep_imbalanceV1_post(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(55)
        self.__BST.insert_element(20)
        self.__BST.insert_element(60)
        self.__BST.insert_element(15)
        self.__BST.insert_element(35)
        self.__BST.insert_element(10)
        self.__BST.insert_element(25)
        self.__BST.insert_element(40) 
        self.__BST.insert_element(45)
        returned = self.__BST.post_order()
        self.assertEqual('[ 10, 15, 25, 20, 45, 40, 60, 55, 50, 35 ]', returned)

    def test_height_rotate_left_right_deep_imbalanceV1_pre(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(55)
        self.__BST.insert_element(20)
        self.__BST.insert_element(60)
        self.__BST.insert_element(15)
        self.__BST.insert_element(35)
        self.__BST.insert_element(10)
        self.__BST.insert_element(25)
        self.__BST.insert_element(40) 
        self.__BST.insert_element(45)
        returned = self.__BST.pre_order()
        self.assertEqual('[ 35, 20, 15, 10, 25, 50, 40, 45, 55, 60 ]', returned)

    def test_height_rotate_left_right_deep_imbalanceV2(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(55)
        self.__BST.insert_element(20)
        self.__BST.insert_element(60)
        self.__BST.insert_element(15)
        self.__BST.insert_element(35)
        self.__BST.insert_element(10)
        self.__BST.insert_element(25)
        self.__BST.insert_element(40) 
        self.__BST.insert_element(43)
        self.assertEqual(4, self.__BST.get_height()) 

    def test_height_rotate_left_right_deep_imbalanceV2_in(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(55)
        self.__BST.insert_element(20)
        self.__BST.insert_element(60)
        self.__BST.insert_element(15)
        self.__BST.insert_element(35)
        self.__BST.insert_element(10)
        self.__BST.insert_element(25)
        self.__BST.insert_element(40) 
        self.__BST.insert_element(43)
        self.assertEqual('[ 10, 15, 20, 25, 35, 40, 43, 50, 55, 60 ]', str(self.__BST))
        self.assertEqual([ 10, 15, 20, 25, 35, 40, 43, 50, 55, 60 ], self.__BST.to_list())

    def test_height_rotate_left_right_deep_imbalanceV2_post(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(55)
        self.__BST.insert_element(20)
        self.__BST.insert_element(60)
        self.__BST.insert_element(15)
        self.__BST.insert_element(35)
        self.__BST.insert_element(10)
        self.__BST.insert_element(25)
        self.__BST.insert_element(40) 
        self.__BST.insert_element(43)
        returned = self.__BST.post_order()
        self.assertEqual('[ 10, 15, 25, 20, 43, 40, 60, 55, 50, 35 ]', returned)

    def test_height_rotate_left_right_deep_imbalanceV2_pre(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(55)
        self.__BST.insert_element(20)
        self.__BST.insert_element(60)
        self.__BST.insert_element(15)
        self.__BST.insert_element(35)
        self.__BST.insert_element(10)
        self.__BST.insert_element(25)
        self.__BST.insert_element(40) 
        self.__BST.insert_element(43)
        returned = self.__BST.pre_order()
        self.assertEqual('[ 35, 20, 15, 10, 25, 50, 40, 43, 55, 60 ]', returned)

    def test_height_rotate_left_right_deep_imbalanceV3(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(55)
        self.__BST.insert_element(20)
        self.__BST.insert_element(60)
        self.__BST.insert_element(15)
        self.__BST.insert_element(35)
        self.__BST.insert_element(10)
        self.__BST.insert_element(25)
        self.__BST.insert_element(40) 
        self.__BST.insert_element(27)
        self.assertEqual(4, self.__BST.get_height())

    def test_height_rotate_left_right_deep_imbalanceV3_in(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(55)
        self.__BST.insert_element(20)
        self.__BST.insert_element(60)
        self.__BST.insert_element(15)
        self.__BST.insert_element(35)
        self.__BST.insert_element(10)
        self.__BST.insert_element(25)
        self.__BST.insert_element(40) 
        self.__BST.insert_element(27)
        self.assertEqual('[ 10, 15, 20, 25, 27, 35, 40, 50, 55, 60 ]', str(self.__BST))
        self.assertEqual([ 10, 15, 20, 25, 27, 35, 40, 50, 55, 60 ], self.__BST.to_list())

    def test_height_rotate_left_right_deep_imbalanceV3_post(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(55)
        self.__BST.insert_element(20)
        self.__BST.insert_element(60)
        self.__BST.insert_element(15)
        self.__BST.insert_element(35)
        self.__BST.insert_element(10)
        self.__BST.insert_element(25)
        self.__BST.insert_element(40) 
        self.__BST.insert_element(27)
        returned = self.__BST.post_order()
        self.assertEqual('[ 10, 15, 27, 25, 20, 40, 60, 55, 50, 35 ]', returned)

    def test_height_rotate_left_right_deep_imbalanceV3_pre(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(55)
        self.__BST.insert_element(20)
        self.__BST.insert_element(60)
        self.__BST.insert_element(15)
        self.__BST.insert_element(35)
        self.__BST.insert_element(10)
        self.__BST.insert_element(25)
        self.__BST.insert_element(40) 
        self.__BST.insert_element(27)
        returned = self.__BST.pre_order()
        self.assertEqual('[ 35, 20, 15, 10, 25, 27, 50, 40, 55, 60 ]', returned)


    def test_height_rotate_left_right_deep_imbalanceV4(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(55)
        self.__BST.insert_element(20)
        self.__BST.insert_element(60)
        self.__BST.insert_element(15)
        self.__BST.insert_element(35)
        self.__BST.insert_element(10)
        self.__BST.insert_element(25)
        self.__BST.insert_element(40) 
        self.__BST.insert_element(23)
        self.assertEqual(4, self.__BST.get_height()) 

    def test_height_rotate_left_right_deep_imbalanceV4_in(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(55)
        self.__BST.insert_element(20)
        self.__BST.insert_element(60)
        self.__BST.insert_element(15)
        self.__BST.insert_element(35)
        self.__BST.insert_element(10)
        self.__BST.insert_element(25)
        self.__BST.insert_element(40) 
        self.__BST.insert_element(23)
        self.assertEqual('[ 10, 15, 20, 23, 25, 35, 40, 50, 55, 60 ]', str(self.__BST)) 
        self.assertEqual([ 10, 15, 20, 23, 25, 35, 40, 50, 55, 60 ], self.__BST.to_list()) 

    def test_height_rotate_left_right_deep_imbalanceV4_post(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(55)
        self.__BST.insert_element(20)
        self.__BST.insert_element(60)
        self.__BST.insert_element(15)
        self.__BST.insert_element(35)
        self.__BST.insert_element(10)
        self.__BST.insert_element(25)
        self.__BST.insert_element(40) 
        self.__BST.insert_element(23)
        returned = self.__BST.post_order()
        self.assertEqual('[ 10, 15, 23, 25, 20, 40, 60, 55, 50, 35 ]', returned) 

    def test_height_rotate_left_right_deep_imbalanceV4_pre(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(55)
        self.__BST.insert_element(20)
        self.__BST.insert_element(60)
        self.__BST.insert_element(15)
        self.__BST.insert_element(35)
        self.__BST.insert_element(10)
        self.__BST.insert_element(25)
        self.__BST.insert_element(40) 
        self.__BST.insert_element(23)
        returned = self.__BST.pre_order()
        self.assertEqual('[ 35, 20, 15, 10, 25, 23, 50, 40, 55, 60 ]', returned) 


    def test_height_rotate_left_right_deep_imbalanceV5(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(55)
        self.__BST.insert_element(20)
        self.__BST.insert_element(60)
        self.__BST.insert_element(15)
        self.__BST.insert_element(35)
        self.__BST.insert_element(10)
        self.__BST.insert_element(25)
        self.__BST.insert_element(40) 
        self.__BST.insert_element(12)
        self.assertEqual(4, self.__BST.get_height()) 

    def test_height_rotate_left_right_deep_imbalanceV5_in(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(55)
        self.__BST.insert_element(20)
        self.__BST.insert_element(60)
        self.__BST.insert_element(15)
        self.__BST.insert_element(35)
        self.__BST.insert_element(10)
        self.__BST.insert_element(25)
        self.__BST.insert_element(40) 
        self.__BST.insert_element(12)
        self.assertEqual('[ 10, 12, 15, 20, 25, 35, 40, 50, 55, 60 ]', str(self.__BST)) 
        self.assertEqual([ 10, 12, 15, 20, 25, 35, 40, 50, 55, 60 ], self.__BST.to_list()) 
    
    def test_height_rotate_left_right_deep_imbalanceV5_post(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(55)
        self.__BST.insert_element(20)
        self.__BST.insert_element(60)
        self.__BST.insert_element(15)
        self.__BST.insert_element(35)
        self.__BST.insert_element(10)
        self.__BST.insert_element(25)
        self.__BST.insert_element(40) 
        self.__BST.insert_element(12)
        returned = self.__BST.post_order()
        self.assertEqual('[ 10, 15, 12, 25, 40, 35, 20, 60, 55, 50 ]', returned) 


    def test_height_rotate_left_right_deep_imbalanceV5_pre(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(55)
        self.__BST.insert_element(20)
        self.__BST.insert_element(60)
        self.__BST.insert_element(15)
        self.__BST.insert_element(35)
        self.__BST.insert_element(10)
        self.__BST.insert_element(25)
        self.__BST.insert_element(40) 
        self.__BST.insert_element(12)
        returned = self.__BST.pre_order()
        self.assertEqual('[ 50, 20, 12, 10, 15, 35, 25, 40, 55, 60 ]', returned) 


    def test_height_rotate_left_right_deep_imbalanceV6(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(55)
        self.__BST.insert_element(20)
        self.__BST.insert_element(60)
        self.__BST.insert_element(15)
        self.__BST.insert_element(35)
        self.__BST.insert_element(10)
        self.__BST.insert_element(25)
        self.__BST.insert_element(40) 
        self.__BST.insert_element(5)
        self.assertEqual(4, self.__BST.get_height()) 

    def test_height_rotate_left_right_deep_imbalanceV6_in(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(55)
        self.__BST.insert_element(20)
        self.__BST.insert_element(60)
        self.__BST.insert_element(15)
        self.__BST.insert_element(35)
        self.__BST.insert_element(10)
        self.__BST.insert_element(25)
        self.__BST.insert_element(40) 
        self.__BST.insert_element(5)
        self.assertEqual('[ 5, 10, 15, 20, 25, 35, 40, 50, 55, 60 ]', str(self.__BST)) 
        self.assertEqual([ 5, 10, 15, 20, 25, 35, 40, 50, 55, 60 ], self.__BST.to_list())
    
    def test_height_rotate_left_right_deep_imbalanceV6_post(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(55)
        self.__BST.insert_element(20)
        self.__BST.insert_element(60)
        self.__BST.insert_element(15)
        self.__BST.insert_element(35)
        self.__BST.insert_element(10)
        self.__BST.insert_element(25)
        self.__BST.insert_element(40) 
        self.__BST.insert_element(5)
        returned = self.__BST.post_order()
        self.assertEqual('[ 5, 15, 10, 25, 40, 35, 20, 60, 55, 50 ]', returned) 

    def test_height_rotate_left_right_deep_imbalanceV6_pre(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(55)
        self.__BST.insert_element(20)
        self.__BST.insert_element(60)
        self.__BST.insert_element(15)
        self.__BST.insert_element(35)
        self.__BST.insert_element(10)
        self.__BST.insert_element(25)
        self.__BST.insert_element(40) 
        self.__BST.insert_element(5)
        returned = self.__BST.pre_order()
        self.assertEqual('[ 50, 20, 10, 5, 15, 35, 25, 40, 55, 60 ]', returned) 

    def test_height_rotate_left_right_deep_imbalance_in_after_first_rotate(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(55)
        self.__BST.insert_element(20)
        self.__BST.insert_element(60)
        self.__BST.insert_element(15)
        self.__BST.insert_element(35)
        self.__BST.insert_element(10)
        self.__BST.insert_element(25)
        self.__BST.insert_element(40) 
        self.__BST.insert_element(5)
        post = self.__BST.post_order()
        pre = self.__BST.pre_order()
        self.assertEqual('[ 5, 10, 15, 20, 25, 35, 40, 50, 55, 60 ]', str(self.__BST)) 
        self.assertEqual([ 5, 10, 15, 20, 25, 35, 40, 50, 55, 60 ], self.__BST.to_list()) 
        self.assertEqual('[ 5, 15, 10, 25, 40, 35, 20, 60, 55, 50 ]', post) 
        self.assertEqual('[ 50, 20, 10, 5, 15, 35, 25, 40, 55, 60 ]', pre) 
        self.__BST.insert_element(4)
        post = self.__BST.post_order()
        pre = self.__BST.pre_order()
        self.assertEqual('[ 4, 5, 10, 15, 20, 25, 35, 40, 50, 55, 60 ]', str(self.__BST))
        self.assertEqual([ 4, 5, 10, 15, 20, 25, 35, 40, 50, 55, 60 ], self.__BST.to_list())
        self.assertEqual('[ 4, 5, 15, 10, 25, 40, 35, 60, 55, 50, 20 ]', post)
        self.assertEqual('[ 20, 10, 5, 4, 15, 50, 35, 25, 40, 55, 60 ]', pre)



#REMOVAL



    def test_height_single_rotation_right_at_root(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(60)
        self.__BST.insert_element(40)
        self.__BST.insert_element(70)
        self.__BST.remove_element(40)
        self.assertEqual(2, self.__BST.get_height()) 

    def test_height_single_rotation_right_at_root_in(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(60)
        self.__BST.insert_element(40)
        self.__BST.insert_element(70)
        self.__BST.remove_element(40)
        self.assertEqual('[ 50, 60, 70 ]', str(self.__BST)) 
        self.assertEqual([ 50, 60, 70 ], self.__BST.to_list()) 

    def test_height_single_rotation_right_at_root_post(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(60)
        self.__BST.insert_element(40)
        self.__BST.insert_element(70)
        self.__BST.remove_element(40)
        returned = self.__BST.post_order()
        self.assertEqual('[ 50, 70, 60 ]', returned) 

    def test_height_single_rotation_right_at_root_pre(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(60)
        self.__BST.insert_element(40)
        self.__BST.insert_element(70)
        self.__BST.remove_element(40)
        returned = self.__BST.pre_order()
        self.assertEqual('[ 60, 50, 70 ]', returned) 


    def test_height_single_rotation_left_at_root(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(60)
        self.__BST.insert_element(40)
        self.__BST.insert_element(30)
        self.__BST.remove_element(60)
        self.assertEqual(2, self.__BST.get_height()) 

    def test_single_rotation_right_at_root_floater_in_order_in_order(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(60)
        self.__BST.insert_element(40)
        self.__BST.insert_element(70)
        self.__BST.insert_element(55)
        self.__BST.remove_element(40)
        self.assertEqual('[ 50, 55, 60, 70 ]', str(self.__BST))
        self.assertEqual([ 50, 55, 60, 70 ], self.__BST.to_list())

    def test_single_rotation_right_at_root_floater_post_order(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(60)
        self.__BST.insert_element(40)
        self.__BST.insert_element(70)
        self.__BST.insert_element(55)
        self.__BST.remove_element(40)
        returned = self.__BST.post_order()
        self.assertEqual('[ 55, 50, 70, 60 ]', returned)

    def test_single_rotation_right_at_root_floater_pre_order(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(60)
        self.__BST.insert_element(40)
        self.__BST.insert_element(70)
        self.__BST.insert_element(55)
        self.__BST.remove_element(40)
        returned = self.__BST.pre_order()
        self.assertEqual('[ 60, 50, 55, 70 ]', returned)

    def test_right_left_rotate_remv(self):
        self.__BST.insert_element(25)
        self.__BST.insert_element(30)
        self.__BST.insert_element(31)
        self.__BST.insert_element(50)
        self.__BST.insert_element(45)
        self.__BST.insert_element(55)
        self.__BST.insert_element(34)
        self.__BST.remove_element(50)
        returned = self.__BST.to_list()
        self.assertEqual(3, self.__BST.get_height())
        self.assertEqual('[ 25, 30, 31, 34, 45, 55 ]', str(self.__BST))
        self.assertEqual([ 25, 30, 31, 34, 45, 55 ], returned)
        self.assertEqual('[ 25, 30, 34, 55, 45, 31 ]', self.__BST.post_order())
        self.assertEqual('[ 31, 30, 25, 45, 34, 55 ]', self.__BST.pre_order())

    def test_left_right_rotate_remv(self):
        self.__BST.insert_element(45)
        self.__BST.insert_element(40)
        self.__BST.insert_element(50)
        self.__BST.insert_element(38)
        self.__BST.insert_element(55)
        self.__BST.insert_element(49)
        self.__BST.insert_element(48)
        self.__BST.remove_element(38)
        returned = self.__BST.to_list()
        self.assertEqual(3, self.__BST.get_height())
        self.assertEqual('[ 40, 45, 48, 49, 50, 55 ]', str(self.__BST))
        self.assertEqual([ 40, 45, 48, 49, 50, 55 ], returned)
        self.assertEqual('[ 40, 48, 45, 55, 50, 49 ]', self.__BST.post_order())
        self.assertEqual('[ 49, 45, 40, 48, 50, 55 ]', self.__BST.pre_order())  

    def test_two_separate_rotates_both_single(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(40)
        self.__BST.insert_element(60)
        self.__BST.insert_element(35)
        self.__BST.insert_element(45)
        self.__BST.insert_element(58)
        self.__BST.insert_element(65)
        self.__BST.insert_element(30)
        self.__BST.insert_element(37)
        self.__BST.insert_element(42)
        self.__BST.insert_element(67)
        self.__BST.insert_element(23)
        self.__BST.remove_element(58)
        returned = self.__BST.to_list()
        self.assertEqual(4, self.__BST.get_height())
        self.assertEqual('[ 23, 30, 35, 37, 40, 42, 45, 50, 60, 65, 67 ]', str(self.__BST))
        self.assertEqual([ 23, 30, 35, 37, 40, 42, 45, 50, 60, 65, 67 ], returned)
        self.assertEqual('[ 23, 30, 37, 35, 42, 45, 60, 67, 65, 50, 40 ]', self.__BST.post_order())
        self.assertEqual('[ 40, 35, 30, 23, 37, 50, 45, 42, 65, 60, 67 ]', self.__BST.pre_order())     

    def test_two_separate_rotates_double_single(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(40)
        self.__BST.insert_element(60)
        self.__BST.insert_element(35)
        self.__BST.insert_element(45)
        self.__BST.insert_element(58)
        self.__BST.insert_element(65)
        self.__BST.insert_element(30)
        self.__BST.insert_element(37)
        self.__BST.insert_element(42)
        self.__BST.insert_element(63)
        self.__BST.insert_element(23)
        self.__BST.remove_element(58)
        returned = self.__BST.to_list()
        self.assertEqual(4, self.__BST.get_height())
        self.assertEqual('[ 23, 30, 35, 37, 40, 42, 45, 50, 60, 63, 65 ]', str(self.__BST))
        self.assertEqual([ 23, 30, 35, 37, 40, 42, 45, 50, 60, 63, 65 ], returned)
        self.assertEqual('[ 23, 30, 37, 35, 42, 45, 60, 65, 63, 50, 40 ]', self.__BST.post_order())
        self.assertEqual('[ 40, 35, 30, 23, 37, 50, 45, 42, 63, 60, 65 ]', self.__BST.pre_order()) 


    def test_two_separate_rotates_single_double(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(40)
        self.__BST.insert_element(60)
        self.__BST.insert_element(35)
        self.__BST.insert_element(45)
        self.__BST.insert_element(58)
        self.__BST.insert_element(65)
        self.__BST.insert_element(30)
        self.__BST.insert_element(42)
        self.__BST.insert_element(47)
        self.__BST.insert_element(67)
        self.__BST.insert_element(48)
        self.__BST.remove_element(58)
        returned = self.__BST.to_list()
        self.assertEqual(4, self.__BST.get_height())
        self.assertEqual('[ 30, 35, 40, 42, 45, 47, 48, 50, 60, 65, 67 ]', str(self.__BST))
        self.assertEqual([ 30, 35, 40, 42, 45, 47, 48, 50, 60, 65, 67 ], returned)
        self.assertEqual('[ 30, 35, 42, 40, 48, 47, 60, 67, 65, 50, 45 ]', self.__BST.post_order())
        self.assertEqual('[ 45, 40, 35, 30, 42, 50, 47, 48, 65, 60, 67 ]', self.__BST.pre_order()) 


    def test_two_separate_rotates_double_double(self):
        self.__BST.insert_element(50)
        self.__BST.insert_element(40)
        self.__BST.insert_element(60)
        self.__BST.insert_element(35)
        self.__BST.insert_element(45)
        self.__BST.insert_element(58)
        self.__BST.insert_element(65)
        self.__BST.insert_element(30)
        self.__BST.insert_element(42)
        self.__BST.insert_element(47)
        self.__BST.insert_element(63)
        self.__BST.insert_element(48)
        self.__BST.remove_element(58)
        returned = self.__BST.to_list()
        self.assertEqual(4, self.__BST.get_height())
        self.assertEqual('[ 30, 35, 40, 42, 45, 47, 48, 50, 60, 63, 65 ]', str(self.__BST))
        self.assertEqual([ 30, 35, 40, 42, 45, 47, 48, 50, 60, 63, 65 ], returned)
        self.assertEqual('[ 30, 35, 42, 40, 48, 47, 60, 65, 63, 50, 45 ]', self.__BST.post_order())
        self.assertEqual('[ 45, 40, 35, 30, 42, 50, 47, 48, 63, 60, 65 ]', self.__BST.pre_order())             




        
    

    

    

    
        




if __name__ == '__main__':
  unittest.main()

    