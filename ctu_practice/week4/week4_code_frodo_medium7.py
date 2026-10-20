# 7. Write a function `get_order_total(price, tax_rate)` that returns **two** values as a tuple: 
# the tax amount and the total price. Call it, unpack both values into separate variables, and print them with labels.
price = 32


def get_order_total(price, tax_rate):
    imposto = tax_rate / 100 * price
    total = price + imposto
    return imposto,total
imposto,total = get_order_total(price, 10)
print("o valor do imposto e {}, e o valor total e {}".format(imposto, total))