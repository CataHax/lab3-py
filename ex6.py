# INPUT grades
grade1 = float(input("grades:"))
grade2 = float(input("grades:"))
grade3 = float(input("grades:"))

# Average
x = (grade1 + grade2 + grade3)/3

# print two more digits after the dot
print(f'{x:.2f}')

# CONSTRICTIONS

if 3.85 < x < 4.00:
    print("A")
elif 2.85 < x < 3.85:
    print("B")
elif 1.85 < x < 2.85:
    print("C")
elif 0.85 < x < 1.85:
    print("D")
elif x < 0.85:
    print("F")
else:
    print("Only from 0-4")
