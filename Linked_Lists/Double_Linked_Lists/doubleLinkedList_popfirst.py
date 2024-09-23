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

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head, self.tail = new_node, new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            self.length +=1

    def pop_first(self):

        if self.head is None:
            print("This list contains no nodes")
            return None
        elif self.head == self.tail:
            return_node = self.head
            self.head, self.tail = None, None
            return return_node
        else:
            temp = self.head
            self.head = self.head.next
            temp.next, self.head.prev = None, None
            return temp

        if self.length > 0:
            self.length -=1






my_DLL = DoubleLinkedList()

lst = [3,5,7,12]

for i in lst:
    my_DLL.append(i)

my_DLL.pop_first()
my_DLL.pop_first()





my_DLL.print_nodes()
#print(my_DLL.length)
