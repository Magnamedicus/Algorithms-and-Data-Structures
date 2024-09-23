class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value=None):
        self.head = None

        if value is not None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
        if self.head:
            self.length = 1
        else:
            self.length = 0

    def print_nodes(self):

        if self.head:
            print(f"This linked list contains {self.length} nodes.")
            temp = self.head
            while temp is not None:
                print(temp.value)
                temp = temp.next
        else:
            print("This list contains no nodes")

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1


    def pop(self):
        if self.head == None:
            print("This list contains no nodes")
            return None
        elif self.head == self.tail:
            node_value = self.head.value
            print(f"A node with the value of {node_value} was removed from the end of the list ")
            self.head = None
            self.tail = None
            return node_value
        else:
            temp = self.head.next
            pre = self.head

            while temp.next is not None:
                temp = temp.next
                pre = pre.next
            pre.next = None
            self.tail = pre
            self.length -= 1

            print(f"A node with the value of {temp.value} was removed from the end of the list")
            return temp
#the pop method first address two edge cases: 1. if the list is empty, 2. if the list only contains 1 node
#if the list is empty it simply prints that there are no nodes and then returns None
#if there is only one node, it stores the node's value, prints that a node with this value has been removed,
#sets self.head and self.tail to None, and then returns the removed node's value

#otherwise, we create two pointers for traversing the list, temp and pre
#they are initialized in staggered position with temp being just ahead of pre.
#so long as temp.next is not None, we increment both their positions forward until temp is at the end
#and pre is one node behind it
#we then detach the end node by setting pre.next to None. we reset the tail by setting self.tail equal to pre
#and we return the value of the node temp is pointing to, which is the value of the now detached node
#we also decrement the length by one


my_linked_list = LinkedList()
lst = [3, 4, 5, 6]
for i in lst:
    my_linked_list.append(i)

my_linked_list.pop()
my_linked_list.pop()
my_linked_list.pop()

my_linked_list.print_nodes()