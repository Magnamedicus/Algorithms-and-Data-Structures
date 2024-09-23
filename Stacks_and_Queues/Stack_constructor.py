
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value = None):
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

my_stack = Stack(5)
my_stack.print_stack()

#A stack is nothing more than a single linked-list where nodes are added and removed only ffom one end
#In this way, it's a linked list that only uses the prepend() and pop-first() methods to alter the list
#additionally, because nodes are Last In First Out (LIFO), we don't need to track the tail end or "bottom"
#of the stack. Stacks therefore have no 'tail' pointed. They only have a 'Top' pointer which is
#analagous to self.head

