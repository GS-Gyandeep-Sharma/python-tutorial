print("I am %s and I am %d years old" % ("John", 30))
print("I'm the best")
print('''"Double Quots"''')
print("\"Double Quots\"")
print("I am {0} and I am {1} years old".format("John", 30))
print("I am {name} and I am {age} years old".format(name="John", age=30))

name = "John"
age = 30
print(f"I am {name} and I am {age} years old")

#Escape Characters
print("Hello\nWorld") #New Line
print("Hello\tWorld") #Tab
print("Hello\rWorld") #Carriage Return
print("Hello\bWorld") #Backspace
print("Hello\fWorld") #Form Feed
print("Hello\vWorld") #Vertical Tab
print("\"Quotes\" and 'single quotes' can be tricky")#single and double quotes


#Sting Operaters
print("Hello" + "World")#Concatenation
print("Hello " * 3)#Repetition
name = "John"
print("Sting indexing",name[0]) #Indexing
print("Sting indexing",name[-1]) # Negative Indexing
print("Hello"[1:4])#Slicing
print("Hello"[1:4:2])#Slicing with step, start, end, steps 
print("Hello"[1:4:-1])#Slicing with step
print("Hello"[::-1])#Reverse
print("H" in "Hello")#Membership
print("H" not in "Hello")#Membership
if("H" in "Hello"):
    print("H is in Hello")
else:
    print("H is not in Hello")

string = "      hello, gyandeep          "
print(string.upper()) #Upper Case
print(string.lower()) #Lower Case
print(string.title()) #Title Case
print(len(string)) #len
print(string.count('e')) #count
print(string.find('g')) #find
print(string.split(',')) #split
print(string.split()) #split
print(string.replace('hello', 'hi')) #replace
print(string.startswith('hello')) #startswith
print(string.endswith('p')) #endswith
print(string.strip()) #strip
sting1 = ["My","name","is","Gyandeep"];
print(" ".join(sting1)) #strip