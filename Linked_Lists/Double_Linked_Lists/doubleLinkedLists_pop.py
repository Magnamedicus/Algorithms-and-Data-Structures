class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self,value = None):
        if value:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.head = None
            self.tail = None
            self.length = 0


    def print_nodes(self):
        if self.head is None:
            print("this list contains no nodes")
            return None

        else:
            temp = self.head
            while temp is not None:
                print(temp.value)
                temp = temp.next
            return

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length +=1

        return True

    def pop(self):

        if self.head is None:
            print("this list contains no nodes")
            return None
        elif self.head == self.tail:
            return_node = self.head
            self.head,self.tail = None, None
            return return_node
        else:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
            self.length -=1
            return temp

#unlike single linked lists, the pop method for a double linked list has a time complexity of O(1), constant
#This is because we don't have to iterate all the way through the list to access the node immediately before tail
#instead, we can access this node with tail.prev.

#The method first checks if the list is empty, if so, it returns None
#if the list has only one node, it simply save the node at self.head and returns it after setting head and tail to None

#if there is more than one node, it creates a 'temp' pointer and sets it equal to tail
#it then sets tail equal to tail.prev, moving it back one node
#the method then detaches the end node by setting tail.next to None and temp.prev to None
#the method finishes by decrementing self.length and returning the node located at 'temp'






my_DLL = DoubleLinkedList()

lst = [3,5,2]

for i in lst:
    my_DLL.append(i)

my_DLL.pop()
my_DLL.pop()




my_DLL.print_nodes()
#print(my_DLL.length)