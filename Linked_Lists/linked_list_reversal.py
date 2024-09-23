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


#For the reversal method, we first swap the head and tail
#to do this we assign a 'temp' point to head, then make head equal to tail
#and finish by making tail equal to temp.

#we then set up three pointers for iterating through the list and reversing the order of its nodes
#one of these pointers has already been created, 'temp'. we create a 'before' pointer and set it to 'None'.
#we will think of the 'before' pointer as existing to the 'left' of temp.
#we then also create an 'after' pointer and set it equal to temp.next.
#we will think of the 'after' pointer as existing to the right of temp.

#these three pointer will be iterated together through the linked list and reverse the connections between nodes
#this is done with exactly 4 steps that MUST be written in a specific order. if not, the reversal will fail.

# 1. First, 'after' is set equal to temp.next (this is already its position for the first iteration)
# 2. Second, temp.next is set equal to 'before', this realigns temp's connection to the node currently on its opposite side
# 3. Third, 'before' is iterated forward by setting it equal to temp
# 4. Fourth, 'temp' is iterated forward by being set equal to 'after'

#Each iteration will leave a gap between temp and after, however, the NEXT iteration will fill in that gap
#when temp.next is set equal to before, that is if before and temp have been iterated forward properly
#the loop will iterate over the range of 0 to self.length
#in the end, the directionality of the list will be completely reversed.









my_linked_list = LinkedList()
lst = [3,4,5,6]
for i in lst:
   my_linked_list.append(i)

my_linked_list.reverse()



my_linked_list.print_nodes()

#other_list = LinkedList(3)
#other_list.remove()
#other_list.print_nodes()

