'''Desc -> A palindrome is a string that reads the same forward and backward, for
example, radar, toot, and madam. We would like to construct an algorithm to
input a string of characters and check whether it is a palindrome.'''
''''''
class Stack(object):

    #this method for initiaze the value
    def __init__(self):
        '''
               :param:self:initialize the value
               '''
        self.values = []
    # this method for push the element
    def push(self, value):
        '''
               :param:Value: For the value
               '''
        self.values.append(value)
    #this method created for Delete the element
    def pop(self):
        '''
               :param:self: Delete the element
               :return : return delete elemnt
               '''
        return self.values.pop()

class Queue(object):

    #this method to initialize the value
    def __init__(self):
        '''
               :param:self: initaizeyhe value
               :return : return the length
               '''
        self.values = []

    #this method for initiazr=e the value
    def push(self, value):
        '''
               :param:Value: For appending the value
               '''
        self.values.append(value)

    #this method for the pop the emement
    def pop(self):
        return self.values.pop(0)
stack = Stack()
queue = Queue()
class PalindromeChecker(object):

    # create the constructor
    def __init__(self, word):
        self.word = word
        self.queue = Queue()
        self.stack = Stack()

    #this method for check the value
    def check_palindrome(self):
        for letter in self.word:
            self.queue.push(letter)
            self.stack.push(letter)
        for i in range(len(self.word)):
            if self.queue.pop() != self.stack.pop():
                return False
        return True
# Driver Code
if __name__ == '__main__':
    s = input("Enter the String:")
    res = PalindromeChecker(s)
    if res.check_palindrome():
        print(s, " is a palindrome")
    else:
        print(s, " is not a palindrome")