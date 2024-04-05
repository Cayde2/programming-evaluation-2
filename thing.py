#This is a code that asks the user to input their grades for 4 different courses and outputs their average and letter grade.
#The following table was used to determine the letter grade:

#Letter	Percent
#A+	95–100%
#A	87–94%
#A−	80–86%
#B+	77–79%
#B	72–76%
#B−	70–71%
#C+	67–69%
#C	63-66%
#C-	61-62%
#D+	57–60%
#D	54–56%
#D−	50–53%
#F	0–49%

print("Hello I will tell you your average for the year.")
cOne = float(input("What is your first class grade?:    "))
cTwo = float(input("What is your second class grade?:   "))
cThree = float(input("What is your third class grade?:    "))
cFour = float(input("What is your fourth class grade?:   "))
average = (cOne + cTwo + cThree + cFour)/4

if average >= 95:
  print("You have an average of", average, ", which is an A+")

elif average >= 87:
  print("You have an average of", average, ", which is an A")

elif average >= 80:
  print("You have an average of", average, ", which is an A-")

elif average >= 77:
  print("You have an average of", average, ", which is a B+")

elif average >= 72:
  print("You have an average of", average, ", which is a B")

elif average >= 70:
  print("You have an average of", average, ", which is a B-")

elif average >= 67:
  print("You have an average of", average, ", which is a C+")

elif average >= 63:
  print("You have an average of", average, ", which is a C")

elif average >= 61:
  print("You have an average of", average, ", which is a C-")

elif average >= 57:
  print("You have an average of", average, ", which is a D+")

elif average >= 54:
  print("You have an average of", average, ", which is a D")

elif average >= 50:
  print("You have an average of", average, ", which is a D-")

elif average < 50:
  print("You have an average of", average, ", which is an F")

#The following lines of code output if you are doing well, great, poorly, or failing:
if average >= 85:
  print("You are doing great!")

elif average >= 70:
  print("You are doing okay.")

elif average >= 50:
  print("You are doing poorly.")

elif average < 50:
  print("You are failing.")
