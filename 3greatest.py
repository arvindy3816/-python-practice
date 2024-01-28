number1 = int(input("enter first number1: 1"))
number2 = int(input("enter second number2: "))
number3 = int(input("enter third number3: "))


if number1>number2 and number1>number3:
    print("number first is a greatest")

elif number2>number1 and number2>number3:
    print("second number is greater")

else:
    print("third number is greater")