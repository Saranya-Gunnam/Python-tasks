#Grades of students
#marks = float(input("Enter the student's marks: "))
#if marks >= 90 and marks <= 100:
 #   print("Grade A")
#elif marks >= 80 and marks < 90:
 #   print("Grade B")
#elif marks >= 70 and marks < 80:
 #   print("Grade C")
#else:
#    print("Fail")

#sides of triangle
#a = float(input("Enter first side: "))
#b = float(input("Enter second side: "))
#c = float(input("Enter third side: "))
#if a + b > c:
  #  if a + c > b:
   #     if b + c > a:
 #           print("Valid Triangle")
  #      else:
 #           print("Invalid Triangle")
 #   else:
  #      print("Invalid Triangle")
#else:
 #   print("Invalid Triangle")

#reverse and sum
#num = int(input("Enter a number: "))
#reverse = 0
#sum_digits = 0
#while num > 0:
  #  digit = num % 10  
  #  reverse = (reverse * 10) + digit 
 #   sum_digits += digit
  #  num //= 10 
#print("Reversed Number:", reverse)
#print("Sum of Digits:", sum_digits)

#count the numbers
#num = int(input("Enter a number: "))  
#count = 0  
#while num > 0:  
 #   count += 1  
 #   num //= 10  
#print("Number of digits:", count)

#negative number to stop
num = float(input("Enter a number (enter a negative number to stop): "))
while num >= 0:
    num = float(input("Enter a number (enter a negative number to stop): "))
print("You entered a negative number. Program stopped.")

#fibonacci
a, b = 0, 1
for _ in range(10):
    print(a, end=" ")  
    a, b = b, a + b  
print()  

