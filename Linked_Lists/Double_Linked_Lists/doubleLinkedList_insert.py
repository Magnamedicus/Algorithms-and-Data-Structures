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

    def get_by_index(self, index):
        if index < 0 or index >= self.length:
            print("index out of range")
            return None
        else:
            if index < self.length / 2:
                temp = self.head
                for _ in range(index):
                    temp = temp.next
                # print(temp.value)
                return temp
            else:
                temp = self.tail
                for _ in range(self.length - 1, index, -1):
                    temp = temp.prev
                # print(temp.value)
                return temp

    def set_by_index(self, index, value):
        temp = self.get_by_index(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)

        else:
            new_node = Node(value)
            before = self.get_by_index(index - 1)
            after = self.get_by_index(index)

            before.next = new_node
            new_node.prev = before
            new_node.next = after
            after.prev = new_node

    # the insert method works similarly to the way it works for the single linked list
    # if the index is 0 we simply call prepend
    # if the index is equal to self.length, we call append
    # otherwise, we will create a new node, then define two pointers: 'before' and 'after'
    # one pointer will point the node that will exist before the new node and the one after it

    # we set before equal to get(index-1) so that its one behind the index where the node is going
    # we set after equal to get(index) so its pointing at the index where the node will be placed
    # we then attach the new node and the nodes on either side of it


my_DLL = DoubleLinkedList()

lst = [3, 5, 7, 8]

for i in lst:
    my_DLL.append(i)

my_DLL.insert(2, 10)
my_DLL.insert(1, 20)

my_DLL.print_nodes()
# print(my_DLL.length)
