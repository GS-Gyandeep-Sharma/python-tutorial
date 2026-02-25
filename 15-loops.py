#While Loop : Count 0 to 3
count = 0
while count < 4:
    print(f"While loop :{count}")
    count+= 1
else:
    print("While loop ended")

print("----------------------------------------------------")
#For Loop : print each character of Python
language = "Python"
for letter in language:
    print(f"For loop :{letter}")
else:
    print("For loop ended")
print("----------------------------------------------------")
for i in range(5):
    print(f"For loop :{i}")
else:
    print("For loop ended")
print("----------------------------------------------------")
for i in range(5,10):#start,stop
    print(f"For loop :{i}")
else:
    print("For loop ended")
print("----------------------------------------------------")
for i in range(0,10,2):#start,stop,step
    print(f"For loop :{i}")

else:
    print("For loop ended")

#Loop control statements
#pass statement
count = 5

print("----------------------------------------------------")  
while count > 0:
    if(count==3):
        pass
    else:
        print(f"While loop :{count}")
    count-= 1
else:
    print("While loop ended")
  
print("----------------------------------------------------")  
for i in range(5):
    #code add in future
    pass
else:
    print("For loop ended")
print("----------------------------------------------------")  

#break statement
for i in range(5):
    if(i==3):
        break
    else:
        print(i)
else:
    print("For loop ended")
print("----------------------------------------------------")  

#continue
for i in range(5):
    if(i==3):
        continue
    else:
        print(i)
else:
    print("For loop ended")