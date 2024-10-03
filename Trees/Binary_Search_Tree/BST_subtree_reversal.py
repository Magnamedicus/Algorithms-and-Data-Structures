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
            self.first, self.last = node,node
        else:
            self.last.next = node
            self.last = node
        self.length +=1
        return True

    def dequeue(self):
         if self.first is None:
             print("this queue contains no nodes")
             return None
         else:
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

    def insert(self,value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            temp = self.root

            while True:
                if new_node.value == temp.value:
                    print("This value already exists in the tree")
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
                    print("The node is present in the tree")
                    return True
                elif value < temp.value:
                    temp = temp.left
                elif value > temp.value:
                    temp = temp.right
            print("the node is not present in the tree")
            return False

    def breadth_first_traversal(self):
        if self.root is None:
            print("this tree contains no nodes")
            return False

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

    def tree_reversal(self):

        if self.root is None:
            print("this tree contains no nodes")
        else:
            def reverse(current_node):
                current_node.left,current_node.right = current_node.right, current_node.left
                if current_node.left:
                    reverse(current_node.left)
                if current_node.right:
                    reverse(current_node.right)
            reverse(self.root)
            return True

    def depth_first_preOrder(self):
        results = []

        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)
        traverse(self.root)
        return results

nums = [41,67,23,89,64,12,7,98,35,3]
my_BST = BinarySearchTree()

for num in nums:
    my_BST.insert(num)

my_BST.tree_reversal()

print(my_BST.depth_first_preOrder())

#The Tree reversal method recursively traverses the tree beginning with the root
#a function, 'reverse()' is defined within the method. The method excepts a node as an argument
#the function first swaps the positions of the node's left and right children
#then, each each child exists (are not None) it calls 'reverse()' on the child node
#this continues the process until all nodes and child nodes have been swapped, creating a reversal of subtrees
