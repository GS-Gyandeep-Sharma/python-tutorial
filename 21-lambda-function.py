#syntex
#lambda arguments:expressions

print("add two numbers using lambda function")
add = lambda x,y:x+y
print(add(12,32))

print("Custom sorting - Sort a list of tuples by the second element")
data = [(1,'b'),(3,'a'),(2,'c')]
sortedData = sorted(data,key=lambda x:x[1])
print(sortedData)