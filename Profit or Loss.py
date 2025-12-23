CP=float(input("Enter the cost price of oranges:"))
SP=float(input("Enter the sell price of oranges:"))
PL=SP-CP
if PL>0:
    print("There is a profit of:",PL)
else:
    print("There is a loss of:",PL)

