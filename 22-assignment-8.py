#1. Find the intersection (common elements) of two list
def listInsersection(list1,list2):
    commonItems = []
    for item in list1:
        if item in list2 and item not in commonItems:
            commonItems.append(item)
    return commonItems
listA = [1,2,3,4,5]
listB = [3,4,5,6,7]
listC = listInsersection(listA,listB)
print(listC)

#2 find the most frequent element in list
def mostFrequent(lst):
    maxCount = 0
    mostFrequentElement = None
    for item in lst:
        count = lst.count(item)
        if count > maxCount:
            maxCount=count
            mostFrequentElement = item
    return mostFrequentElement
        
listA = [1,1,3,4,5,3,2,5,1,3,5,2,1,1,1]
print(mostFrequent(listA))

#Q3 Find cumlative sum of the list
def cumlativeSum(data):
    result = []
    total = 0
    for item in data:
        total += item
        result.append(total)
    return result
numbers = [1,4,5,7,8,5,33]
print(numbers)
print(cumlativeSum(numbers))

#Q4 Remove Duplicates from list
def removeDuplicates(list):
    result = []
    for item in list:
        if item not in result:
            result.append(item)
    return result
fruits = ["apple","banana","cucumber","pineapple","apple","apple","pineapple","pineapple"]
print(list(set(fruits)))
print(removeDuplicates(fruits))


#Q5 Find the index of an element in a tuple
def findIndex(data,elem):
    for item in data:
        return data.index(elem) if elem in data else -1
numbers = (1,2,3,4,5,6)
index = findIndex(numbers,3)
print(index)

#Q6 Find the most frequent value in dictionary
def mostFrequentInDictionary(dct):
    frequency = {}

    for value in dct.values():
        if value not in frequency:
            frequency[value] = 0
        frequency[value] += 1
    return max(frequency,key = frequency.get)
data = {"a":1,"b":1,"c":2,"d":2,"e":2}
print(mostFrequentInDictionary(data))

#Q7 Merge distionaries with summation
def mergeDictionaries(data1,data2):
    result = data1.copy()
    for key,value in data2.items():
        if(key in result.keys()):
            result[key] += value
        else:
            result[key] = value
    return result

data1 = {"a":100,"b":434,"c":33}
data2 = {"b":100,"c":434,"d":33}
print(mergeDictionaries(data1,data2))

#Q8 Flatten a nested dictionary
def flattenDictionary(data,parentKey = "",sep = "."):
    result = {}
    for key,value in data.items():
        newKey = f"{parentKey}{sep}{key}" if parentKey else key
        if isinstance(value,dict):
            result.update(flattenDictionary(value,newKey))
        else:
            result[newKey]=value
    return result
            
data = {"a":{"b":{"c":42},"d":7},"e":10}
print(flattenDictionary(data))
#output = {'a.b.c':42,'d':7,'e':10}

#Q9 Sort a dictionary by values
def sortByValues(data):
    sortedValues = sorted(data.items(),key = lambda item:item[1])
    return {key:value for key,value in sortedValues}
    
data = {"a":100,"b":434,"c":33}
print(sortByValues(data))

#Q10 Access values from nested dictionary
def findKey(data,targetKey):
    if isinstance(data,dict):
        if targetKey in data:
            return data[targetKey]
        for value in data.values():
            result = findKey(value,targetKey)
            if result is not None:
                return result
    elif isinstance(data,list):
        for item in data:
            result = findKey(item,targetKey)
            if result is not None:
                return result
    return None

data = {
    "level1":{
        "level2":{
            "level3":{
                "value1":10,
                "value2":[1,2,{"deep_key":42}],
                "value3":{"inner_key":"target"}
            },
            "other_key":99,
        },
        "list_key":[
            {"list_inner_key1":88},
            {"list_inner_key2":{"deep_list_key":77}}
        ]
    }
}
print(findKey(data,'deep_key'))
print(findKey(data,'inner_key'))
print(findKey(data,'deep_list_key'))

