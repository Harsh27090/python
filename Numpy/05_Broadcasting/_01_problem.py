prices = [100,200,300]
discount = 10
final_prices = []

for price in prices:
    price -= price * discount/100
    final_prices.append(price)

print(prices)
print(final_prices)