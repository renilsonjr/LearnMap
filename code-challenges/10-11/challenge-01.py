""" 
Encontrando um par de tarefas

Uma equipe de desenvolvimento possui uma lista de tarefas, e cada tarefa tem uma duração estimada em horas.
O líder da equipe deseja selecionar exatamente duas tarefas diferentes cuja soma das durações seja igual a um determinado número de horas.
Você receberá:
- duracoes: uma lista de números inteiros positivos que representam a duração de cada tarefa.
- objetivo: um número inteiro que representa a soma desejada.
Sua função deverá retornar os índices das duas tarefas cuja soma seja igual ao objetivo.
Regras

1. Uma tarefa não pode ser utilizada duas vezes.
2. Os índices começam em zero.
3. Os índices retornados devem estar em ordem crescente.
4. Se não existir uma combinação válida, retorne uma lista vazia.
5. Caso existam múltiplas combinações, qualquer uma delas será aceita.

renilson notes: 
lista de tarefas[idx] /duracao
busca i = 0


encontre dois numeros num array que somados deem o objetivo

ex1:
duracoes = [2, 7, 11, 15]
objetivo = 9

# Saída esperada
[0, 1]

ex2:
duracoes = [3, 4, 3]
objetivo = 6

# Saída esperada
[0, 2]
"""

def encontrar_par(duracoes: list[int], objetivo: int) -> list[int]:
    

    for i in range(len(duracoes)):
        
        if duracoes[i] + duracoes[i+1] == objetivo:
            return [i, i+1]
        print(i, i+1)

    """ for index, number in enumerate(duracoes):
        if 
    return [] """

    return []

if __name__ == "__main__":
    duracoes = [2, 7, 11, 15]
    objetivo = 9
    print(encontrar_par(duracoes, objetivo))


"""
pro item dentro da lista

if o primeiro item somado ao segundo return target = true
else soma o primeiro ao segundo if return target = true
else soma o primeiro ao terceiro, if return target = true
else...


"""