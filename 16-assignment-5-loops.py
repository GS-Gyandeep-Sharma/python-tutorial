#1. Print the While Loop output in same line
#print function have 3 parameters string,saparater(sep)= " ",end = "\n" (line change)
count = 0
countArray = []
while count < 10:
    print(count,end="")
    count += 1

#2. Find factorial of given number

def factorial(num):
    fact = 1
    while num > 1:
        fact *= num
        num -= 1
    return fact

print(f"\nFactorial of 10 is {factorial(10)}")

#3. Count the vowels in string
string = "Would you like me to generate a different version that includes numbers and special characters for a more secure password style string";

def countVowel(string):
    vowelCount = 0
    for letter in string:
        lowerLetter = letter.lower()
        if lowerLetter in "aeiou":
            vowelCount += 1
    return vowelCount
    
print(f"Vowel count is {countVowel(string)}")

#3. Longest word in string
def findLongestWord(string):
    words = string.split()
    longestWord = ""
    for word in words :
        if len(longestWord)<len(word):
            longestWord = word
    return longestWord
print(f"Longest word is {findLongestWord(string)}")

#4. Fabonacci series

def fabonacci(n):
    var1,var2 = 0,1
    count = 0
    while True:
        print(var1,end = " ")
        # var3 = var2
        # var2 = var1+var2
        # var1 = var3
        var1,var2 = var2,var1+var2
        count +=1
        if(count == n):
            break
print("Fabonacci Series - ")
fabonacci(10)