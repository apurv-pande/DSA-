print("------IMPLEMENTATION OF LL USING STACK-------")
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next 
            
class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()
    def isEmpty(self):
        return self.LinkedList.head is None
    def __str__(self):
        values = []
        current = self.LinkedList.head
        while current:
            values.append(str(current.value))
            current = current.next
        return '\n'.join(values)
    def pop(self):
        if self.isEmpty():
            return "There is no element in the stack."
        nodeValue = self.LinkedList.head.value
        self.LinkedList.head = self.LinkedList.head.next
        return nodeValue
    def peek(self):
        if self.isEmpty():
            return "There is no element in the stack."
        return self.LinkedList.head.value
    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node
    def delete(self):
        self.LinkedList.head = None

# Driver Code
customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)
print("Top Element:", customStack.peek())
print("Popped Element:", customStack.pop())
print("\nAfter Pop:")
print(customStack)
print()

print("---------ENQUEUE - DEQUEUE---------")
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

class Queue:
    def __init__(self):
        self.LinkedList = LinkedList()
    def __str__(self):
        values = [str(x) for x in self.LinkedList]
        return ' '.join(values)
    def enqueue(self, value):
        newnode = Node(value)
        if self.LinkedList.head is None:
            self.LinkedList.head = newnode
            self.LinkedList.tail = newnode
        else:
            self.LinkedList.tail.next = newnode
            self.LinkedList.tail = newnode
    def isEmpty(self):
        return self.LinkedList.head is None
    def dequeue(self):
        if self.isEmpty():
            return "There is not any node in the queue."
        else:
            tempnode = self.LinkedList.head
            if self.LinkedList.head == self.LinkedList.tail:
                self.LinkedList.head = None
                self.LinkedList.tail = None
            else:
                self.LinkedList.head = self.LinkedList.head.next
            return tempnode
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.LinkedList.head
    def delete(self):
        self.LinkedList.head = None
        self.LinkedList.tail = None

# Testing
custQueue = Queue()
custQueue.enqueue(1)
custQueue.enqueue(2)
custQueue.enqueue(3)
print(custQueue)
print("Dequeued:", custQueue.dequeue())
print(custQueue)
print("Peek:", custQueue.peek())
print("Dequeued:", custQueue.dequeue())
print(custQueue)
print("Peek:", custQueue.peek())
print("Dequeued:", custQueue.dequeue())
print(custQueue)
print("Peek:", custQueue.peek())
print()

