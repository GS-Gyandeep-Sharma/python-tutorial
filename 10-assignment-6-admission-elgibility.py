print("Enter PCM marks out of 100");

mathMarks = int(input("Enter your marks in maths: "))
physicsMarks = int(input("Enter your marks in physics: "))
chemistryMarks = int(input("Enter your marks in chemistry: "))


minMathMarks = 65
minPhysicsMarks = 55
minChemistryMarks = 50
minPassingMarks = 180
minPassingMathPhysicsMarks = 140

TotalPMMarks = mathMarks + physicsMarks
TotalPCMMarks = TotalPMMarks + chemistryMarks

print("Total Physics - Math marks: ", TotalPMMarks)
print("Total Physics, Chemistry and Math marks: ", TotalPCMMarks)

if(mathMarks >= minMathMarks and physicsMarks >= minPhysicsMarks and chemistryMarks >= minChemistryMarks and ( TotalPCMMarks >= minPassingMarks or TotalPMMarks >= minPassingMathPhysicsMarks)):
    print("You are eligible for admission")
else:
    print("You are not eligible for admission")
    