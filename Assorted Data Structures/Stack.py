

class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def push(self, val):
        self.stack.insert(0, val)

    def pop(self):
        return self.stack.pop(0)

    def peek(self):
        return self.stack[0]

    def isEmpty(self):
        if len(self.stack) is 0:
            return True

        return False

    def __str__(self):
        return str(self.stack)

#testing
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(str(stack.pop()))
print(str(stack))
