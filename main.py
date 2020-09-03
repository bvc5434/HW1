#Brendan Corso bvc5434@psu.edu

Course1 = input("Enter your course 1 letter grade: ")
if(Course1 == "A"):
  Course_1 = 4.0
elif(Course1 == "A-"):
  Course_1 = 3.67
elif(Course1 == "B+"):
  Course_1 = 3.3
elif(Course1 == "B"):
  Course_1 = 3.0
elif(Course1 == "B-"):
  Course_1 = 2.67
elif(Course1 == "C+"):
  Course_1 = 2.33
elif(Course1 == "C"):
  Course_1 = 2.0
elif(Course1 == "D"):
  Course_1 = 1.0
else:
  Course_1 = 0.0
Credit1 = input("Enter your course 1 credit: ")
print(f"Grade point for course 1 is: {Course_1}")
Course_1=float(Course_1)
Credit1=float(Credit1)
Course2 = input("Enter your course 2 letter grade: ")
if(Course2 == "A"):
  Course_2 = 4.0
elif(Course2 == "A-"):
  Course_2 = 3.67
elif(Course2 == "B+"):
  Course_2 = 3.3
elif(Course2 == "B"):
  Course_2 = 3.0
elif(Course2 == "B-"):
  Course_2 = 2.67
elif(Course2 == "C+"):
  Course_2 = 2.33
elif(Course2 == "C"):
  Course_2 = 2.0
elif(Course2 == "D"):
  Course_2 = 1.0
else:
  Course_2 = 0.0
Credit2 = input("Enter your course 2 credit: ")
print(f"Grade point for course 2 is: {Course_2}")
Course_2=float(Course_2)
Credit2=float(Credit2)
Course3 = input("Enter your course 3 letter grade: ")
if(Course3 == "A"):
  Course_3 = 4.0
elif(Course3 == "A-"):
  Course_3 = 3.67
elif(Course3 == "B+"):
  Course_3 = 3.3
elif(Course3 == "B"):
  Course_3 = 3.0
elif(Course3 == "B-"):
  Course_3 = 2.67
elif(Course3 == "C+"):
  Course_3 = 2.33
elif(Course3 == "C"):
  Course_3 = 2.0
elif(Course3 == "D"):
  Course_3 = 1.0
else:
  Course_3 = 0.0
Credit3 = input("Enter your course 3 credit: ")
print(f"Grade point for course 3 is: {Course_3}")
Course_3=float(Course_3)
Credit3=float(Credit3)
GPA = (Course_1*Credit1+Course_2*Credit2+Course_3*Credit3)/(Credit1+Credit2+Credit3)
print(f"Your GPA is: {GPA}")