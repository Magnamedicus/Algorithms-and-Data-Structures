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

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


    def has_loop(self):

        if self.head is None:
            return False

        elif self.head.next is None:
            return False

        else:

            fast_pointer, slow_pointer = self.head, self.head

            while fast_pointer and fast_pointer.next:

                slow_pointer = slow_pointer.next
                fast_pointer = fast_pointer.next.next

                if fast_pointer == slow_pointer:
                    return True

            return False

    #The has_loop() method will detect if there is a cycle anywhere in the linked list
    #each round of the while loop will iterate the fast pointer forward two nodes and the slow pointer forward one node
    #it will then check to see if the two node equal one another
    #if there is a loop in the list, they will eventually collide and equal one another
    #the while loop will run until the fast_pointer is at the last node or has moved off the edge as equals None
    #the function return True is a loop is detected and False if one is not








my_linked_list = LinkedList()
lst = [3,4,5,6]
for i in lst:
   my_linked_list.append(i)

print(my_linked_list.has_loop())



my_linked_list.print_nodes()

#other_list = LinkedList(3)
#other_list.remove()
#other_list.print_nodes()

