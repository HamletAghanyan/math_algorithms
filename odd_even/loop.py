print('Enter a number to check odd or even!')
a = int(input("Enter A -> "))
while a != 0:
    a = a-2
    if a == -1:
        print("odd")
        quit()
print("even")

