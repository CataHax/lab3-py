# INPUT a string

x = input("Tell me somwthing, anything! PLEASEEEE!:")
print(x)

# contains only letters
if x.isalpha():
    print("contains only letters")

if x.isupper():
    print("contains only uppercase letters")

if x.islower():
    print("contains only lowercase letters")

if x.isdigit():
    print("contains only digits")

if x.isalnum():
    print("only letters and numbers")

if x[0].isupper():
    print("first letter is upper")

if x[-1] == ".":
    print("ends with a period")
