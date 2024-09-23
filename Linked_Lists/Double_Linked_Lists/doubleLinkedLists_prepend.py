class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self, value=None):
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

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1

        return True

    def pop(self):

        if self.head is None:
            print("this list contains no nodes")
            return None
        elif self.head == self.tail:
            return_node = self.head
            self.head, self.tail = None, None
            return return_node
        else:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
            self.length -= 1
            return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head, self.tail = new_node, new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            self.length += 1

    # The prepend method is, again, very similar to prepend for the single linked list
    # the one exception being that we are connecting the new node to the subsequent node's 'prev' property

    # the method checks to see if the list is empty, if it is, self.head and self.tail are set equal to the new node
    # otherwise, self.head's prev propert is set equal to the new node, the new node's next propert is set equal to self.head
    # self.head is set equal to new_node (moving over to the left) and self.length is incremented by 1.


my_DLL = DoubleLinkedList()

lst = [3, 5, 7]

for i in lst:
    my_DLL.append(i)

my_DLL.prepend(12)

my_DLL.print_nodes()
# print(my_DLL.length)
