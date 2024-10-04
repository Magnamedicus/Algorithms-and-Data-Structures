
#Below are class definitions for a Node, Queue, and Binary Search Tree. A custom queue is defined for use
#in the breadth first traversal method. The BST class includes methods for traversing in breadth first as well as
#depth first (preorder, postorder, and in-order). There are also methods for inserting, scanning and reversing the tree

#below the class definitions is an instantiation of the BST for testing purposes.




class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.left = None
        self.right = None

class Queue:
    def __init__(self,node = None):
        if node:
            self.first = node
            self.last = node
            self.length = 1
        else:
            self.first = None
            self.last = None
            self.length = 0

    def enqueue(self, node):

        if self.first is None:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self.length +=1
        return True

    def dequeue(self):
        temp = self.first
        self.first = self.first.next
        temp.next = None
        self.length -=1
        return temp


class BinarySearchTree:
    def __init__(self,value = None):
        if value:
            new_node = Node(value)
            self.root = new_node
        else:
            self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            temp = self.root
            while True:
                if new_node.value == temp.value:
                    print("this node already exists in the tree")
                    return False
                elif new_node.value < temp.value:
                    if temp.left is None:
                        temp.left = new_node
                        return True
                    temp = temp.left
                elif new_node.value > temp.value:
                    if temp.right is None:
                        temp.right = new_node
                        return True
                    temp = temp.right

    def contains(self,value):
        if self.root is None:
            print("This tree contains no nodes.")
            return False
        else:
            temp = self.root
            while temp:
                if temp.value == value:
                    return True
                elif value < temp.value:
                    temp = temp.left
                elif value > temp.value:
                    temp = temp.right
            return False

    def breadth_first_traversal(self):
        if self.root is None:
            print("This tree contains no nodes")
            return False
        else:
            queue = Queue(self.root)
            results = []

            while queue.length > 0:
                current_node = queue.dequeue()
                results.append(current_node.value)
                if current_node.left:
                    queue.enqueue(current_node.left)
                if current_node.right:
                    queue.enqueue(current_node.right)

            return results

    def depth_first_traversal_preOrder(self):
        if self.root is None:
            print("This tree contains no nodes")
            return False
        else:
            results = []
            def traverse(current_node):
                results.append(current_node.value)
                if current_node.left:
                    traverse(current_node.left)
                if current_node.right:
                    traverse(current_node.right)
            traverse(self.root)
            return results

    def depth_first_traversal_postOrder(self):
        if self.root is None:
            print("This tree contains no nodes")
            return False
        else:
            results = []
            def traverse(current_node):
                if current_node.left:
                    traverse(current_node.left)
                if current_node.right:
                    traverse(current_node.right)
                results.append(current_node.value)
            traverse(self.root)
            return results

    def depth_first_traversal_inOrder(self):
        if self.root is None:
            print("This tree contains no nodes")
            return False
        else:
            results = []
            def traverse(current_node):
                if current_node.left:
                    traverse(current_node.left)
                results.append(current_node.value)
                if current_node.right:
                    traverse(current_node.right)
            traverse(self.root)
            return results

    def tree_reversal(self):

        if self.root is None:
            print("This tree contains no nodes")
            return False

        def reverse(current_node):
            current_node.left,current_node.right = current_node.right,current_node.left
            if current_node.left:
                reverse(current_node.left)
            if current_node.right:
                reverse(current_node.right)
        reverse(self.root)
        return True






nums = [61,32,43,12,67,80,14,10,72,70,1,15]
my_BST = BinarySearchTree()

for num in nums:
    my_BST.insert(num)

print(my_BST.tree_reversal())

print(my_BST.depth_first_traversal_inOrder())
