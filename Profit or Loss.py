cost_price=float(input("Enter the cost prices of oranges:"))
sell_price=float(input("Enter the sell price of the oranges:"))
if sell_price > cost_price:
    profit=sell_price-cost_price
    print("The profit is:",profit)
else:
    Loss=cost_price-sell_price
    print("The loss is:",Loss)

