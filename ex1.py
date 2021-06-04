x1 = int(input("Enter the first number:"))

x2 = int(input("Enter the second number:"))

x3 = int(input("Enter the third number:"))

# now I must do three "if-s"


if x3 > x2 > x1:
    print("increasing")

elif x1 > x2 > x3:
    print("decreasing")

else:
    print("nothing")
