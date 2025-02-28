#positive or negative
num1 = float(input("Enter a number:"))

if num1 > 0:
    print("+ve")
elif num1 == 0:
    print("0")
else:
    print("-ve")

#odd or even
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("num is Even")
else:
    print("num is Odd")

#eligible to vote
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

#greatest of two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 > num2:
    print("The greatest number is num1")
elif num2 > num1:
    print("The greatest number is num2.")
else:
    print("Both numbers are equal.")

#pass or fail
n = int(input("Enter marks:"))

if n >= 40:
    print("pass")
else:
    print("fail")

#days of a week
day = int(input("Enter a number (1-7):"))

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid day")

#months
month=int(input("enter a number(1-12):"))

if month == 1:
    print("january")
elif month == 2:
    print("february")
elif month == 3:
    print("march")
elif month == 4:
    print("april")
elif month == 5:
    print("may")
elif month == 6:
    print("june")
elif month == 7:
    print("july")
elif month == 8:
    print("august")
elif month == 9:
    print("september")
elif month == 10:
    print("october")
elif month == 11:
    print("november")
elif month == 12:
    print("december")
else:
    print("invalid month")

#operations
opt = input("enter the operation to perform:").lower()
opt1 = float(input("Enter first number"))
opt2 = float(input("Enter second number"))
#if opt in ['add', '+', 'kudikalu]
if opt =='add' or opt == '+':
    print(opt1 + opt2)
elif opt =='sub' or opt == '-':
    print(opt1 - opt2)
elif opt =='mul' or opt == '*':
    print(opt1 * opt2)
elif opt =='div':
    if opt2 == 0:
        print("division not possible by 0")
    else:
        print(opt1 / opt2)
else:
    ("invalid operator")    


  