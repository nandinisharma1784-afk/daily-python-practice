print('''helo
darla''')

      #simple calculator
num1=float(input("enter your 1st number:"))
operator=input("enter operator which u wanna use(*,/,+,-,**)")
num2=float(input("enter your 2nd number:"))
if operator == "*":
  print(num1*num2)
elif operator == "/":
  print(num1/num2)
elif operator=="+":
  print(num1+num2)
elif operator=="-":
  print(num1-num2)
elif operator=="**":
  print(num1**num2)
else:
  print("invalid operator")
