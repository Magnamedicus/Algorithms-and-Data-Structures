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

#The insert method first creates a new node, it then checks if the tree is empty. If it is, self.root is set equal to new_node.
#If the list is not empty it first creates a 'temp' pointer set equal to self.head.
# It then creates an infinite while loop and compares the value of the new node to the value of temp. If the value of new_node is less than the value of temp
#the method checks to see if there is an empty space to the left of temp (checks if temp.left is None)
#if this is the case, temp.left is set equal to new_node. If this is not the case, temp is reassigned to the node on the left (temp = temp.left)

#similarly if new_node's value is greater than temp.value, the method inserts new_node to the right, but only if theres an empty space
#if there isn't, temp = temp.right.
#if at any point, temp.value is equal to new_node.value, False is returned
#returning True or False under various circumstances is how we break free from the while loop



nums = [76,45,34,87,93,47,62,12,6,33,100,52]
my_BST = BinarySearchTree()
for i in nums:
    my_BST.insert(i)

print(my_BST.root.left.left.left.right.value)