# # INSERT year
#
# year = int(input("Enter a year:"))
#
# # if divisible by 4 or 400
#
# if year % 4 == 0 or year % 400 == 0:
#     print("It is leap year")
# else:
#     print("it is not leap year")

year = int(input("Enter a year:")) #professor

is_year = False
if is_year % 4 == 0:
    is_year = True
    if is_year % 100 == 0:
        is_year = False
        if is_year % 400 == 0:
            is_year = True

print(is_year)
# if is_year:                          #professor
#     print(f"{year} is leap year")
# else:
#     print(f"{year} is not leap year")
