"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # take the current value of our node (self.value)    
        # compare to the new value we want to insert
        # if new value < self.value
            # IF self.left is already taken by a node
                # make that (left) node, call insert 
            # set the left to the new node with the new value
        if self is None:
            root = value
        else:
            if self.value < value:
                if self.right is None:
                    self.right = value
                else:
                    insert(self.right, value)
        # if new value >= self.value
            # IF self.right is already taken by a node
                # make that (right) node call insert 
            # set the right child to the new node with new value
            else:
                if self.left is None:
                    self.left = value
                else:
                    insert(self.left, value)
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        # compare the target to current value
        # if current value < target
        found = False
        if self.value < target:
            # check the left subtree (self.left.contains(target))
            # if you cannot go left, return False
            if self.left is None:
                return False
            found = self.left.contains(target)
        # if current value >= target
        if self.value >= target:
            # check if right subtree contains target
            # if you cannot go right, return False
            if self.right is None:
                return False
            found = self.right.contains(target)
            return found
    # Return the maximum value found in the tree
    def get_max(self):
        if (self == None):
            return float('-inf')
        res = self.value
        lres = get_max(self.left)
        rres = get_max(self.right)
        if (lres > res):
            res = lres
        if (rres > res):
            res = rres
        return res

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        if self.left is None:
            return None
        if self.right is None:
            return None
        

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
