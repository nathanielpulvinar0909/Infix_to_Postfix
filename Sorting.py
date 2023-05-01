def infix_to_postfix(data):
    # To print the main method in the end of program
    class Stack:
        def __init__(self):  # Main list / data
            self.stack = []

        def null(self):  # To check if the data is empty
            return len(self.stack) == 0

        def check(self):  # To return if the index
            if not self.null():
                return self.stack[-1]
            else:
                return "$"

        def push(self, data):  # To add elements
            self.stack.append(data)

        def pop(self):  # To delete the recent added data
            if not self.null():
                return self.stack.pop()
            else:
                return "$"

    stack = Stack()  # Assigning an object in the class
    postfix = ""

    # Setting symbols included in the postfix and infix
    # such as times, divide, plus, minus and exponent
    symbols = {
        "*": 3,
        "/": 3,
        "+": 2,
        "-": 2,
        "^": 4
    }
    # Based on the rules of PEMDAS via prioritization

    # Main data manipulation
    for i in data:
        if i.isalpha():  # Signature code
            postfix += i
        else:
            while not stack.null() and symbols.get(stack.check(), 0) >= symbols.get(i, 0):
                postfix += stack.pop()
            stack.push(i)

    # As long as the stack is not null, add data
    while not stack.null():
        postfix += stack.pop()

    return postfix  # Returning the data of postfix accumulated


exp = input("Enter the infix expression  >  ")  # Input the infix
print("Postfix Expression is :", infix_to_postfix(exp))  # Result of converted Postfix


