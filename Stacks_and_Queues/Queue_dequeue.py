class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value = None):
        if value:
            new_node = Node(value)
            self.first = new_node
            self.last = new_node
            self.length = 1
        else:
            self.first = None
            self.last = None
            self.length = 0

    def print_queue(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next

    def enqueue(self,value):
            new_node = Node(value)
            if self.first == None:
                self.first = new_node
                self.last = new_node

            else:
                self.last.next = new_node
                self.last = new_node
            self.length +=1

    def dequeue(self):
        if self.first is None:
            print("this queue contains no nodes")
            return None
        else:
            temp = self.first
            self.first = self.first.next
            temp.next = None
            self.length -=1
            return temp

my_queue = Queue()

my_queue.enqueue(5)
my_queue.enqueue(13)
my_queue.enqueue(8)

my_queue.dequeue()

my_queue.print_queue()