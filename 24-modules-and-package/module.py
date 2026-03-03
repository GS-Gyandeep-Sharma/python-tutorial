import myModule

myModule.sayHello("Gyan")

from myModule import person1

print(person1["name"])

#package : collection of modules and __init__.py file
#library : collection of modules and packages

import math # inbuilt library
A = 16
print(math.sqrt(A))

from math import factorial #import inbult spacific function
print(factorial(5))

#install new module pip install <library_name>