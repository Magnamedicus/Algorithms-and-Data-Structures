
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

my_linkedList = LinkedList(24)

print(my_linkedList.tail.value)

#This is how we construct an initialize the very first node of a linked list
#We first define a "node" class where each instantiation of a node contains a value and a pointed to some other node

#Then, we define a linked list class where a new linked-list will instantiate a node from the node class as its first node
#Argument for 'value', passed to the linked list instantiation, in turn gets passed to the 'node' instantiation
#We then define 'head' and 'tail' pointer which intitally point to this very first node
#we also define a length that will become incremented or decremented as we grow or shrink the list

#This is the standardized method for making a new linked list