class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.next = None


class Queue:
    def __init__(self,node):
        if node:
            self.first = node
            self.last = node
            self.length = 1
        else:
            self.first,self.last = None,None
            self.length = 0

    def enqueue(self,node):
        if self.first is None:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self.length +=1

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
    def __init__(self, value = None):
        if value:
            new_node = Node(value)
            self.root = new_node

        else:
            self.root = None

    def insert(self, value):
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

    def breadth_first_search(self):
        if self.root is None:
            print("this tree contains no nodes")
            return False
        else:

            current_node = self.root
            queue = Queue(current_node)
            result = []


            while queue.length > 0:
                current_node = queue.dequeue()
                if current_node.left:
                    queue.enqueue(current_node.left)
                if current_node.right:
                    queue.enqueue(current_node.right)
                result.append(current_node.value)
            return result

    def depth_first_search_preOrder(self):
        if self.root is None:
            print("this tree contains no nodes")
            return None
        results = []
        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left:
                traverse(current_node.left)
            if current_node.right:
                traverse(current_node.right)

        traverse(self.root)
        return results



nums = [3,74,2,7,12,9,22,14]
my_BST = BinarySearchTree()

for i in nums:
    my_BST.insert(i)



print(my_BST.depth_first_search())


#The depth first pre-order traversal uses recursion to first visit the entire left sub-tree, then the right
#With each node visited, the node value is appended to the results list. Result is ultimately return by the method
#Traverse is called with a node passed as an argument, it first appends the value of that node to results
#Traverse then checks if there is a node to the left and then to the right. If there is, it similarly calls
#traverse on the left and right nodes. This progression continues until the left and right subtrees have been
#sequentially traversed and their values appended to results.
