#1. limit the decimal places to 2 using .format()
piValue = 3.141592653589793
print("The value of pi is {0:.2f}".format(piValue))

#2. Extract characters from index 2 to 8 with steps of 2
string = "Python Course"
print(string[2:8:2])

#3. Slice to get only middle character(s)
def middle(word):
    count = len(word)
    middleNum =  int(count/2)
    if count%2==0:
        return word[(middleNum-1):(middleNum+1)]
    else:
        return word[middleNum   ]

print(middle("Madhav"))
print(middle("Madhava"))
#4. Remove first 3 and last three characters
string = "Regression Analysis"
print(string[3:-3])

#5. Get the substring that start 4 characters from the end to the last characters
string = "Classification"
print(string[-4:])

#6. How to reverse a string using Python string method
string = "Classification New"
print(string[::-1])

#7. Write a python function to check if string is a palingdrom using string function

def checkPalingdraom(input):
    if input[::-1]==input:
        return "Yes"
    else:
        return "No"

string = "Russia"
print(string," is pilingdrom : ",checkPalingdraom(string))
string = "MOM"
print(string," is pilingdrom : ",checkPalingdraom(string))