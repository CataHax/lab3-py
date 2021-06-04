# INPUT a letter and a +/- sign if necessary


letters = ["A","B","C","D","F"]
num = list((range(5,0,-1)))
#print(num)
grade_letter = input("Enter the grade:")
# for i in range(len(letters)):
#     if grade_letter == letters[i]:
#         print(num[i]-1)

c = 0.3
if grade_letter == "A":
     print(num[1])
if grade_letter == "A-":
     print(num[1]-c)
if grade_letter == "A+":
     print(num[1]+c)
elif grade_letter == "B":
     print(num[1])
elif grade_letter == "C":
     print(num[2])
elif grade_letter == "D":
     print(num[3])
elif grade_letter == "F":
     print(num[4])
