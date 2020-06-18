"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

class Node:
  def __init__(self, value=None, next_node=None):
    self.value = value
    self.next_node = next_node
  
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
        self.head = None
        self.tail = None
    
    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        

    def dequeue(self):
        pass
