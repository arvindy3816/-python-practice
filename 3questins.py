cost_price = int(input("enter the cost price"))
selling_price = int(input("enter the selling price"))

if selling_price >  cost_price:
 profit = selling_price -  cost_price
print("we have made the profit")

elif selling_price < cost_price:
loss = cost_price - selling_price
print("we have incurred loss f:",loss)

else:
print("we have no loss and no profit")