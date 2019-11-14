class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    def __str__(self):
        return str(self.data)

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    def insertTail(self,val):
        if(self.head == None):
            self.head = Node(val)
        else:
            current = self.head
            while(current.next != None):
                current = current.next
            newNode = Node(val)
            current.next = newNode
    def __str__(self):
        s = ""
        current = self.head
        while(current != None):
            s += str(current.data) + "-> "
            current = current.next
        s += "None"
        return s
    def insertHead(self,val):
        if(self.head == None):
            self.head = Node(val)
        else:
            newNode = Node(val)
            newNode.next = self.head
            self.head = newNode
    def deletionTail(self):
        if (self.head == None):
            print("LinkedList is Empty")
            return
        else:
            current = self.head
            if(current.next == None):
                self.head = None
                return
            while (current.next.next != None):
                current = current.next
            current.next = None


test = SinglyLinkedList()
print(test)
test.insertTail(0)
test.insertTail(1)
test.insertTail(2)
print(test)

test.insertHead(-1)
print(test)
test.deletionTail()
print(test)
test.deletionTail()
test.deletionTail()
test.deletionTail()
test.deletionTail()

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    def insertTail(self, val):
        if(self.head == None):
            self.head = Node(val)
        else:
            current = self.head
            while(current.next != None):
                current = current.next
            newNode = Node(val)
            current.next = newNode
            newNode.prev= current
    def __str__(self):
        s = ""
        current = self.head
        while(current != None):
            s += str(current.data) + "<-> "
            current = current.next
        s += "None"
        return s




