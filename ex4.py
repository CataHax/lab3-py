# INPUT the day and the month


x = int(input("Enter the day:"))


y = int(input("Enter the month:"))

# day 21




# IF

if  y == 1 or y == 3 or y == 2:
    print("Winter")
elif 4 <= y <= 6:
    print("Spring")
elif y in range (7,10):
    print("Summer")
elif y in range(10,13):
    print("Fall")
else:
    print("Ma'am, there are only 12 months")

if y % 3 == 0 and x >= 21:
    if y == "Winter":
        y = "Spring"
    elif y == "Spring":
        y = "Summer"
    elif y == "Summer":
        y = "Fall"
    else:
        y = "Winter"
