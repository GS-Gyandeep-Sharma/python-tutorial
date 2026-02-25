# Create set in python
# using curly braces {}
vowels = {"a","e","i","u"}
print(vowels)

# using the set() constructor
numbers = set([1,2,3,4,5])
print(numbers)

#create empty set
emptySet = set()
print(emptySet)

#Set Operations 

print("Add")
fruits = {"apple","banana","orange"}
fruits.add("cherry")
print(fruits)

print("Remove - raise error if element not found")
fruits = {"apple","banana","orange"}
fruits.remove("apple")
print(fruits)

print("Discard - do not raise error if element not found")
fruits = {"apple","banana","orange"}
fruits.remove("banana")
print(fruits)

#Set Mothods
setA = {1,2,3,4,5}
setB = {3,4,5,6,7}
print("Union") #Combine elements of two sets
setC = setA.union(setB)
print(setC)

print("Intersection") #Pick common elements of two sets
setC = setA.intersection(setB)
print(setC)

print("Difference") #Element present in first set but not in second
setC = setA.difference(setB)
print(setC)

print("Symmetric Difference") #exclude common elements
setC = setA.symmetric_difference(setB)
print(setC)

print("Set Comprehensions")
#Syntex
#newSet = {expression for item in iterable if condition}
squares = {x**2 for x in range(1,6)}
print(squares)
