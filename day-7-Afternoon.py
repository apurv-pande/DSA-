print("-------Practice Question--------")
# n = int(input())
# arr = list(map(int, input().split()))
# # Sort the array
# arr.sort()
# # Product of two largest numbers
# p1 = arr[-1] * arr[-2]
# # Product of two smallest numbers
# # (useful when both are negative)
# p2 = arr[0] * arr[1]
# # Choose the pair with maximum product
# if p1 >= p2:
#     print(arr[-1] + arr[-2])
# else:
#     print(arr[0] + arr[1])
# print()

print("--------TREE IMPLEMENTATION---------")
#We can implement tree data structure by using array or lists
class Tree:
    def __init__(self, data):
        self.data = data
        self.child = []

    def addchild(self, obj):
        self.child.append(obj)
        print("New node added.")

    def printTree(self, level=0):
        print(" " * level + self.data)
        for child in self.child:
            child.printTree(level + 4)
            
rootNode = Tree("Drinks")
Hot = Tree("Hot")
Cold = Tree("Cold")
Tea = Tree("Tea")
Coffee = Tree("Coffee")
Alco = Tree("Alcoholic")
NonAl = Tree("Non-Alcoholic")

rootNode.addchild(Hot)
rootNode.addchild(Cold)
Hot.addchild(Tea)
Hot.addchild(Coffee)
Cold.addchild(Alco)
Cold.addchild(NonAl)

rootNode.printTree()
print()

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    # Add child node
    def add_child(self, child):
        self.children.append(child)

    # Print tree
    def print_tree(self, level=0):
        print(" " * level * 4 + self.data)

        for child in self.children:
            child.print_tree(level + 1)

# Creating nodes
N1 = TreeNode("N1")
N2 = TreeNode("N2")
N3 = TreeNode("N3")
N4 = TreeNode("N4")
N5 = TreeNode("N5")
N6 = TreeNode("N6")
N7 = TreeNode("N7")
N8 = TreeNode("N8")

# Building tree
N1.add_child(N2)
N1.add_child(N3)
N2.add_child(N4)
N2.add_child(N5)
N3.add_child(N6)
N4.add_child(N7)
N4.add_child(N8)

# Print tree
print("Tree Structure:")
N1.print_tree()
print()

print("------Array rotation-------")
def rotateArray(arr, k):
    n = len(arr)
    k = k % n
    rotated = arr[-k:] + arr[:-k]
    return rotated
arr = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter number of steps: "))
result = rotateArray(arr, k)
print("Rotated Array : ",result)