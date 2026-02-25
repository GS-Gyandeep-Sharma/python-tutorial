numbers = [0,30,20,10,60,50,40,80,90,70]
# list[start:stop:step]
print(numbers[2:6:2])
print(numbers[:2]) #alternative
print(numbers[0::2]) #step is 2
print(numbers[-4:-1]) # start from 4th last and end on last
print(numbers[::-1]) #reverse

#Modifying List

print("changing elementj")
fruits = ["apple","banana","orange"]
fruits[1] = "blueberry"
print(fruits)

print("adding element")
fruits.append("mango")
print(fruits)

print("removing element")
fruits.remove("orange")
print(fruits)

print("extending elemet")
fruits.extend(["watermalon","guava"])
print(fruits)

print("insert element")
fruits.insert(3,"pamogranate")
print(fruits)

print("index element")
index = fruits.index("mango")
print(index)

print("sorting")
numbers.sort()
print(numbers)

print("reverse sorting")
numbers.sort(reverse=True)
print(numbers)

print("sorting stings in list")
fruits.sort()
print(fruits)

print("sorting with a key")
fruits.sort(key=len)
print(fruits)

fruits.sort(key=len,reverse=True)
print(fruits)

print("pop with index")
popped = numbers.pop(2)
print(popped)
print(numbers)

last = numbers.pop()
print(last)
print(numbers)

fruitsCopy = fruits.copy()
print(fruitsCopy)


#join list

list1 = ["a","b","c","d"]
list2 = ["e","f","g","h"]

#method 1
print("Join List")
list3 = list1+list2
print(list3)

#method2 using appned
for x in list2:
    list1.append(x)
print(list1)

#method 3 using extend
list1.extend(list2)
print(list1)

print("Comprehansion list")
#syntex
# newList = [expression for item in iterable if condition]

print("list of square")
square = [x**2 for x in range(1,6)]
print(square)

print("filtering even numbers")
evenNumbers = [x for x in range(1,20) if x%2==0]
print(evenNumbers)

print("applying a function on each element")
upperFruits = [fruit.upper() for fruit in fruits]
print(upperFruits)

nestedList = [[1,2],[3,4],[5,6],[7,8]]
flattenList = []
print("flatten a nested list")
flattenList = [item for sublist in nestedList for item in sublist]
print(flattenList)
