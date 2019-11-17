from AbstractDataStructure.LinkedList import SinglyLinkedList

class HashTable:
    def __init__(self, size):
        self.table = [SinglyLinkedList() for i in range(size)]
    def hashFunc(self, val):
        #hash func = val mod N
        return val%len(self.table)
    def __str__(self):
        s = ""
        for i in range (len(self.table)):
            s += str(i) + "-> " + str(self.table[i]) + "\n"
        return s
    def addVal(self, val):
        self.table[self.hashFunc(val)].insertTail(val)

# test = HashTable(5)
# print(test)
# for i in range (20):
#     test.addVal(i)
# print(test)

class HashTable2:
    def __init__(self, size):
        self.table = [None for i in range(size)]
    def hashFunc(self, val):
        #hash func = val mod N
        return val%len(self.table)
    def __str__(self):
        s = ""
        for i in self.table:
            s += str(i) + ", "
        return s
    def isFull(self):
        for i in self.table:
            if (i == None):
                return False
        return True
    def addVal(self, val):
        if(self.isFull()):
            print("Table is Full")
            return
        index = self.hashFunc(val)

        while(True):
            if(self.table[index] == None):
                self.table[index] = val
                return
            else:
                index += 1


# test2 = HashTable2(5)
# print(test2)
# test2.addVal(3)
# test2.addVal(8)
# test2.addVal(5)
# print(test2)
