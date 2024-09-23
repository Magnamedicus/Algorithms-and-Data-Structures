class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value=None):
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
    def append(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1
        return True

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
            self.length -=1



            print(f"A node with the value of {temp.value} was removed from the end of the list")
            return temp.value

    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

            print(f"A node with a value of {value} has been prepended to the list")
        self.length += 1
        return True

    def pop_first(self):
        if self.head.next == None:
            node_value = self.head.value
            self.head = None
            self.tail = None
            return node_value
        elif self.head == None:
            print("This linked list contains no nodes")
            return
        else:
            temp = self.head
            node_value = temp.value
            self.head = self.head.next
            temp.next = None
            print(f"A node with the value {node_value} has been removed")
            self.length -=1
            return node_value

    def get_by_index(self,index):
        temp = self.head
        if index < 0 or index >= self.length:
            print("Your index is out of range")
            return None
        else:
            for _ in range(index):
                temp = temp.next
            print(f"The value of the node at index: {index} is {temp.value}")
            return temp

    def set_value(self,index,value):
        temp = self.get_by_index(index)
        if temp:
            temp.value = value
            return True
        else:
            return False







my_linked_list = LinkedList()
lst = [3,4,5,6]
for i in lst:
   my_linked_list.append(i)


my_linked_list.get_by_index(3)
my_linked_list.set_value(2,34)
my_linked_list.print_nodes()

