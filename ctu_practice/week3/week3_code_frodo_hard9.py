# 9. Read a sentence from the user and use a `for` loop over its characters to count vowels, 
# consonants (letters that are not vowels), and digits separately, ignoring everything else 
# (spaces, punctuation); 
# print the three counts.
sentence = input()
quantidade_de_numeros = 0
quantidade_de_vogais = 0
quantidade_de_consoante = 0
for caracteres in sentence:
    if caracteres.isdigit():
        quantidade_de_numeros = quantidade_de_numeros + 1
# print("digitos = ",quantidade_de_digitos)
    if caracteres.lower() in "aeiou":
        quantidade_de_vogais = quantidade_de_vogais + 1
    if caracteres.lower() in "bcdfghjklmnpqrstvxwyz":
        quantidade_de_consoante = quantidade_de_consoante + 1
print("vogais=",quantidade_de_vogais, "numeros =", quantidade_de_numeros, "consoates = ", quantidade_de_consoante)
