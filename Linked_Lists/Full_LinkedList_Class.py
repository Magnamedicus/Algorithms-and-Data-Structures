#fully written out singley linked list class with all of its most common methods


class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
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
            return False
        else:
            temp = self.head
            while temp:
                print(temp.value)
                temp = temp.next
            return True

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head,self.tail = new_node,new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length +=1
        return True

    def pop(self):
        if self.head is None:
            print("this list contains no nodes")
            return None
        elif self.head == self.tail:
            temp = self.head
            self.head,self.tail = None,None
            self.length -=1
            return temp
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            self.tail = temp
            temp = temp.next
            self.tail.next = None
            print(f"A node with the value {temp.value} has been removed")
            self.length -=1
            return temp

    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head,self.tail = new_node,new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1
        return True

    def pop_first(self):
        if self.head is None:
            print("This list contains no nodes")
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            print(f"A node with value {temp.value} has been removed from the list")
            self.length -=1
            return temp

    def get_by_index(self,index, print_value = False):
        if self.head is None:
            print("this list contains no nodes")
        elif index > self.length -1:
            print("Index is out of range")
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            if print_value:
                print(f"The value at index {index} is {temp.value}.")
            return temp

    def insert(self,index,value):
        new_node = Node(value)
        if index > self.length -1:
            print("index is out of range")
            return False
        else:
            temp = self.get_by_index(index)
            pre = self.head
            while pre.next is not temp:
                pre = pre.next

            pre.next = new_node
            new_node.next = temp
            self.length +=1
            return True

    def set(self,index,value):
        if index > self.length:
            print("index is out of range")
        else:
            temp = self.get_by_index(index)
            temp.value = value
            return True

    def find_middle(self):
        if self.head is None:
            print("This list contains no nodes")
            return None
        elif self.head == self.tail:
            print("this list contains only one node")
            return self.head
        else:
            slow,fast = self.head,self.head

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            print(f"the middle node has a value of {slow.value}.")
            return slow

    def reversal(self):
        if self.head is None or self.head == self.tail:
            print("This list contains less than 2 nodes and cannot be reversed.")
            return False
        else:
            temp = self.head
            self.head = self.tail
            self.tail = temp

            before,after = None, temp.next

            while temp:
                after = temp.next
                temp.next = before
                before = temp
                temp = after
            return True



nums = [4,67,2,3,12,15,18,22,1]
my_LL = LinkedList()
for num in nums:
    my_LL.append(num)

#my_LL.reversal()





my_LL.print_nodes()