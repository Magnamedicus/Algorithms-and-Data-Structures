class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self,value = None):
        if value:
            new_node = Node(value)
            self.root = new_node
        else:
            self.root = None

#The Binary Search Tree organizes node in as parent nodes with each parent having a maximum of two child nodes
#Each child node is organized on either the left or the right of its parent based on whether its magnitude is
#greater or less than its parent. A child will be on the right if greater than its parent and on the left if less than

#The initial pointer for a tree is 'self.root', this is analagous to self.head in a linked list or self.top in a stack
#self.root will point to the first node from which all other nodes derive
#The constructor above creates a new BST with a root, which will either be set equal to a node if a value is entered
#or be set to None if choosing to create an empty tree.

