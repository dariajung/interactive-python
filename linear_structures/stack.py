class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

def revstring(_str):
    s = Stack()
    for i in _str:
        s.push(i)

    rev = []

    while not s.isEmpty(): 
        rev.append(s.pop())

    return ''.join(rev)

def checkPar(_str):
    s = Stack()
    balanced = True

    for i in _str:
        if i == '(' and balanced:
            s.push(i)

        else:
            if s.isEmpty():
                balanced = False

            if i == ')' and balanced:
                s.pop()

    if s.isEmpty() and balanced:
        return True
    else:
        return False

