num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
num3=int(input("enter the third number:"))

if num1>num2 and num1>num3:
    print("first number is maximum:",num1)
elif num2>num1 and num2>num3:
    print("second number is maximum:",num2)
else:
    print("third number is maximum:",num3)
