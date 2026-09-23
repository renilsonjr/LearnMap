# 6. Write a script with several **independent** `if` 
# statements (not `elif`) that reads `product_price` 
# (input, float) and prints each message that applies: 
# `"Eligible for free shipping"` if price > 50, `
# "Eligible for member discount"` if price > 100, `
# "Premium item"` if price > 200 — more than one message can 
# print for the same input.

product_price = float(input('What is the product price?'))
if product_price > 50:
    print('Eligible for free shipping')
if product_price > 100:
    print('Eligible for member discount')
if product_price > 200:
    print('Premium item')
if product_price <= 50:
    print('No benefits')

