# 10. Read integers into a list until the user enters `0` (the sentinel, not stored). 
# Then, without using `sum()`, use a `for` loop to compute the total and count the even numbers; 
# finally print the average (2 decimals) and, in a second `for` loop, every number in the list that is
# greater than that average. Handle the case where the user enters `0` immediately (empty list) without crashing.
numeros = []
numero = int(input())

while numero != 0:
    numeros.append(numero)
    numero = int(input())
soma = 0
par = 0
quantidade_de_pares = 0
average = 0  
 
for numero in numeros:
    soma = numero + soma
    par = numero % 2
    
    if par == 0:
        quantidade_de_pares = quantidade_de_pares + 1
if len(numeros) > 0:
    average = soma / len(numeros)
    for numero in numeros:
        if numero > average:
            
            print("numeros acima da do resultado de media =",numero)
        
        
    
print("lista=",numeros,"soma=\n", soma,"quantidade de pares =\n", quantidade_de_pares,"media={:.2f}\n".format(average))
