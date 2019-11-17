# This stack is implemented based on fixed-size array

class Stack:
    def __init__(self, size): #stack_init()
        self.size = size
        self.arr = [0 for i in range (size)]
        self.t = -1
    def isEmpty(self):
        return self.t == -1
    def push(self, val):
        if(self.t == self.size - 1):
            print("Stack full")
            return
        self.t += 1
        self.arr[self.t] = val
    def top(self):
        if(self.isEmpty()):
            return None
        return self.arr[self.t]
    def pop(self):
        if (self.isEmpty()):
            print("Stack is Empty.Cannot pop")
            return
        self.t -= 1
    def __str__(self):
        s = ""
        for i in range(self.t + 1):
            s += str(self.arr[i])
            s += "->"
        return s

test = Stack(size = 5)
print(test.isEmpty()) #test is Empty

#test Push & Size
test.push(0)
test.push(1)
test.push(2)
test.push(3)
test.push(4)
print(test)

test.push(4)
print(test)

#test pop & top
test.pop()
print(test)
print(test.top())
test.pop()
test.pop()
test.pop()
test.pop()
test.pop()

print(test)
print(test.top())