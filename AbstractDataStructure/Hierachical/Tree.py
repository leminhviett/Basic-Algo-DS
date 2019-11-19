class Node:
    def __init__(self, parent, data, node_l, node_r):
        self.parent = parent
        self.node_l = node_l
        self.node_r = node_r
        self.data = data

def preOrder(root):
    if(root != None):
        print(root.data, end=", ")
        preOrder(root.node_l)
        preOrder(root.node_r)

class BinTree:
    def __init__(self):
        self.root = Node(None, None, None, None)
        self.store = ""
    def insert(self, node_inserting, current_root = None):
        if(self.root.data == None):
            self.root = node_inserting
            return

        if(current_root == None):
            current_root = self.root
        if(current_root.data == None):
            node_inserting.parent = current_root
            current_root.data = node_inserting.data
        else:
            if(current_root.data < node_inserting.data):
                if(current_root.node_r == None):
                    node_inserting.parent = current_root
                    current_root.node_r = node_inserting

                else:
                    self.insert(node_inserting, current_root = current_root.node_r)
            else:
                if (current_root.node_l == None):
                    node_inserting.parent = current_root
                    current_root.node_l = node_inserting
                else:
                    self.insert(node_inserting, current_root = current_root.node_l)
    def __str__(self):
        self.store = ""
        def preOrder(root='special_char'):
            if (root == 'special_char'):
                root = self.root
            if (root != None):
                self.store += str(root.data) + ", "
                preOrder(root.node_l)
                preOrder(root.node_r)
        preOrder()
        return self.store

    #TODO: deltion for Binary tree
    def subDel(self, node_ref):
        # Delete node having 1/0 child
        if (node_ref.node_l == None):
            child = node_ref.node_r
        else:
            child = node_ref.node_l

            ##del Root
        if (node_ref == self.root):
            if (child != None):
                child.parent = None
                return
            ## del internal node
        if (node_ref.parent.node_l == node_ref):
            node_ref.parent.node_l = child
        else:
            node_ref.parent.node_r = child
        if (child != None):
            child.parent = node_ref.parent
            return
        else:
            # del external node (leaves)
            # this case child == None
            node_ref.parent = None
    def deleteNode(self, node_ref):
        if(node_ref.node_l == None or node_ref.node_r == None):
            self.subDel(node_ref)
        else:
            min_refRight = node_ref.node_r
            while(min_refRight.node_l != None):
                min_refRight = min_refRight.node_l #assign most left of node_ref.node_r

            node_ref.data = min_refRight.data #replace node_ref with node min
            self.subDel(min_refRight)








# root = Node(None, 5, None, None)
# node1 = Node(root, 3, None, None)
# node2 = Node(root, 8, None, None)
# root.node_l = node1
# root.node_r = node2
#
# node1_1 = Node(node1, 31, None, None)
# node1_2 = Node(node1, 13, None, None)
# node1.node_l = node1_1
# node1.node_r = node1_2
#
# preOrder(root)

test = BinTree()
n1 = Node(None, 5, None, None)
n2 = Node(None, 2, None, None)
n3 = Node(None, 8, None, None)
n4 = Node(None, 4, None, None)
n5 = Node(None, 15, None, None)
n6 = Node(None, 3, None, None)
n8 = Node(None, 7, None, None)
n9 = Node(None, 10, None, None)
n10 = Node(None, 12, None, None)
n11 = Node(None, 9, None, None)


test.insert(n1)
test.insert(n2)
test.insert(n3)
test.insert(n4)
test.insert(n5)
test.insert(n6)
test.insert(n8)
test.insert(n9)
test.insert(n10)
test.insert(n11)

# preOrder(test.root)
# print()

#test Del node func
print(test)
test.deleteNode(n4)
print(test)
test.deleteNode(n6)
print(test)
test.deleteNode(n3)
print(test)

test.deleteNode(n1)
print(test)







