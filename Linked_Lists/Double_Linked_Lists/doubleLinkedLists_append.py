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

#The append method is very similar to append for the single linked list
#The method first checks to see if the list is empty by checking is self.head == None
#if so, self.head and self.tail are set equal to the new node
#if there are already nodes in the linked list, the method sets tail.next equal to the new node
#the method then also sets the new node's 'prev' property equal to self.tail
#self.tail is then set equal to the new node, which now represents the terminal end of the list

#self.length is incremented by 1 and the method returns True.






my_DLL = DoubleLinkedList()

my_DLL.append(34)
my_DLL.append(45)
my_DLL.append(4)



my_DLL.print_nodes()