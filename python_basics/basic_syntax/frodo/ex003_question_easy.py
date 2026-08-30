grocery = ("tomato", "potato", "pepper","carrot","pumpkin","rabbit","watermelon")
user_input = input("What do u want from grocery?")

if user_input in grocery:
    print ("Found grocery")
    
else:
    print('nothing in grocery')

#se o usuario pedir um item em caps sendo que na lista nao esta em caps, vc vai receber um erro,
#em python importa estar em caps ou nao na pesquisa pra parear com o conteudo pesquisado


