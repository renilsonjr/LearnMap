"""7. Given `stock = {'apples': 3, 'pears': 0, 'plums': 7}`, use a `for` loop over the dictionary to print 
`"<fruit>: <n> in stock"` for each entry; inside the same loop, count how many fruits are out of stock
 (value `0`) and print that count after the loop ends."""

stock = {'apples' : 3, 'pears': 0, 'plums': 7}
out_of_stock = 0
for fruits in stock:
    if stock[fruits] == 0:
        out_of_stock = out_of_stock + 1
    print(f"{fruits}: {stock[fruits]} in stock")
    
print("Frutas sem estoque:", out_of_stock)        
    

   # print(fruits, stock[fruits])

    
    
    
          

    
    
    # if fruits <= 0:
    #     print('out of stock')