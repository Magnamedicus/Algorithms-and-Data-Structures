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

    def pop(self):

        if self.top == None:
            print("this stack contains no nodes")
            return None
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            self.length -=1
            return temp


my_stack = Stack()

my_stack.push(4)
my_stack.push(6)
my_stack.push(13)

my_stack.pop()

my_stack.print_stack()

#The pop method for a stack is analagous to the pop-first() method for any other single linked list.
#We are only removing from the 'head' or 'top' end of the list
#The function first assigns a 'temp' pointer to 'top' node, then moves the 'top' pointer forward
#with top = top.next. it then disconnects the end node by setting temp.next to None
#it ends by decrementing self.length by 1 and returning temp.