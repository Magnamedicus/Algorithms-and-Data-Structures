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

    def get_by_index(self,index):
        if index < 0 or index >= self.length:
            print("index out of range")
            return None
        else:
            if index < self.length/2:
                temp = self.head
                for _ in range(index):
                    temp = temp.next
                print(temp.value)
                return temp
            else:
                temp = self.tail
                for _ in range(self.length-1, index, -1):
                    temp = temp.prev
                print(temp.value)
                return temp


    #The get method for a double link list can be optimized to take advantage of the list's bidirectionality
    #the get method for a single linked list would work here, however having the ability to move in both directions
    #allows us to choose which end to start from based upon how close it is to the given index

    #in this algorithim, if the index is in the first half of the list (index < self.length/2) we start from self.head
    #if the index is in the second half of the list (index >= self.length/2) we start from self.tail and iterate backwards

    #in either case we iterate through the list using a for-loop with range(index) and return temp after the loop
    #has completed


my_DLL = DoubleLinkedList()

lst = [3, 5, 7, 8, 11, 14, 16]

for i in lst:
    my_DLL.append(i)

my_DLL.get_by_index(1)

#my_DLL.print_nodes()
# print(my_DLL.length)
