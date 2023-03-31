print('Hello, world!')
a = int(input("Enter A -> "))
b = int(input("Enter B -> "))
c = int(input("Enter C -> "))
if (a > b):
    if (a > c):
        print (a)
    else:
        print(c)
elif (b > c):
     print (b)
else:
     print (c)
