print("--------Practise questions---------")
#Reverse each word in a string 
s = "Hello World"
words = s.split()
for i in range(len(words)):
    words[i] = words[i][::-1]
result = " ".join(words)
print(result)
print()

#check for valid parenthesis 
def valid_parenthesis(s):
    stack = []
    for ch in s:
        if ch in "({[":
            stack.append(ch)
        elif ch == ")":
            if not stack or stack[-1] != "(":
                return False
            stack.pop()        
        elif ch == "}":
            if not stack or stack[-1] != "{":
                return False
            stack.pop()        
        elif ch == "]":
            if not stack or stack[-1] != "[":
                return False
            stack.pop()
    return len(stack) == 0
# Example
s = "{[()]}"
print(valid_parenthesis(s))
print()

print("----------INSERTION SORT------------")
#Algorithm 
#Sort the list [5,3,8,6,2] in ascending order
#start from the second element because a single element is trivially sorted.
#Compare it with elements before it and insert it in the correct position .
#Repeat this process for all elements.
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
    return arr
#input
arr = list(map(int, input("Enter numbers: ").split()))
#sorting
sorted_arr = insertion_sort(arr)
#output
print("Sorted array:", sorted_arr)
print()

print("---------SELECTION SORT----------")
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume current index has minimum value
        min_index = i
        # Find smallest element in remaining array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap elements
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
# Input
arr = list(map(int, input("Enter numbers: ").split()))
# Sorting
sorted_arr = selection_sort(arr)
# Output
print("Sorted array:", sorted_arr)
print()
