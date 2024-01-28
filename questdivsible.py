num = int(input("Enter any number "))
if num % 5 == 0:
    print("its num is divisible by 15")
else:
    if num % 3 == 0 or num % 5==0:
        print("this num is divisible by 3 or 5")
    else:
        print("number is neither divisible by 3 or 5")