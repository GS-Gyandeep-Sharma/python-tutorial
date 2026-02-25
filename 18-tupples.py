#notChangable,orderd,allow duplicate values

#using parantheses()
fruits = ("apple","banana","orange","apple")
print(fruits)

#without parantheses, comma saparated
alsoFruits = "apple","banana","orange","apple"

#using tuple() constructor
newTuple = tuple(("apple","banana","orange","apple"))

#single item

tupleSingle = ("only",)

#tupleOperations

print("Concatenate")
tuple1 = (1,2,3)
tuple2 = (4,5,6)
tuple3 = tuple1+tuple2
print(tuple3)

print("Repeatative")
tuple2 = ("a","b")*2
print(tuple2)

print("cheking")
tuple4 = (1,2,4)
print(2 in tuple4)
print(10 in tuple4)

#Tuple Methods
print("count")
tuple5 = ("red","green","blue","white","red")
print(tuple5.count("red"))

print("index")
print(tuple5.index("green"))

print("len")
numbers = (2,3,4,1)
print(len(numbers))

print("sort")
sortedNumbers = sorted(numbers)
print(sortedNumbers)

print("sum")
print(sum(numbers))

print("min")
print(min(numbers))

print("max")
print(max(numbers))

# packing and unpacking the tuple

a = "Ram"
b = 21
c = "Engineer"
packTuple = a,b,c
print("pack tuple")
print(packTuple)

name,age,profession = packTuple
print("unpack tuple")
print(name)
print(age)
print(profession)