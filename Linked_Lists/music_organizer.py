import random
class Node:
    def __init__(self,title,artist, length, year):
        self.title = title
        self.artist = artist
        self.length = length
        self.year = year
        self.next = None

class LinkedList:
    def __init__(self,title=None, artist=None, length=None, year=None):
        self.head = None

        if title is not None:
            new_node = Node(title,artist,length, year)
            self.head = new_node
            self.tail = new_node
        if self.head:
            self.length = 1
        else:
            self.length = 0

    def print_nodes(self):

        if self.head:
            print(f"\nThis collection contains {self.length} songs.")
            temp = self.head
            print("Your Collection:")
            while temp is not None:
                print(f"Title:{temp.title}; Artist:{temp.artist}")
                temp = temp.next
        else:
            print("\nThis list contains no nodes")
    def append(self,title,artist,length,year):
        print(f"A song with title '{title}' was added to the end of the list.")
        new_node = Node(title,artist,length, year)
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
            node_value = self.head.title
            print(f"A song with the title of {node_value} was removed from the end of the list ")
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



            print(f"A node with the value of {temp.title} was removed from the end of the list")
            return temp.title

    def prepend(self,title,artist,length,year):
        new_node = Node(title,artist,length, year)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

            print(f"A song with a title of {title} has been prepended to the list")
        self.length += 1
        return True

def main_menu():

    print("\n1. Add a song to the end of your collection")
    print("2. Add a song to the beginning of your collection")
    print("3. Remove a song from the end of your collection")
    print("4. Display the songs in your collection")

    choice = input("\nChoose an option, or type 'Exit' to quit ")
    return choice.strip()


def prompt_user_make():
    make_LL = input("Would you like to make a new music collection? ").strip()

    return make_LL.lower()

def prompt_user_songs():
    title = input("Enter a title: ")
    artist = input("What artist perform this title? ")
    length = input("What is the length of this song in seconds? ")
    year = input("What year was this song produced? ")

    return title,artist,length,year

def main():

    while True:

        make_ll = prompt_user_make()

        if make_ll == 'yes':
            music_collection = LinkedList()
            break
        elif make_ll == 'no':
            print("Fair enough, maybe next time")
            return
        else:
            print("Please enter a valid input: ")

    while True:
        choice = main_menu().lower()
        if choice == "1":
            title,artist, length, year = prompt_user_songs()
            music_collection.append(title,artist,length,year)
        elif choice == "2":
            title, artist, length, year = prompt_user_songs()
            music_collection.prepend(title, artist, length, year)
        elif choice == "3":
            music_collection.pop()
        elif choice == "4":
            music_collection.print_nodes()
        elif choice == "exit":
            print("Thanks, see you later!")
            return
        else:
            print("Please enter a valid input")

        continue_inputs = input("\nanother choice? ").strip()
        if continue_inputs.lower() == 'yes':
            continue
        elif continue_inputs.lower() == 'no':
            return







main()

