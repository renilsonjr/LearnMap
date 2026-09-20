# PF — Prova Final Cumulativa

## Condições de realização

- **Duração:** 60 minutos.
- **Valor:** 10,0 pontos.
- Realize esta prova somente quando `3 <= MP < 7`.
- Faça a prova individualmente, sem consulta, NumPy, sistema de álgebra simbólica ou solucionador pronto.
- Calculadora básica é permitida apenas para aritmética; deixe passos verificáveis para crédito parcial.
- Distribuição: 3 questões fáceis de 0,5 ponto, 4 médias de 1,0 ponto e 3 difíceis de 1,5 ponto.
- Sugestão de tempo: 9 minutos para as fáceis, 24 para as médias e 27 para as difíceis.

## Persona e política de correção

**Papel:** comissão de recuperação avaliando se o estudante retomou os fundamentos cumulativos necessários para cursos de computação científica, modelagem e otimização.

**Política:** a comissão valoriza formulação correta, operação elementar rastreável e interpretação. Erro aritmético localizado pode receber crédito parcial; base não declarada, sistema sem classificação, diagonalização sem autoespaços ou algoritmo sem hipótese perdem o núcleo da questão.

Respostas e gabaritos estão deliberadamente ausentes. Preserve o caráter inédito da prova até a sessão de 60 minutos.

## Questões fáceis — 1,5 ponto

### Questão 1 — 0,5 ponto

Para `u=(2,-1,0)` e `v=(1,1,3)`, calcule `3u-2v` e explique por que o resultado pertence a `span(u,v)`.

### Questão 2 — 0,5 ponto

Resolva por substituição retroativa:

```text
x + 2y - z = 0
    y + 3z = 7
        2z = 2.
```

### Questão 3 — 0,5 ponto

Verifique se `(1,2)` é autovetor de

```text
A = [1 1]
    [2 2].
```

Se for, determine o autovalor; se não for, apresente a comparação que falha.

## Questões médias — 4,0 pontos

### Questão 4 — 1,0 ponto

Seja

`W={(x,y,z)∈R³:x-2y+z=0}`.

Obtenha uma base de `W`, sua dimensão e as coordenadas de `(3,2,1)` na base escolhida.

### Questão 5 — 1,0 ponto

Para `T:R³→R²` definida por

`T(x,y,z)=(x+2y, y+2z)`,

construa a matriz canônica, encontre uma base do núcleo e determine o posto. Confira posto-nulidade.

### Questão 6 — 1,0 ponto

Considere as bases `B=((1,1),(1,-1))` e `C=((1,0),(1,1))` de `R²`. Encontre a matriz de transição `C←B` resolvendo os sistemas para as colunas. Use-a para converter `[v]_B=(2,3)^T` em `[v]_C`.

### Questão 7 — 1,0 ponto

Para

```text
A = [1 1]
    [0 2],
```

calcule os autovalores e uma base de cada autoespaço. Decida se `A` é diagonalizável e, em caso positivo, exiba `P` e `D` com a ordem compatível.

## Questões difíceis — 4,5 pontos

### Questão 8 — 1,5 ponto

Classifique, em função de `a∈R`, o sistema

```text
x + y +  z = 2
2x + 2y + az = 4
x - y      = 0.
```

Forneça o conjunto-solução em cada caso. Antes do cálculo, justifique em um parágrafo por que operações elementares aplicadas à matriz aumentada preservam o conjunto de soluções.

### Questão 9 — 1,5 ponto

Em `R³`, sejam

`U=span((1,1,0),(0,1,1))`

e

`W=span((1,0,1))`.

1. Verifique se `R³=U⊕W`.
2. Decomponha `(2,3,4)` como `u+w`, se a soma for direta.
3. Prove, para subespaços gerais, que a condição `U∩W={0}` torna única toda decomposição que exista.

### Questão 10 — 1,5 ponto

Considere a dinâmica `x_(k+1)=Ax_k`, com

```text
A = [2 2]
    [1 3]
```

e `x_0=(1,2)`.

1. Diagonalize `A` sobre `R`, calculando autovalores e autovetores.
2. Expresse `x_0` na base de autovetores.
3. Obtenha uma fórmula para `x_k` e identifique a direção dominante quando `k→∞`, declarando a hipótese sobre o coeficiente inicial que torna a conclusão válida.

---

Calcule `MF` pela regra do [plano de avaliação](../README.md#avaliação-e-conclusão). Depois da correção, use o [material](../MATERIAL_DE_ESTUDO.md) e as [listas](../EXERCICIOS.md) para revisar somente os blocos em que perdeu pontos.
