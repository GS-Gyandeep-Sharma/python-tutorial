#create or define function
def greetings():
    print("Hello, welcome to our function")

#call function
greetings()


#function to add two numbers
def add_numbers(num1, num2):
    result = num1 + num2
    print('Sum of',num1,'and',num2,'is',result)


add_numbers(10, 20)

add_numbers(num1=30,num2=40)

add_numbers(num2=30,num1=40) #interchange parameters

#pass function

def pass_function():
    pass

pass_function()