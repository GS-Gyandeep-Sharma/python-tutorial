import re

#password strength conditions 
#min 8 characters, digits, upppercase, lowercase, special characters 
def chekcPasswordStrength(password):
    if len(password)<8:
        return "Weak : Password should be minimum 8 characters long"
    if not any(char.isdigit() for char in password):
        return "Weak : Password must contain a digit"
    if not any(char.isupper() for char in password):
        return "Weak : Password must contain an upper character"
    if not any(char.islower() for char in password):
        return "Weak : Password must contain an lower character"
    if not re.search(r'[!@#$%^&*(){}<>.?]',password):
        return "Medium : Password must contain a special character"
    return "Strong : Your password is secured!"

def passwordChecker():
    print("Welcome to password to strength checker")
    while True:
        password = input("Enter your password (type 'exit' for quit)")

        if(password.lower()=='exit'):
            print("Thank you for using tool")
            break
        result = chekcPasswordStrength(password)
        print(result)

#Run the password tool
if __name__ == "__main__":
    passwordChecker()

