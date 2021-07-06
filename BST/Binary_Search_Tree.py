class Binary_Search_Tree:

  class __BST_Node:

    def __init__(self, value):
      self.value = value                        #each node will have a value attribute which is the value that the user passes when inserting a value      
      self.right_child = None                   #each node will have a right_chid attribute initialized as None
      self.left_child = None                    #each node will have a left_child attribute initialized as None
      self.height = 1                           #each node will have a height attribute initialized at 1

  def __init__(self):
    self.__root = None                          #the root is the only attribute we initialize for the BST as it links to all other subroots; initialize as None
  

  def __rotate(self, t, direction):
    if direction == 'left':                     #if parameter is left
        upd_root = t.right_child                #new root is t's right child
        t.right_child = upd_root.left_child     #t's right child will be roots left child (floater)
        upd_root.left_child = t                 #upd root's left child is now t
        self.__update_height(t)                 #update height
        self.__update_height(upd_root)          #update height
    else:                                       #if left is not parameter, must be right rotate
        upd_root = t.left_child                 #new root is t's left child
        t.left_child = upd_root.right_child     #t's left child will be roots right child (floater)
        upd_root.right_child = t                #t will now be upd root's right child
        self.__update_height(t)                 #update height
        self.__update_height(upd_root)          #update height
    return upd_root



  def __balanced(self, t):
    if t is None:
        return t
    if self.__the_balance_of(t) > 1:                                                                                        #if we're right heavy by more than 1
        if self.__the_balance_of(t.right_child) == 1 or self.__the_balance_of(t.right_child) == 0:                          #If t's right child is right-heavy by 1 or balanced at 0
            t = self.__rotate(t, 'left')                                                                                    #rotate left about t 
            self.__update_height(t)
            return t                                                                                                        #return the new root
        elif self.__the_balance_of(t.right_child) == -1:                                                                    #If t's right child is left-heavy by 1
            t.right_child = self.__rotate(t.right_child, 'right')                                                           #rotate right about t's right child,
            t = self.__rotate(t, 'left')                                                                                    #then rotate left about t 
            self.__update_height(t)
            return t                                                                                                        #and return the new root.
    elif self.__the_balance_of(t) < -1:                                                                                     #if we're left heavy by more than 1
        if self.__the_balance_of(t.left_child) == -1 or self.__the_balance_of(t.left_child) == 0:                           #If t's left child is left-heavy by 1 or balanced at 0, rotate right about t and return the new root.
            t = self.__rotate(t, 'right')                                                                                   #rotate right about t 
            self.__update_height(t)
            return t                                                                                                        #return the new root
        elif self.__the_balance_of(t.left_child) == 1:                                                                      #If t's left child is right-heavy by 1,
            t.left_child = self.__rotate(t.left_child, 'left')                                                              #rotate left about t's left child,
            t = self.__rotate(t, 'right')                                                                                   #then rotate right about 
            self.__update_height(t)
            return t                                                                                                        #return the new root.  
    self.__update_height(t)                                                                                                 #update height - for when we don't hit the conditionals to rotate                           
    return t


  def __the_balance_of(self, t):
    if t is None:                                           #if t itself is None than it's balance is zero 
        return 0
    if t.left_child is None and t.right_child is None:    #if both of t's chidren are None than t must have a balance of zero
        return 0 
    elif t.left_child is None and t.right_child is not None:
        return abs(t.right_child.height)                      
    elif t.right_child is None and t.left_child is not None:                         #if right child is none
            return -t.left_child.height                        
    else:                                                   #if both children are not none
        return t.right_child.height - t.left_child.height   #just take the difference of their heights

  def __update_height(self, t):
    if t.right_child is None and t.left_child is None:                  #UPDATE HEIGHT: if both the children of the Node we're standing on are None
        t.height = 1                                                    #Height does not change
    elif t.right_child is None and t.left_child is not None:            #if the right_child is None and the left_child is not
        t.height = t.left_child.height + 1                              #add the height of the left child
    elif t.right_child is not None and t.left_child is None:            #if the left_child is None and the right_child is not
        t.height = t.right_child.height + 1                             #add the height of the right child
    else:                                                               #must mean both children are not None
        if t.right_child.height > t.left_child.height:                  #if the right_child's height is greater
            t.height = t.right_child.height + 1                         #add it's height
        else:                                                           #must mean the left_child's height is greater
            t.height = t.left_child.height + 1                          #add it's height 


  def __insert_rec(self, value, t):                         #PRIVATE INSERTION METHOD
    if t is None:                                           #BASE CASE: when we get to a place where t is None, we must be standing on a leaf
        return Binary_Search_Tree.__BST_Node(value)         #create a Node for insertion that returns to the parent to link
    else:
        if value == t.value:                                #RECURSIVE CASE: if we arrive at a duplicate value, raise a ValueError
          raise ValueError
        elif value > t.value:                                           #if the value passed in by the user is greater than the value of the Node we're standing on
            t.right_child = self.__insert_rec(value, t.right_child)     #continue to the right_child of the Node we're standing on
        elif value < t.value:                                           #if the value passed in by the user is less than the value of the Node we're standing on
            t.left_child = self.__insert_rec(value, t.left_child)       #continue to the left_child of the Node we're standing on 
    return self.__balanced(t)

  
  def insert_element(self, value):                                      #PUBLIC INSERTION METHOD: 
      self.__root = self.__insert_rec(value, self.__root)               #Call private recusrive method 
      

  def __remove_rec(self, value, t):                                     #PRIVATE REMOVAL METHOD:
    if t is None:                                                       #If we go through the Node path to find that we're trying to remove a Node that is not in the BST
      raise ValueError                                                  #Raise ValueError
    elif t.value == value:                                              #BASE CASE: If we get to the value we want to remove
        if t.left_child is None and t.right_child is None:              #If the node has zero children (a leaf node)
            return None                                                 #simply remove it from the tree
        elif t.left_child is not None and t.right_child is None or t.right_child is not None and t.left_child is None: #If the node has one child, regardless of the direction
            if t.left_child is not None:
                return t.left_child                                     #that child (subtree) takes the place of the removed node. 
            else:
                return t.right_child
        else:                                                           #If the node has two children, replace its value with the minimum value from the right subtree, then remove that now duplicated minimum value from the right subtree
            current = t.right_child                                     #have current be the right child of the node we want to remove
            while current.left_child is not None:                       #find the minimum value on this right subtree of the node we want to remove
                current = current.left_child
            t.value = current.value                                                 #copy that value onto the value we want to remove
            t.right_child = self.__remove_rec(current.value, t.right_child)         #remove the value we found that we copied
            return t                                                                #link parents to children                                                                                                                            
    else:                                                                           #RECURSIVE CASES
        if value > t.value:                                                         #if value passed in is greater than the value of the node we're standing on
            t.right_child = self.__remove_rec(value, t.right_child)                 #continue to the right of that node
        elif value < t.value:                                                       #if the value passed in is less than the value of the node we're standing on
            t.left_child = self.__remove_rec(value, t.left_child)                   #continue to the left of that node
    return self.__balanced(t)                                                       #link parents to children on the way back up


  def remove_element(self, value):                                      #PUBLIC REMOVAL METHOD
    self.__root = self.__remove_rec(value, self.__root)                 #call private recursive method 










#IN ORDER TRAVERSAL
  def __in_order_rec(self, t):                                          #PRIVATE IN ORDER METHOD
    if t is None:                                                       #BASE CASE: if we're standing on None
        return ''                                                       #append an empty string
    else:                                                               #RECURSIVE CASE: 
        left = self.__in_order_rec(t.left_child)                        #get the value of the left child
        right = self.__in_order_rec(t.right_child)                      #get the value of the right child
        return  str(left) + ', ' + str(t.value) + str(right)            #return the concatenation of the left value, the parent, then the right value in that order

  def in_order(self):                                                   #PUBLIC IN ORDER METHOD
    to_process = self.__in_order_rec(self.__root)                       #Call private method
    result = '[' + to_process[1:] + ' ]'                                #slice string for correct formatting
    return result                                                       #return the string to the user


#POST ORDER TRAVERSAL
  def __post_order_rec(self, t):                                        #PRIVATE POST ORDER METHOD
    if t is None:                                                       #BASE CASE: if we're standing on None
        return ''                                                       #append an empty string
    else:                                                               #RECURSIVE CASE
        left = self.__post_order_rec(t.left_child)                      #get the value of the left child
        right = self.__post_order_rec(t.right_child)                    #get the value of the right child
        return  str(left) + str(right) + ', ' + str(t.value)            #return the concatenation of the left value, the right value, then the parent in that order

  def post_order(self):                                                 #PUBLIC METHOD POST ORDER
    to_process = self.__post_order_rec(self.__root)                     #call private method
    result = '[' + to_process[1:] + ' ]'                                #slice string for correct formatting
    return result                                                       #return the string to the user

#PRE ORDER TRAVERSAL
  def __pre_order_rec(self, t):                                         #PRIVATE PRE ORDER METHOD
    if t is None:                                                       #BASE CASE: if we're standing on None
        return ''                                                       #append an empty string
    else:                                                               #RECURSIVE CASE
        left = self.__pre_order_rec(t.left_child)                       #get the value of the left child
        right = self.__pre_order_rec(t.right_child)                     #get the value of the right child
        return  str(t.value) + ', ' + str(left) + str(right)            #return the concatenation of the parent, the left value, then the right value in that order
  
  def pre_order(self):                                                  #PUBLIC METHOD PRE ORDER                                                                   
    to_process = self.__pre_order_rec(self.__root)                      #call private method                   
    if to_process == '':                                                #if tree is empty
        return '[ ]'                                                    #return empty brackets
    result = '[ ' + to_process[0:len(to_process)-2] + ' ]'              #slice string for correct formatting
    return result                                                       #return the string to the user


  def __to_list_rec(self, t):
    if t is None:                                                       #if t is none
        return []                                                       #return empty list
    else:                                                              
        left = self.__to_list_rec(t.left_child)                         #recur to the left    
        right = self.__to_list_rec(t.right_child)                       #recur to right       
        return left + [t.value] + right                                 #in-order



  def to_list(self):
    to_process = self.__to_list_rec(self.__root)
    return to_process


  def get_height(self):                         #Get the height of the entire BST
    if self.__root is None:                     #if our primary root is None, then there are no nodes in the tree thus the height is zero
        return 0                                #thus the height is zero
    else:                                       #if there are nodes in the subtree
        return self.__root.height               #return the height of the root, which has been udpated in insertion to match the height of the entire BST


  def __str__(self):                            #string representation 
    return self.in_order()                      #return default in order representation of the values




#if __name__ == "__main__":





