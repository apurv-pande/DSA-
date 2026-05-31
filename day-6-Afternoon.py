print("---------------Practise Questions--------------")
lst = [1, 2, 3, 2, 4, 5, 1, 6]
duplicates = []
for i in lst:
    if lst.count(i) > 1 and i not in duplicates:
        duplicates.append(i)
print("Duplicates are:", duplicates)
print()

#sort dictionary by key or values 
#By keys 
mydict = {"a":2,"e":4,"d":7,"c":1,"b":6}
sorted_dict = dict(sorted(mydict.items()))
print(sorted_dict)

#By values
mydict = {'c': 3, 'a': 1, 'b': 2}
sorted_dict = dict(sorted(mydict.items(), key=lambda x: x[1]))
print(sorted_dict)
print()

#remove all elements from a dictionary 
mydict = {'a': 1, 'b': 2, 'c': 3}
mydict.clear()
print(mydict)
print()

print("----------Instance Variable-----------")
#creates a separate memory for each object 
class New: 
    def __init__(self):
        self.a = 10

obj = New()
obj1 = New()
obj2 = New()
obj.a = 20
print(obj.a)
print(obj1.a)
print(obj2.a)
print()

print("-----static variable------")
class New:
    a = 10
    def __init__(self):
        self.name = "oraora"
obj3 = New()
print(obj3.a)
obj4 = New()
print(obj4.a)
New.a = 50
print(obj3.a)
print(obj4.a)
print(New.a)
print()

class College:
    collegename = "modern college"
    def __init__(self):
        self.studentname = "prashant"
principal = College()
teacher = College()
accountant = College()
print("principal", principal.collegename, ".......", principal.studentname)
print("teacher", teacher.collegename, ".......", teacher.studentname)
print("accountant", accountant.collegename, ".......", accountant.studentname)
print()
College.collegename = "HBO"
principal.studentname = "prashant jha"
print("principal", principal.collegename, "|", principal.studentname)
print("teacher", teacher.collegename, "|", teacher.studentname)
print("accountant", accountant.collegename, "|", accountant.studentname)
print()

print("----------------LINKED LIST----------------")
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at end
    def insert(self, data):
        new_node = Node(data)

        # if list is empty
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # Display linked list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
# Create linked list
link = LinkedList()

# Insert elements
link.insert(10)
link.insert(20)
link.insert(30)
link.insert(40)

# Display list
link.display()
print()

#OR
class node:
    def __init__(self, data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
linkedlist = linkedlist()
linkedlist.head = node(5)
second = node(10)
third = node(15) 
fourth = node(20)

linkedlist.head.next = second
second.next = third
third.next = fourth

while linkedlist.head.next != None:
    print(linkedlist.head.data, "|",linkedlist.head.next," -> ",end=" ")
    linkedlist.head = linkedlist.head.next
print()

print("-----LL-----")
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Add node at end
    def add_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    # Add node at beginning
    def add_begin(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    # Add node in between
    def add_between(self, target, value):
        while self.head:
            if self.head.data == target:
                new_node = Node(value)
                new_node.next = self.head.next
                self.head.next = new_node
                if self.head == self.tail:
                    self.tail = new_node
                print("Node inserted successfully")
                return
            self.head = self.head.next
        print("Target node not found")

    # Delete first node
    def delete_begin(self):
        if self.head is None:
            print("Linked List is empty")
            return
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        print("First node deleted")

    # Delete last node
    def delete_end(self):
        if self.head is None:
            print("Linked List is empty")
            return
        if self.head.next is None:
            self.head = None
            self.tail = None
            print("Last node deleted")
            return
        while self.head.next != self.tail:
            self.head = self.head.next
        self.head.next = None
        self.tail = self.head
        print("Last node deleted")

    # Search node
    def search(self, value):
        pos = 1
        while self.head:
            if self.head.data == value:
                print("Node found at position", pos)
                return
            self.head = self.head.next
            pos += 1
        print("Node not found")

    # Count nodes
    def count(self):
        cnt = 0
        while self.head:
            cnt += 1
            self.head = self.head.next
        print("Total nodes:", cnt)

    # Display linked list
    def display(self):
        while self.head:
            print(self.head.data, end=" -> ")
            self.head = self.head.next
        print("None")

if __name__ == '__main__':
    obj = LinkedList()

    while True:
        print("\n====== LINKED LIST MENU ======")
        print("1. Add node at end")
        print("2. Add node at beginning")
        print("3. Add node in between")
        print("4. Delete first node")
        print("5. Delete last node")
        print("6. Search node")
        print("7. Count nodes")
        print("8. Display linked list")
        print("9. Exit")

        ch = int(input("Enter your choice: "))
        if ch == 1:
            value = int(input("Enter value: "))
            obj.add_end(value)
        elif ch == 2:
            value = int(input("Enter value: "))
            obj.add_begin(value)
        elif ch == 3:
            target = int(input("Insert after value: "))
            value = int(input("Enter new value: "))
            obj.add_between(target, value)
        elif ch == 4:
            obj.delete_begin()
        elif ch == 5:
            obj.delete_end()
        elif ch == 6:
            value = int(input("Enter value to search: "))
            obj.search(value)
        elif ch == 7:
            obj.count()
        elif ch == 8:
            obj.display()
        elif ch == 9:
            print("Program exited")
            break
        else:
            print("Invalid choice")