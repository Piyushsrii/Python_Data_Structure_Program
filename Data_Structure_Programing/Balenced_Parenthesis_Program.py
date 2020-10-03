'''Desc -> Take an Arithmetic Expression such as
(5+6)∗(7+8)/(4+3)(5+6)∗(7+8)/(4+3) where parentheses are used to order the
performance of operations. Ensure parentheses must appear in a balanced
fashion.'''


class Stack:

    # this method for initiaze the ithems
    def __init__(self):
        self.items = []
        # this method for check empty

    def is_empty(self):
        return self.items == []

    # this method for push the element
    def push(self, data):
        self.items.append(data)

    # this method for Delete the method
    def pop(self):
        return self.items.pop()


s = Stack()
exp = input('Please enter the expression: ')
try:
    for c in exp:
        if c == '(':
            s.push(1)
            if c == ')':
                if s.is_empty():
                    is_balanced = False
                    break
                s.pop()
        elif c == '[':
            s.push(1)
            if c == ']':
                if s.is_empty():
                    is_balanced = False
                    break
                s.pop()
        elif c == '{':
            s.push(1)
            if c == '}':
                if s.is_empty():
                    is_balanced = False
                    break
                s.pop()
    else:
        if s.is_empty():
            is_balanced = True
        else:
            is_balanced = False
except ValueError:
    print("please enter correct value")
    if is_balanced:
        print('Expression ', exp, ' is correctly parenthesized.')
    else:
        print('Expression ', exp, ' is not correctly parenthesized.')
