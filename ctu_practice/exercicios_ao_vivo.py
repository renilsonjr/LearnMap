# 1. Quantas pessoas vão usar a sala: um número inteiro.
# 2. Se a pessoa responsável tem cadastro: resposta sim ou nao.
#   Mostre uma única mensagem, seguindo estas regras:
# - Menos de 1 ou mais de 6 pessoas: Quantidade invalida.
# - De 1 a 6 pessoas, mas sem cadastro: Cadastro necessario.
# - Com cadastro e de 1 a 3 pessoas: Reservar sala pequena.
# - Com cadastro e de 4 a 6 pessoas: Reservar sala grande.

pessoas = int(input("quantas pessoas?"))
cadastro = str(input("tem cadastro?"))

if pessoas < 1 or pessoas > 6:
      print("Quantidade invalida")
elif (pessoas >= 1) and (pessoas <= 3) and (cadastro == "sim"):
      print("Reservar sala pequena")
elif (pessoas >= 1) and (pessoas <= 6) and (cadastro == "nao"):
      print("cadastro necessario")
elif (pessoas >= 4) and (pessoas <= 6) and (cadastro == "sim"):
    print("Reservar sala grande")      




    