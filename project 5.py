a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=int(input("Enter a number:"))
if a>b and a>c:
    print("Number 1 is the biggest")
elif b>a and b>c:
    print("Number 2 is the biggest")
elif c>a and c>b:
    print("Number 3 is the biggest")
else:
    print("They all are equal")