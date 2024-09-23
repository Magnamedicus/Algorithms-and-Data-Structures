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

      #The insert() method takes in an index and a value for the new node
      #It then creates the new node, passing in 'value' as an argument
      #Insert() then checks if the given index is less than zero or greater than the list's length
      #in this instance, index actually CAN be equal to self.length. Even though this is technically out of range
      #If index is equal to length, it means that we are to create a new index on the end of the list and place the new node there

      #If this is the case, we call append and add the node to the end
      #if index is equal to zero, we call prepend and add the node to the beginning
      #if index is somewhere in between, we create a 'temp' pointer and set it equal to self.get_by_index(index-1)
      #this places our pointer one node behind the node with the index of interest, that way we have access to
      #the index where the new node is going.
      #For instance, if the entered index is 2, it means we want the new node to exist at index 2
      # and so, our pointed must point to index 1, so new_node can be added to the right of 1 and become 2

      #Knowing that we will need to break the connection between nodes at indices 1 and 2 and then reconnect them later
      #we save the node immediately following our temp pointer to a variable called "break_point"
      #We next connect temp.next to new_node and assign new_node.next to break_point
      #Now, the new node exists at the given index with the node that used to exist at the index pushed one to the right




my_linked_list = LinkedList()
lst = [3,4,5,6]
for i in lst:
   my_linked_list.append(i)

my_linked_list.insert(1,18)

my_linked_list.print_nodes()

#other_list = LinkedList()
#other_list.insert(4,15)
#other_list.print_nodes()

