userName = "gyandeep";
password = "123456";

userInputName = input("Enter your name: ");
userInputPassword = input("Enter your password: ");

if(userInputName == userName and userInputPassword == password):
    print("Both username and password are correct")
elif(userInputName == userName and userInputPassword != password):
    print("Username is correct but password is incorrect")
else:
    print("Login failed")