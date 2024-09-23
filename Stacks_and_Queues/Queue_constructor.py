class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value = None):

        if value:
            new_node = Node(value)
            self.first = new_node
            self.last = new_node
            self.length = 1
        else:
            self.first = None
            self.last = None
            self.length = 0

    def print_queue(self):

        temp = self.first
        if temp:
            print(temp.value)
            temp = temp.next


#The Queue data structure is essentially a linked list where nodes are only added at one end and only removed
#from the opposite end. Adding a node is referred to as 'Enqueuing" and removal "Dequeuing".
#for a single linked list, we want to make sure the enqueue() method is something analagous to append()
#similarly, we want to make sure the dequeue() method is something equivalent to pop-first().

#this is essentially a normal, single, linked list where we only add nodes with append and only remove them
#with pop-first. This is because both methods have O(1) time complexity where traditional pop() is O(n).

#also, instead of head and tail we have first and last. self.head is analagous to self.first
#self.tail is analagous to self.last




