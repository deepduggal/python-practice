"""
 Deep's Linked List Implementation in Python
  - Node
  - Singly
  - Doubly

  a -> b -> c
"""

class LLNode:
  def __init__(self, value):
    self.value = value
    self.next = None

class SinglyLinkedList:
  def __init__(self):
    self.head: None
    self.nodes = set()

  def __len__(self):
    return len(self.nodes)

  def is_empty(self): 
    return len(self) == 0
    # return self.head == None

  def print(self):
    if self.is_empty():
      return None
    
    result_string = str(self.head.value)
    n = self.head
    while(n.next != None):
      result_string = result_string.join(n.next.value, ' -> ')
    return result_string

  def tail(self):
    if self.is_empty():
      return None
    # @TODO
    

  def add(self, value):
    node = LLNode(value)

    if self.is_empty():
      self.head = node

    self.nodes.add(node)


  def remove(self):
    pass