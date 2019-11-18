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
    def insert(self, val, current_root = None):
        if(current_root == None):
            current_root = self.root

        if(current_root.data == None):
            current_root.data = val
        else:
            if(current_root.data < val):
                if(current_root.node_r == None):
                    current_root.node_r = Node(current_root.node_r, val, None, None)
                else:
                    self.insert(val, current_root = current_root.node_r)
            else:
                if (current_root.node_l == None):
                    current_root.node_l = Node(current_root.node_l, val, None, None)
                else:
                    self.insert(val, current_root=current_root.node_l)
    def __str__(self):
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
test.insert(val=5)
test.insert(val=8)
test.insert(val=10)
test.insert(val=1)
test.insert(val=90)
test.insert(val=-5)
test.insert(val=-8)

test.insert(val=-0)


preOrder(test.root)
print()
print(test)








