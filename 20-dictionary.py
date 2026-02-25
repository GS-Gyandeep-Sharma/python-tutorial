#We create dictionary using curly braces{} and saparating keys and values by colon.

newDictionary = {"key1":"value1","key2":"value2","key3":"value3"} #syntex
newDictionary1 = dict({"key1":"value1","key2":"value2","key3":"value3"}) #using dict() Constructor
newDictionary2 = dict([("key1","value1"),("key2","value2"),("key3","value3")]) #using a list of tuples
emptyDictionary = {} #empty dictionary

#Dictionary with data

dataDictionary = {
    "course":"Python",
    "instructor":"Ram",
    "level":"Beginner"
}
print(dataDictionary['course'])

#Dictionary Methods 
print("keys")
print(dataDictionary.keys())

print("values")
print(dataDictionary.values())

print("items")
print(dataDictionary.items())

print("get")
print(dataDictionary.get("course"))

#Add, Modify and Remove items

print("Add")
dataDictionary["language"] = "hindi"
print(dataDictionary)


print("Modify")
dataDictionary["level"] = "high"
print(dataDictionary)


print("remove")
del dataDictionary["language"]
print(dataDictionary)

print('remove with pop')
instructor = dataDictionary.pop("instructor")
print(instructor)

print("nested dictionary")
nestedDictionary = {
    "student1":{
        "name":"stu1",
        "class":"9",
        "grade":"a"
    },
    "student2":{
        "name":"stu2",
        "class":"93",
        "grade":"b"
    },
    "student3":{
        "name":"stu3",
        "class":"94",
        "grade":"c"
    }
}
print(nestedDictionary)

#Dictionary comprehension
#syntex
#newDic = {key_expression:value_expression for item in iterable if condition}

square = {x:x*x for x in range(1,6)}
print(square)

