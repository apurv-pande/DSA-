print("-------Practice Questions---------")
#remove leading zeroes from a list of integers 
mylist = [0,0,1,2,3,0,5,0,9]
while len(mylist) > 0 and mylist[0] == 0:
    mylist.pop(0)
print(mylist)
print()

#Find the first missing positive integer
mylist = [3, 4, -1, 1]
positive_numbers = []
# store only positive numbers
for num in mylist:
    if num > 0:
        positive_numbers.append(num)
# start checking from 1
missing = 1
while missing in positive_numbers:
    missing += 1
print(missing)
print()

print("---------TYPES OF TREES----------")
print("# FULL BINARY TREE")
print("1. Each node has either 0 or 2 children and no node has a single child.")
print()
print("# Complete Bianry Tree")
print("1. All levels except the possibly the last are completely filled.")
print("2. Nodes in the last level are filled from left to right.")
print()
print("# Perfect Binary Tree")
print("1. All internal nodes have exactly two nodes")
print("2. All leaf nodes are at the same level.")
print()

print("-----------OPERATIONS ON TREE-----------")
print(" 1. Creation of tree \n 2. Insertion of Node \n 3. Deletion of node \n 4. Deletion of tree \n 5. Search of a node \n 6. Traversal in Tree ")
print()

print("Binary search tree performs faster than binary tree while insertion and deletion. ")
class BST:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None

    def insert(self, nodevalue):
        if self.data is None:
            self.data = nodevalue
            return

        # Left subtree
        if nodevalue <= self.data:
            if self.leftchild is None:
                self.leftchild = BST(nodevalue)
            else:
                self.leftchild.insert(nodevalue)

        # Right subtree
        else:
            if self.rightchild is None:
                self.rightchild = BST(nodevalue)
            else:
                self.rightchild.insert(nodevalue)
def preorder(root):
    if root is None:
        return
    print(root.data, end=" ")
    preorder(root.leftchild)
    preorder(root.rightchild)

def postorder(root):
    if root is None:
        return
    postorder(root.leftchild)
    postorder(root.rightchild)
    print(root.data , end=" ")
def inorder(root):
    if root is None:
        return 
    inorder(root.leftchild)
    print(root.data , end=" ")
    inorder(root.rightchild)  
    
# Function to search a node in BST
def search(root, value):
    if root is None:
        return False
    if root.data == value:
        return True
    elif value < root.data:
        return search(root.leftchild, value)
    else:
        return search(root.rightchild, value)
    
# Function to print tree
def printTree(root, space=0, level_space=5):
    if root is None:
        return
    # Print right child first
    printTree(root.rightchild, space + level_space)
    # Print current node
    print()
    print(" " * space + str(root.data))
    # Print left child
    printTree(root.leftchild, space + level_space)


# Create BST
newBST = BST(None)

# Insert nodes
newBST.insert(70)
newBST.insert(50)
newBST.insert(90)
newBST.insert(30)
newBST.insert(60)
newBST.insert(80)
newBST.insert(100)
newBST.insert(20)
newBST.insert(40)

# Print tree
printTree(newBST)
print("Preorder Traversal : ")
preorder(newBST)
print()

print("Inorder Traversal : ")
inorder(newBST)
print()

print("Postorder Traversal : ")
postorder(newBST)

print()
if search(newBST, 20):
    print("Node Found")
else:
    print("Node Not Found")
if search(newBST, 60):
    print("Node Found")
else:
    print("Node Not Found")

