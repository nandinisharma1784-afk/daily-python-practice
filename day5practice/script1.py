square= lambda x: x**2
square(8)
list1=[1,2,6,7,9]
cube= list(map(lambda x:x**3,list1))
print(cube)
even_number= list(filter(lambda x:x%2==0,list1))
print(even_number)
