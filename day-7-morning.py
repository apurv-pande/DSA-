print("------Practice Questions------")

print("----------RECURSION-----------")
#when the main problem can be divided into similar sub problems then we can use the recursion
#if we have to perfrom depth first search , pre order , post order 
#recursion uses stack memory hence we try to avoid recursion
#ease to code , space efficiency as well as time efficiency is better in iteration than in recursion
#has a base criteria that stops it 
def factorial(num):
    if num < 1:
        return 1
    return num * factorial(num - 1)
print(factorial(4))
print()

def capitalisation(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0][0].upper() + arr[0][1:])
    return result + capitalisation(arr[1:])
print(capitalisation(['car','taco','banana']))
print()

def power(base,exponent):
    if exponent == 0:
        return 1
    return base * power(base , exponent-1)
print(power(2,0))
print(power(2,2))
print(power(2,4))
print(power(2,5))
print()

def productofarray(arr):
    if len(arr) == 0:
        return 1
    return arr[0] * productofarray(arr[1:])
print(productofarray([1,2,3]))
print(productofarray([1,2,3,10])) 
print()

def reverse(string):
    if len(string) <= 1:
        return string
    return string[len(string)-1] + reverse(string[0:len(string)-1])
print(reverse('python'))
print(reverse('appallers'))
print(reverse('a'))
print()

def recursiverange(num):
    if num <= 0:
        return 0
    return num + recursiverange(num - 1)
print(recursiverange(6))
print()

def isPalindrome(string):
    if len(string) == 0:
        return True
    if string[0] != string[len(string)-1]:
        return False
    return isPalindrome(string[1:-1])
print(isPalindrome('hannah'))
print()

def someRecursion(arr , cb):
    if len(arr) == 0:
        return False
    if not(cb(arr[0])):
        return someRecursion(arr[1:], cb)
    return True
def isOdd(num):
    if num%2==0:
        return False
    else:
        return True
    
print(someRecursion([1,2,3,4],isOdd))
print(someRecursion([4,6,8,9],isOdd))
print(someRecursion([4,6,8],isOdd))