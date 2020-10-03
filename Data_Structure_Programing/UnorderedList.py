'''Desc -> Read the Text from a file, split it into words and arrange it as Linked List.
Take a user input to search a Word in the List. If the Word is not found then add it
to the list, and if it found then remove the word from the List. In the end save the
list into a file'''
class Node(object):
    #this methodfor constructor
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    #this method for grtting the data
    def get_data(self):
        return self.data
    #this method for the moving next node
    def get_next(self):
        return self.next_node

    #this method for get the data
    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList(object):

     #this method for constructor
    def __init__(self, head=None):
        self.head = head

    #Display the data
    def displayall(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next_node

    #this method for insert the data
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None:
                current = current.next_node
            current.next_node = new_node

    #this method to diplay the data
    def fdisplay(self):
        current = self.head
        temp = ""
        while current:
            # print(current.data, end = ' ')
            temp = temp + current.data + " "
            current = current.get_next()
        return temp
    #this method for search the data
    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        return found

    # this method delete the data
    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())


# Main Code execution starts here
if __name__ == '__main__':

    # Start with the empty list
    llist = LinkedList()

    # Getting the words from the File and creating a file.
    fname = input("\nEnter the File Name: ")
    fhand = open(fname, 'r')
    FLines = fhand.readlines()
    for line in FLines:
        words = line.split()
        for word in words:
            llist.insert_at_end(word)
    print("\n File contents in the List is:")
    llist.displayall()

    # Searching the word in the Linked List
    Searchword = input("\nEnter the word to be searched : ")
    if (llist.search(Searchword)):
        llist.delete(Searchword)
        print("Word", Searchword, " found in the Linked List and deleted")
    else:
        print("Word", Searchword, " not found in the Linked List")
    # llist.displayall()

    # Updated Linked list is stored in the file b.txt
    fname = "b.txt"
    fhand = open(fname, 'w+')
    a = llist.fdisplay()
    # print(a)
    fhand.write(a)
    fhand.close()

    print("File created with filename b.txt")