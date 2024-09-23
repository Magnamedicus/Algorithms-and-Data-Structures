import random


class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self,value = None):
        if value:
            new_node = Node(value)
            self.top = new_node
            self.length = 1
        else:
            self.top = None
            self.length = 0

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    def push(self,value):
        new_node = Node(value)
        if self.top == None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length +=1

my_stack = Stack()

#for i in range(10):
    #rand_num = random.randint(1,50)
    #my_stack.push(rand_num)

my_stack.push(4)
my_stack.push(6)
my_stack.push(13)

my_stack.print_stack()

#The push() method is analagous to prepend() in any other single linked list
#If the stack is empty, it simply creates a new node and assigns self.top to new node, then increments length
#If not empty, it sets new_node.next equal to self.top, then moves self.top to equal new_node
#finally, it increments the length by one

