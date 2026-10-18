""" 
Controlador de elevador inteligente


Você está desenvolvendo um sistema simples de automação para controlar um elevador inteligente em um edifício.
O edifício possui andares numerados de 0 até andar_maximo. O elevador sempre começa no andar 0.
O sistema recebe uma sequência de comandos, que devem ser processados na ordem em que aparecem.
Os comandos disponíveis são:

Comando	    Comportamento
SUBIR	    Sobe exatamente um andar
DESCER	    Desce exatamente um andar
REINICIAR	Retorna imediatamente ao andar 0

O elevador nunca poderá ultrapassar o último andar ou descer abaixo do térreo (andar 0).
Caso um comando tente movimentar o elevador para um andar inválido, o elevador deverá permanecer no andar atual, e um contador de movimentos bloqueados deverá ser incrementado.
Sua tarefa: desenvolver uma função que receba o andar máximo e a sequência de comandos, retornando uma array com o andar final e a
quantidade total de movimentos bloqueados.

ex01:
andar_maximo = 3   

comandos = [
    "SUBIR",
    "SUBIR",
    "SUBIR",
    "SUBIR",
    "DESCER",
    "REINICIAR",
    "DESCER"
]

resultado [0,2]
"""



"""
andar_final = 0
quantidade_block = 2

comandos = [
    "DESCER"
]

[0,1,2,3]
return [andar_final, quantidade_block]

 """



def controlar_elevador(andar_maximo: int, comandos: list[str]) -> list[int]:
    final_andar = 0
    block_count = 0 

    for command in comandos:
        if command == "SUBIR":
            if final_andar < andar_maximo:
                final_andar = final_andar + 1
            else:
                block_count = block_count + 1
        elif command == "DESCER":
            if final_andar > 0:
                final_andar = final_andar - 1
            else:
                block_count = block_count + 1
        elif command == "REINICIAR":
            final_andar = 0

    return [final_andar, block_count]



if __name__ == "__main__":
    andar_maximo = 3
    comandos = [
        "SUBIR",
        "SUBIR",
        "SUBIR",
        "SUBIR",
        "DESCER",
        "REINICIAR",
        "DESCER",
    ]
    print(controlar_elevador(andar_maximo, comandos))
