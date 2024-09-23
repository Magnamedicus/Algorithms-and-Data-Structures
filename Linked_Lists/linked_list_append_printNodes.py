import random
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_nodes(self):
        temp = self.head
        print(f"This linked-list contains {self.length} nodes.")

        while temp is not None:
            print(temp.value)
            temp = temp.next
    #The print function defines a pointer "temp" and points it initially at self.head
    #it also begins by printing the length of the linked list
    #so long as temp is not none (meaning its pointing to an actual node in the list) the value
    #of the node temp is pointing to will be printed and then temp will be set equal to temp.next
    #this will move temp along the list until it 'falls off' the end and equals 'None'.

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length +=1

    #the function does three things
        #1. it creates a new node by instantiating the Node class
        #2. it points the node self.tail is currently pointing to at the new node, thereby connecting it to the end
        #3. It points self.tail to self.tail.next, thereby realligning the self.tail pointer with the new end or 'tail' of the list
    #The function first handles the edge case of us potentially appedning a node to an empty list
    #if the list is empty, self.head will equal 'None'
    #if this is the case, self.head and self.tail are set equal to (or 'pointed' at) new_node
    #if this is not the case, the function proceeds with #2 and #3 above
    #lastly, the function increments self.length


my_linked_list = LinkedList(0)

for _ in range(40):
    rand_num = random.randint(0,200)
    my_linked_list.append(rand_num)



my_linked_list.print_nodes()
