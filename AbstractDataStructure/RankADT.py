class Vector:
    #like array but store each element with its rank = its index in array
    def __init__(self, size):
        self.arr = [0 for i in range (size)]
        self.topRank = -1
    def elementAtRank(self, rank):
        if(rank > self.topRank):
            return "No element at rank" + str(rank)
        else:
            return self.arr[rank]
    def replaceAtRank(self, rank, val):
        if (rank > self.topRank):
            return "No element at rank" + str(rank)
        else:
            old = self.arr[rank]
            self.arr[rank] = val
            return old
    def removeAtRank(self, rank):
        if (rank > self.topRank):
            return "No element at rank" + str(rank)
        else:
            old = self.arr[rank]
            for i in range(rank, self.topRank):
                self.arr[i] = self.arr[i + 1]
            return old

    def insertAtRank(self, rank, val):
        if(self.topRank == len(self.arr) - 1):
            print("Vector is Full")
            return
        if (rank > self.topRank + 1):
            return "Cannot perform at rank" + str(rank)
        elif (rank == self.topRank + 1):
            self.arr[rank] = val
            self.topRank = rank
        else:
            self.topRank += 1
            for i in range(self.topRank, rank, -1):
                print(i)
                self.arr[i] = self.arr[i - 1]
            self.arr[rank] = val
    def __str__(self):
        if(self.topRank == -1):
            return ""
        else:
            s =""
            for i in range(self.topRank+1):
                s += str(self.arr[i]) + "-"
            return s


# test = Vector(4)
# print(test.elementAtRank(0))
# test.insertAtRank(0, 0)
# test.insertAtRank(1, 1)
# test.insertAtRank(2, 2)
# print(test)
# test.insertAtRank(2, 5)
# print(test)
# test.insertAtRank(2, 5)
# test.replaceAtRank(1, 3)
# print(test)
# print((test.topRank))

class PriorityQueue:
    def __init__(self, size):
        self.element = [None for i in range(size)]
        self.size = size
        self.top = -1
        self.key = [None for i in range(size)]
    def insertItem(self,k, e):
        if(self.top == self.size - 1):
            print("Queue is Full")
            return
        else:
            self.top += 1
            self.element[self.top] = e
            self.key[self.top] = k
    def minKey(self):
        if(self.top == -1):
            print("Queue is Empty")
            return None
        else:
            min = self.key[0]
            for i in self.key:
                if(min > i):
                    min = i
            return min
    def minElement(self):
        if(self.top == -1):
            print("Queue is Empty")
            return None
        else:
            min = self.element[0]
            for i in self.key:
                if(min > i):
                    min = i
            return self.element[self.key.index(min)]
    def isEmpty(self):
        return self.top == -1
    def size(self):
        return self.size
    def removeMin(self):
        if(self.isEmpty()):
            print("Queue is Empty")
            return None
        else:
            temp = self.minElement()
            index = self.element.index(self.minElement())
            for i in range (index, self.top):
                self.element[i] = self.element[i+1]
                self.key[i] = self.key[i+1]
            self.top -= 1
            return temp
    def __str__(self):
        if(self.isEmpty()):
            return "None"
        k = ""
        e = ""
        for i in range (self.top + 1): #inclusive self.top
            e += str(self.element[i]) + ", "
            k += str(self.key[i]) + ", "
        return "key = \t\t" + k + "\nelement = \t" + e



test = PriorityQueue(4)
test.insertItem(4, 1)
test.insertItem(5, 2)
test.insertItem(10, 1)
test.insertItem(-4, 3)
print(test)

test.insertItem(-4, 3)
print("Min key = ", test.minKey())
print("Min element = ", test.minElement())

print(test.removeMin())
print(test)






