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
            #print(f"A node with the value of {node_value} was removed from the end of the list ")
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



            #print(f"A node with the value of {temp.value} was removed from the end of the list")
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
            #print(f"A node with the value {node_value} has been removed")
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
            #print(f"The value of the node at index: {index} is {temp.value}")
            return temp

    def set_value(self,index,value):
        temp = self.get_by_index(index)
        if temp:
            temp.value = value
            return True
        else:
            return False

    def insert(self,index,value):
      new_node = Node(value)
      if index < 0 or index > self.length:
          print("index out of range")
          return False
      elif index == 0:
          return self.prepend(value)
      elif index == self.length:
          return self.append(value)
      else:
          temp = self.get_by_index(index-1)
          break_point = temp.next
          temp.next = new_node
          new_node.next = break_point
          self.length +=1
          return True

    def remove(self,index):
        if index < 0 or index >= self.length:
            print("index out of range")
            return None

        elif self.head is None:
            print("This list contains no nodes")
            return None

        elif index == 0:
            return self.pop_first()

        elif index == self.length -1:
            return self.pop()

        else:
            pre = self.get_by_index(index-1)
            temp = pre.next
            pre.next = temp.next
            temp.next = None
            self.length -=1
            return temp

#the remove() method first checks if the index is out of range or if the list is empty
#if either condition is true, the method returns None and prints an error message
#if the index is equal to zero, it uses the pop_first() method to remove the first node
#if the index is equal to self.length - 1, it uses the pop() method to remove the very last node
#otherwise, we set up two pointers, 'pre' and 'temp'.

#we once again stagger the pointers with pre one node behind temp.
#we initialize pre's position as one node behind the given index, putting temp at the index itself
#we then attach node pre is pointing to the node temp is pointing to
# this creates a connection between the two nodes adjecent to the node we want to remove

#then we simply set temp.next to None, disconnecting the node at the given index from the rest of the list
#we then decrement the list length and return temp (which is now the removed node)









my_linked_list = LinkedList()
lst = [3,4,5,6]
for i in lst:
   my_linked_list.append(i)

my_linked_list.remove(1)


my_linked_list.print_nodes()

#other_list = LinkedList(3)
#other_list.remove()
#other_list.print_nodes()

