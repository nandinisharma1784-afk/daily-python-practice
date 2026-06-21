
 #defining function
def square(x):
  return x*x
print(square(9))

def reverse(string):
  return string[::-1]
print(reverse("abc"))

import math
def prime(x):
    if x<=1:
      return f"{x} is not prime"
    for y in range(2,math.isqrt(x)+1):
      if x%y==0:
        return f"{x} is not prime"

    return f"{x} is prime"
print(prime(9))

import math

def prime(x):
    if x <= 1:
        return f"{x} is not prime"

    for y in range(2, int(math.isqrt(x)) + 1):
        if x % y == 0:
            # Catch non-primes early inside the loop
            return f"{x} is not prime"

    # Indented 4 spaces to stay inside the function, after the loop finishes
    return f"{x} is prime"

print(prime(9))


mport math

shape=input("enter you desired shape(circle,rectangle,triangle)")
def area(shape):
  if shape == "circle":
    radius=float(input("enter radius of circle:"))
    return f"{shape} has area of {math.pi*(radius**2) }"

  elif shape == "rectangle":
    length=float(input("enter length of rectancle:"))
    width=float(input("enter width of rectancle:"))
    return f"{shape} has area of {length*width}"
  elif shape == "triangle":
    base=float(input("enter base of triangle:"))
    height=float(input("enter height of triangle:"))
    return f"{shape} has area of {0.5*base*height}"
print(area(shape))


numbers_split=(input("enter numbers:"))
numbers=numbers_split.split()
numbers=[int(num) for num in numbers]
def split_even_odd(numbers):
  even=[]
  odd=[]
  for num in numbers:
     if num%2==0:
       even.append(num)
     else:
       odd.append(num)
  return even,odd
print(split_even_odd(numbers))
