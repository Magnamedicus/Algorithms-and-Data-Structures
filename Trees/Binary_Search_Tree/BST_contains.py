class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self,value = None):
        if value:
            new_node = Node(value)
            self.root = new_node
        else:
            self.root = None

    def insert(self,value):
        new_node = Node(value)


        if self.root is None:
            self.root = new_node
            return True
        else:

            temp = self.root
            while True:
                 if new_node.value == temp.value:
                     return False
                 elif new_node.value < temp.value:
                     if temp.left is None:
                         temp.left = new_node
                         return True
                     temp = temp.left

                 elif new_node.value > temp.value:
                     if temp.right is None:
                         temp.right = new_node
                         return True
                     temp = temp.right

    def contains(self, value):
        if self.root is None:
            print("This list contains no nodes")
            return False
        else:
            temp = self.root

            while temp:
                if temp.value == value:
                    return True

                else:
                    if value < temp.value:
                        temp = temp.left
                    elif value > temp.value:
                        temp = temp.right
            return False



nums = [3,14,34,54,21,11,65,5,9]
my_BST = BinarySearchTree()

for i in nums:
    my_BST.insert(i)


print(my_BST.contains(9))


#The contains methods checks if a given value is in the tree, returns True if it is and False if it is not
#This is essentially a divide and conquer algorithm
#We use a temp point, initially set to self.root, to navigate through the tree using a while loop that runs
#so long as 'temp' is not None. For each round of the loop, the method check is temp.value is equal to 'value'.
#if so, we return True. If not, temp is either iterated left or right. left if value is less then temp.value and
#right if value is greater then temp.value

#if temp ever runs off the edge of the tree, rendering it equal to 'None', we know that the given value was not found
#at this point, the while loop breaks and we return False
