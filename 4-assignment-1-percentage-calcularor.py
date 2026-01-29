print("Percentage of student");
name = input("Enter your full name: ");
physicsMarks = int(input("Enter your marks in physics out of 100: "));
chemistryMarks = int(input("Enter your marks in chemistry out of 100: "));
mathsMarks = int(input("Enter your marks in maths out of 100: "));

total = 300;
markesOptained = physicsMarks + chemistryMarks + mathsMarks;
percentage = int((markesOptained / total) * 100);
print("Name: ", name);
print("Physics Marks out of 100: ", physicsMarks);
print("Chemistry Marks out of 100: ", chemistryMarks);
print("Maths Marks out of 100: ", mathsMarks);
print("Total Marks: ", total);
print("Markes Obtained out of 300: ", markesOptained);
print("Percentage: ", percentage);
if(percentage>70):
    print("You are pass with first division")
elif(percentage>40 and percentage<70):
    print("You are pass with second division")
elif(percentage>33 and percentage<40):
    print("You are pass with third division")
else:
    print("You are fail")
