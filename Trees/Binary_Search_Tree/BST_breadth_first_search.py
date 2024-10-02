class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        self.next = None

class Queue:
    def __init__(self, node = None):
        if node:
            new_node = node
            self.first = new_node
            self.last = new_node
            self.length = 1
        else:
            self.first = None
            self.last = None
            self.length = 0

    def enqueue(self,node):
        new_node = node
        if self.first is None:
            self.first = new_node
            self.last = new_node


        else:
            self.last.next = new_node
            self.last = new_node
        self.length +=1
        return True

    def dequeue(self):
        if self.first is None:
            return None
        else:
            temp = self.first
            self.first = self.first.next
            temp.next = None
            self.length -=1
            if self.length == 0:
                self.first,self.last = None,None
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
            return True
        else:

            temp = self.root
            while True:
                 if new_node.value == temp.value:
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

    def contains(self, value):
        if self.root is None:
            print("This list contains no nodes")
            return False
        else:
            temp = self.root

            while temp:
                if temp.value == value:
                    return True

                else:
                    if value < temp.value:
                        temp = temp.left
                    elif value > temp.value:
                        temp = temp.right
            return False

    def breadth_first_search(self):

        if self.root is None:
            print("This tree contains no nodes")
            return False
        else:

            current_node = self.root
            queue = Queue(self.root)
            results = []


            while queue.length > 0:
                current_node = queue.dequeue()
                if current_node.left:
                    queue.enqueue(current_node.left)
                if current_node.right:
                    queue.enqueue(current_node.right)
                results.append(current_node.value)
            return results




nums = [3,14,34,54,21,11,65,5,9]
my_BST = BinarySearchTree()

for i in nums:
    my_BST.insert(i)


print(my_BST.breadth_first_search())

#The breadth_first search traverses the tree by level, starting at the root. It first creates a queue
#this can be a list(for simplicity sake) or an actual Queue class
#We first add the root to the Queue and define a results list, which will be returned by the method

#A while loop is establish that will run so long as the queue length is greater than zero
#the method will first pop the first node from the queue, saving it to a variable
# The method will then add the popped node's left and right child nodes (if they exist) to the queue and then
#append the current node's value to results. It will then move on to the next node in the queue.
#eventually, it will make its way completely through the tree until every node has been popped and its value appended to results
#results will then be returned.