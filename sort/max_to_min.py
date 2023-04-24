print("Enter 3 numbers and get the max one!")
a = int(input("Enter A -> "))
b = int(input("Enter B -> "))
c = int(input("Enter C -> "))
if (a > b):
    if (a > c):
        if (c > b):
            print (a,c,b) 
        else:
            print(a,b,c)
    else:
        print (c,a,b)
else:
    if (b > c):
        if (c > a):
            print (b,c,a)
        else:
            print (b,a,c)
    else:
        print (c,b,a)
