# This queue is implemented based on fixed-size array
# logic is using turn-around index

class Queue:
    def __init__(self, size):
        self.size = size
        self.arr = [0 for i in range(size)]
        self.r = -1
        self.f = -1
    def isEmpty(self):
        return (self.f == -1)
    def enqueue(self, val):
        if(self.isEmpty()):
            self.r = 0
            self.f = 0
            self.arr[self.r] = val
            return
        else:
            #Full if r = f after increment
            self.r = (self.r + 1)%self.size
            if(self.r == self.f):
                print("Queue is Full")
                self.r = (self.r - 1)%self.size # cannot add anymore, so back to previous position
                return
            else:
                self.arr[self.r] = val
    def dequeue(self):
        if(self.isEmpty()):
            print("Queue is Empty")
            return
        else:
            # Q will be empty if r == f be4 increment
            if(self.f == self.r):
                self.f = -1
                self.r = -1
            else:
                self.f += 1
    def front(self):
        return self.arr[self.f]
    def __str__(self):
        s = "front -> "
        if(not self.isEmpty()):
            if(self.f <= self.r):
                for i in range(self.f, self.r+1):
                    s += str(self.arr[i])
                    s += "-> "
            else:
                for i in range (self.f, self.size + self.r + 1):
                    s += str(self.arr[i]%self.size)
                    s+= "-> "
        s += " rear"
        return s

test = Queue(4)
# test isEmpty & enq
print(test.isEmpty())
for i in range(4):
    test.enqueue(i)
print(test.isEmpty())
print(test)

# test isEmpty & deq
test.dequeue()
test.dequeue()
print(test)
print(test.isEmpty())
test.dequeue()
test.dequeue()
test.dequeue()
print(test)




