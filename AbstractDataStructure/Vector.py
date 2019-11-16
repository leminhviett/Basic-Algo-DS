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


test = Vector(4)
print(test.elementAtRank(0))
test.insertAtRank(0, 0)
test.insertAtRank(1, 1)
test.insertAtRank(2, 2)
print(test)
test.insertAtRank(2, 5)
print(test)
test.insertAtRank(2, 5)
test.replaceAtRank(1, 3)
print(test)
print((test.topRank))


class PriorityQueue:
    def __init__(self, size):
        self.queue = [-1 for i in range(size)]
        self.size = size
        self.priority = []




