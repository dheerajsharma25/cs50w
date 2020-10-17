import sys
try:
    x= int(input("x: "))
    y= int(input("y: "))
except ValueError:
    print("cant be the string")
    sys.exit(1)

try:
    result = x/y
except ZeroDivisionError:
    print("cant divide by zero")
    sys.exit(1)

print(f"{x}/{y} = {result}")