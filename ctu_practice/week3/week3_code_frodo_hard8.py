"""8. Read `n` (int, input) and use nested `for` loops with `range()` to print an `n` by `n` 
multiplication table, one row per line, values separated by spaces (use `end=' '` and an empty 
`print()` at the end of each row)."""

n = int(input())
for i in range(1,n + 1):
     
        
    for j in range(1, n +1):
         
        print(i * j,end=" ")
    print()
