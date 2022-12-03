
class Stack:
    def __init__(self):
        self.my_stack = []

    def is_empty(self):
        if self.my_stack:
            return False
        else:
            return True

    def push(self, new_element):
        self.my_stack.append(new_element)

    def pop(self):
        self.my_stack.pop(-1)
        if len(self.my_stack) > 0:
            return self.my_stack[-1]

    def peek(self):
        result = self.my_stack[-1]
        return result

    def size(self):
        result = len(self.my_stack)
        return result
