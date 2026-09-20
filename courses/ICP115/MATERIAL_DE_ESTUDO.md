# Material de Estudo — ICP115

Este texto é uma primeira exposição autocontida da cobertura selecionada de Álgebra Linear Algorítmica. Ele não tenta substituir as referências oficiais nem antecipar produto interno, mínimos quadrados ou SVD. O fio condutor é sempre o mesmo: definir o objeto, reconhecer a estrutura, executar o algoritmo e interpretar o resultado.

## Como usar o material

Em cada módulo:

1. tente responder à pergunta motivadora antes de ler;
2. copie definições acompanhadas de um exemplo próprio;
3. refaça o exemplo resolvido sem consultar os passos;
4. execute manualmente qualquer algoritmo antes de programá-lo;
5. responda ao checkpoint, que não possui solução neste repositório.

Quando houver código, a implementação didática vem antes da chamada a bibliotecas. NumPy pode ser usado depois como oráculo de conferência, nunca como substituto da formulação ou da demonstração.

## Convenções

- Os escalares são reais, salvo indicação explícita: trabalhamos principalmente sobre `R`.
- Vetores são colunas; `R^n` é o conjunto das colunas com `n` entradas reais.
- `span(S)` é o conjunto de todas as combinações lineares finitas de elementos de `S`.
- `E=(e_1,...,e_n)` denota a base canônica e `[v]_B` a coluna de coordenadas de `v` na base ordenada `B`.
- `ker(T)` e `im(T)` são núcleo e imagem de `T`; `rank(A)` é o posto de `A`.
- Igualdade matemática, como `Ax=b`, não é o mesmo que aproximação de ponto flutuante, como `abs(r)<10^-12`.
- Em algoritmos numéricos, `tol` é uma escolha operacional. Ela não transforma uma quantidade não nula em zero exato.

---

## Módulo 1 — Vetores, combinações e bases no plano

### Pergunta motivadora

Se duas setas formam um sistema de coordenadas oblíquo, como representar qualquer outra seta nesse sistema e como saber se a representação é única?

### 1.1 Vetores e operações

Um vetor de `R^n` é uma lista ordenada de `n` números reais,

`v=(v_1,...,v_n)`.

Somamos vetores componente a componente e multiplicamos por escalar:

`u+v=(u_1+v_1,...,u_n+v_n)`,

`αv=(αv_1,...,αv_n)`.

Geometricamente, um vetor de `R²` representa deslocamento. Algebricamente, suas entradas dependem da base escolhida. O objeto vetor e sua coluna de coordenadas coincidem apenas quando a base está implícita.

### 1.2 Combinação linear e espaço gerado

Uma **combinação linear** de `v_1,...,v_k` é

`α_1v_1+...+α_kv_k`, com `α_i∈R`.

O conjunto de todas essas combinações é `span(v_1,...,v_k)`. Ele sempre contém o vetor zero: basta escolher todos os coeficientes iguais a zero.

Para decidir se `x` pertence ao espaço gerado, resolvemos

`α_1v_1+...+α_kv_k=x`.

Essa pergunta já é um sistema linear. No próximo módulo, ela ganhará um algoritmo geral.

### 1.3 Dependência, independência e base

Os vetores `v_1,...,v_k` são **linearmente independentes** quando

`α_1v_1+...+α_kv_k=0`

implica `α_1=...=α_k=0`. Se existir uma relação não trivial, o conjunto é dependente.

Uma lista ordenada `B=(b_1,...,b_n)` é uma **base** de um espaço `V` quando:

1. `span(b_1,...,b_n)=V`;
2. os vetores são linearmente independentes.

As duas condições têm papéis diferentes: geração garante existência de coordenadas; independência garante unicidade.

**Teorema das coordenadas.** Se `B` é base de `V`, então todo `v∈V` possui uma única representação

`v=c_1b_1+...+c_nb_n`.

A coluna `[v]_B=(c_1,...,c_n)^T` é a coordenada de `v` em `B`.

**Hipóteses necessárias:** `B` deve gerar todo `V` e ser independente. Uma lista apenas geradora pode oferecer várias representações; uma lista apenas independente pode não representar todo vetor.

### 1.4 Um critério no plano

Para `u=(a,c)` e `v=(b,d)`, a matriz que coloca esses vetores nas colunas é

```text
P = [ a  b ]
    [ c  d ].
```

Os dois vetores formam base de `R²` exatamente quando `det(P)=ad-bc≠0`. Se o determinante é zero, um vetor é múltiplo do outro ou algum deles é zero; o espaço gerado é no máximo uma reta.

Esse critério é específico e conveniente em dimensão dois. A eliminação gaussiana fornecerá o critério geral por pivôs.

### Exemplo resolvido — duas descrições do mesmo vetor

Considere `B=(b_1,b_2)` com `b_1=(1,1)` e `b_2=(1,-1)`. Como

`det([b_1 b_2])=1·(-1)-1·1=-2≠0`,

`B` é base de `R²`.

Para encontrar as coordenadas de `x=(4,2)`, escrevemos

`c_1(1,1)+c_2(1,-1)=(4,2)`.

Comparando componentes:

```text
c_1+c_2 = 4
c_1-c_2 = 2.
```

Somando as equações, `2c_1=6`, logo `c_1=3`; então `c_2=1`. Portanto,

`[x]_B=(3,1)^T`, embora `[x]_E=(4,2)^T`.

A igualdade correta é entre vetores:

`x=3b_1+b_2`.

As colunas `(4,2)^T` e `(3,1)^T` são diferentes porque descrevem o mesmo vetor em bases diferentes.

### Erros comuns

- Confundir vetor com sua coluna sem declarar a base.
- Dizer que um conjunto é base apenas porque tem `n` vetores em `R^n`; ainda é preciso verificar independência ou geração.
- Tratar `span(v_1,...,v_k)` como a lista de geradores, e não como um conjunto infinito de combinações.
- Provar dependência escolhendo todos os coeficientes iguais a zero; essa relação existe para qualquer lista e não é não trivial.
- Dividir por determinante sem antes garantir que ele é não nulo.

### Conexão com IA

Um vetor de características é uma representação: as entradas dependem das características escolhidas. Trocar a base muda os números, não o exemplo abstrato representado. Embeddings também são coordenadas em um espaço vetorial aprendido; interpretar uma coordenada isoladamente sem considerar a base ou o sistema de representação costuma ser enganoso.

### Checkpoint 1 — sem solução

Sejam `u=(2,1)` e `v=(-1,2)`.

1. Mostre que `B=(u,v)` é base de `R²`.
2. Encontre `[(3,4)]_B`.
3. Explique por que trocar a ordem para `(v,u)` altera a coluna de coordenadas, mas não o vetor.

---

## Módulo 2 — Sistemas lineares e eliminação gaussiana

### Pergunta motivadora

Como um único algoritmo decide se um sistema tem zero, uma ou infinitas soluções e ainda fornece a estrutura de todas elas?

### 2.1 Matrizes e sistemas

Uma matriz `A∈R^(m×n)` possui `m` linhas e `n` colunas. O produto `Ax`, para `x∈R^n`, combina as colunas de `A` usando as entradas de `x`:

`Ax=x_1a_1+...+x_na_n`.

Assim, resolver `Ax=b` equivale a perguntar se `b∈span(a_1,...,a_n)` e, em caso afirmativo, encontrar os coeficientes.

A matriz aumentada `[A|b]` registra coeficientes e lado direito sem perder a distinção entre eles.

### 2.2 Operações elementares

Há três operações elementares de linha:

1. trocar duas linhas;
2. multiplicar uma linha por escalar não nulo;
3. somar a uma linha um múltiplo de outra.

Cada operação é reversível. Por isso, aplicada à matriz aumentada inteira, preserva exatamente o conjunto de soluções.

**Cuidado:** operar apenas em `A` e esquecer `b` muda o sistema. Operações de coluna, por sua vez, alteram o significado das incógnitas e não pertencem à eliminação usual de `Ax=b`.

### 2.3 Forma escalonada, pivôs e variáveis livres

Uma matriz está em forma escalonada quando:

- linhas nulas ficam abaixo das não nulas;
- o primeiro elemento não nulo de cada linha está à direita do pivô da linha anterior;
- abaixo de cada pivô há zeros.

Na forma escalonada reduzida, cada pivô vale `1` e é o único elemento não nulo de sua coluna.

As colunas de pivô correspondem a variáveis básicas. As demais correspondem a variáveis livres.

Para `Ax=b`:

- uma linha `[0 ... 0 | c]`, com `c≠0`, indica inconsistência;
- sem inconsistência e sem variáveis livres, há solução única;
- sem inconsistência e com ao menos uma variável livre, há infinitas soluções.

O sistema homogêneo `Ax=0` é sempre consistente. Ele tem solução não trivial exatamente quando há variável livre.

### 2.4 Eliminação gaussiana como algoritmo

Para cada coluna, procure um pivô em uma linha ainda não usada, troque linhas se necessário, normalize o pivô e elimine as outras entradas da coluna. Em aritmética exata, “não nulo” é uma propriedade matemática. Em ponto flutuante, selecionamos um pivô de maior módulo entre os candidatos e usamos uma tolerância.

O código abaixo calcula uma forma escalonada reduzida didática. Ele não pretende competir com rotinas numéricas robustas.

```python
def rref(coeffs, rhs=None, tol=1e-12):
    """Retorna (matriz_reduzida, colunas_pivo, inconsistente)."""
    rows = len(coeffs)
    if rows == 0:
        return [], [], False
    cols = len(coeffs[0])
    if any(len(row) != cols for row in coeffs):
        raise ValueError("linhas com tamanhos diferentes")
    if rhs is not None and len(rhs) != rows:
        raise ValueError("lado direito incompatível")

    matrix = []
    for i, row in enumerate(coeffs):
        new_row = [float(value) for value in row]
        if rhs is not None:
            new_row.append(float(rhs[i]))
        matrix.append(new_row)

    pivot_columns = []
    pivot_row = 0
    for column in range(cols):
        if pivot_row == rows:
            break
        candidate = max(
            range(pivot_row, rows),
            key=lambda i: abs(matrix[i][column]),
        )
        if abs(matrix[candidate][column]) <= tol:
            continue

        matrix[pivot_row], matrix[candidate] = (
            matrix[candidate],
            matrix[pivot_row],
        )
        pivot = matrix[pivot_row][column]
        matrix[pivot_row] = [value / pivot for value in matrix[pivot_row]]

        for i in range(rows):
            if i == pivot_row:
                continue
            factor = matrix[i][column]
            matrix[i] = [
                current - factor * reference
                for current, reference in zip(matrix[i], matrix[pivot_row])
            ]

        pivot_columns.append(column)
        pivot_row += 1

    for row in matrix:
        for j, value in enumerate(row):
            if abs(value) <= tol:
                row[j] = 0.0

    inconsistent = False
    if rhs is not None:
        inconsistent = any(
            all(abs(row[j]) <= tol for j in range(cols))
            and abs(row[-1]) > tol
            for row in matrix
        )
    return matrix, pivot_columns, inconsistent
```

**Invariante algébrico:** depois de cada operação elementar, o novo sistema tem o mesmo conjunto-solução que o anterior.

**Limitação numérica:** pivotamento parcial reduz alguns efeitos de arredondamento, mas não fornece análise de estabilidade nem resolve problemas mal condicionados. Esses temas pertencem aos cursos posteriores.

### 2.5 Posto

O **posto** de `A` é o número de pivôs de sua forma escalonada. Ele também é a dimensão do espaço gerado pelas colunas de `A`.

Se `A` é quadrada `n×n`, são equivalentes:

- `rank(A)=n`;
- cada coluna é pivô;
- `Ax=0` só tem a solução zero;
- `Ax=b` possui solução única para todo `b∈R^n`;
- `A` é invertível.

A equivalência será reinterpretada por transformações lineares no módulo 4.

### Exemplo resolvido — uma solução única

Resolva

```text
x +  y +  z = 6
2x -  y +  z = 3
x + 2y -  z = 2.
```

A matriz aumentada é

```text
[ 1  1  1 | 6 ]
[ 2 -1  1 | 3 ]
[ 1  2 -1 | 2 ].
```

Faça `L_2←L_2-2L_1` e `L_3←L_3-L_1`:

```text
[ 1  1  1 |  6 ]
[ 0 -3 -1 | -9 ]
[ 0  1 -2 | -4 ].
```

Troque as duas últimas linhas e faça `L_3←L_3+3L_2`:

```text
[ 1  1  1 |  6 ]
[ 0  1 -2 | -4 ]
[ 0  0 -7 | -21].
```

Da última linha, `z=3`; da segunda, `y-6=-4`, então `y=2`; da primeira, `x=1`. Há três pivôs e nenhuma variável livre, logo a solução é única:

`(x,y,z)=(1,2,3)`.

Uma conferência posterior pode executar:

```python
matrix, pivots, inconsistent = rref(
    [[1, 1, 1], [2, -1, 1], [1, 2, -1]],
    [6, 3, 2],
)
print(matrix, pivots, inconsistent)
```

### Erros comuns

- Aplicar a operação de linha aos coeficientes, mas não ao lado direito.
- Concluir que há infinitas soluções apenas porque o sistema tem mais incógnitas que equações; ainda é preciso verificar consistência e posto.
- Dividir uma linha por zero ou por uma quantidade tratada como zero sem justificar a tolerância.
- Ler colunas de pivô da matriz reduzida como uma base do espaço coluna original. Os **índices** dos pivôs selecionam colunas da matriz original.
- Formar `A^-1b` como método padrão. Eliminação resolve o sistema sem exigir a construção explícita da inversa.

### Conexão com IA

Camadas lineares, regressão e ajustes posteriores produzem sistemas ou problemas matriciais. Mesmo quando uma biblioteca resolve o cálculo, posto e variáveis livres informam identificabilidade: parâmetros diferentes podem produzir a mesma saída. O algoritmo de eliminação também antecipa a diferença entre descrever uma solução e entender a estrutura de todas as soluções.

### Checkpoint 2 — sem solução

Escalone o sistema

```text
x + 2y -  z = 1
2x + 4y - 2z = 2
x + 2y -  z = 3.
```

Classifique-o e identifique a primeira linha que certifica sua conclusão. Depois altere somente o último lado direito para `1` e descreva o novo conjunto-solução.

---

## Módulo 3 — `R^n`, subespaços, independência e coordenadas

### Pergunta motivadora

Uma equação linear homogênea descreve infinitos vetores. Como substituir esse conjunto infinito por uma base finita sem perder informação?

### 3.1 Espaços e subespaços

`R^n`, com as operações usuais, satisfaz as propriedades de um espaço vetorial: fechamento, associatividade, comutatividade da soma, vetor zero, oposto, distributividade e compatibilidade da multiplicação por escalares.

Um subconjunto não vazio `W⊆R^n` é **subespaço** quando:

1. se `u,v∈W`, então `u+v∈W`;
2. se `u∈W` e `α∈R`, então `αu∈W`.

Equivalentemente, `W` contém toda combinação linear `αu+βv` de dois de seus elementos. Em particular, todo subespaço contém `0`.

São subespaços:

- `span(S)` para qualquer conjunto `S`;
- o conjunto-solução de `Ax=0`, chamado espaço nulo;
- a imagem de uma transformação linear.

Em geral não são subespaços:

- retas e planos que não passam pela origem;
- conjuntos definidos por `Ax=b` com `b≠0`, quando não vazios;
- conjuntos com restrições como `x_i≥0`.

### 3.2 Base e dimensão

Uma base de `W` é uma lista independente que gera `W`. Em espaços de dimensão finita, todas as bases de `W` têm a mesma quantidade de vetores; essa quantidade é `dim(W)`.

**Teorema de extração e extensão.** Em dimensão finita:

- de qualquer lista geradora de `W` é possível remover vetores redundantes até obter uma base;
- qualquer lista independente em `W` pode ser estendida até uma base de `W`.

As hipóteses “lista geradora” e “lista independente” não são intercambiáveis.

### 3.3 Como extrair uma base de colunas

Se `A=[a_1 ... a_k]`, escalone `A` e anote os índices das colunas de pivô. As colunas correspondentes **da matriz original** formam uma base de `span(a_1,...,a_k)`.

A razão é que operações de linha preservam as relações lineares entre colunas, mas alteram os próprios vetores coluna. Logo os índices são confiáveis; as colunas transformadas não representam necessariamente o mesmo subespaço de `R^m`.

### 3.4 Coordenadas em um subespaço

Se `B=(b_1,...,b_k)` é base de `W`, então a aplicação

`v↦[v]_B`

identifica `W` com `R^k`. Para obter as coordenadas, resolva

`[b_1 ... b_k]c=v`.

Há uma única solução porque as colunas são independentes e `v` pertence ao espaço gerado.

### 3.5 Sistemas homogêneos e parametrização

Depois de escalonar `Ax=0`, escolha parâmetros para variáveis livres e escreva a solução como combinação linear desses parâmetros. Os vetores que multiplicam os parâmetros geram `ker(A)`; se a parametrização é independente, eles formam uma base.

Se `A` tem `n` colunas e `r` pivôs, existem `n-r` variáveis livres. Logo:

`dim(ker(A))=n-rank(A)`.

Essa é a versão matricial do teorema posto-nulidade, que será formalizado para transformações.

### Exemplo resolvido — base de um plano homogêneo

Considere

`W={(x,y,z)∈R³ : x+y+z=0}`.

O vetor zero pertence a `W`. Se `u,v∈W` e `α,β∈R`, então

`(αu_1+βv_1)+(αu_2+βv_2)+(αu_3+βv_3)`

`=α(u_1+u_2+u_3)+β(v_1+v_2+v_3)=0`.

Portanto, `W` é subespaço.

Da equação, `x=-y-z`. Escolhendo `y=s` e `z=t`,

```text
(x,y,z)=(-s-t,s,t)
         =s(-1,1,0)+t(-1,0,1).
```

Os vetores `b_1=(-1,1,0)` e `b_2=(-1,0,1)` geram `W`. Se

`αb_1+βb_2=0`,

a segunda componente dá `α=0` e a terceira dá `β=0`; são independentes. Assim, `B=(b_1,b_2)` é base e `dim(W)=2`.

Para `w=(-2,1,1)`, a própria parametrização mostra

`w=b_1+b_2`, logo `[w]_B=(1,1)^T`.

### Erros comuns

- Verificar fechamento, mas esquecer que o conjunto precisa conter o zero.
- Tratar o conjunto-solução de `Ax=b`, `b≠0`, como subespaço apenas porque as equações são lineares.
- Confundir número de geradores apresentados com dimensão; geradores podem ser redundantes.
- Usar as colunas da matriz escalonada como base do espaço coluna original.
- Dar uma parametrização geradora sem verificar se os vetores obtidos são independentes.

### Conexão com IA

Um subespaço pode representar todas as combinações permitidas por um modelo linear, enquanto o núcleo representa alterações invisíveis à saída. Se uma codificação linear envia vetores diferentes à mesma representação, a diferença entre eles pertence ao núcleo. Dimensão mede graus de liberdade, não quantidade de pontos.

### Checkpoint 3 — sem solução

Considere os vetores

`v_1=(1,0,1)`, `v_2=(0,1,1)`, `v_3=(1,1,2)` e `v_4=(2,1,3)`.

1. Extraia uma base de `span(v_1,v_2,v_3,v_4)` usando pivôs.
2. Determine a dimensão.
3. Encontre as coordenadas de `v_4` na base extraída.
4. Identifique duas relações de dependência, se existirem.

---

## Módulo 4 — Transformações lineares, matrizes, núcleo e imagem

### Pergunta motivadora

Como uma tabela finita de números consegue determinar o efeito de uma função sobre infinitos vetores?

### 4.1 Linearidade

Uma função `T:V→W` entre espaços vetoriais é **linear** quando, para todos `u,v∈V` e `α,β∈R`,

`T(αu+βv)=αT(u)+βT(v)`.

É suficiente verificar aditividade e homogeneidade, mas a forma combinada evidencia que transformações lineares preservam todas as combinações lineares. Em particular, `T(0)=0`.

Translações como `T(x)=Ax+b`, com `b≠0`, são afins, não lineares.

### 4.2 A matriz de uma transformação

Se `T:R^n→R^m` é linear e `E=(e_1,...,e_n)` é a base canônica, então

`x=x_1e_1+...+x_ne_n`

implica

`T(x)=x_1T(e_1)+...+x_nT(e_n)`.

Logo a matriz canônica de `T` tem `T(e_j)` na coluna `j`:

`[T]_E=[T(e_1) ... T(e_n)]`.

Conhecer o efeito sobre uma base determina o efeito sobre todo vetor.

Se `S:R^p→R^n` e `T:R^n→R^m`, então

`[T∘S]=[T][S]`.

A ordem importa: primeiro atua a matriz à direita.

### 4.3 Núcleo e imagem

O núcleo e a imagem são

`ker(T)={v∈V:T(v)=0}`,

`im(T)={T(v):v∈V}`.

Ambos são subespaços. Para uma matriz `A`:

- `ker(T)` é o conjunto-solução de `Ax=0`;
- `im(T)` é o espaço gerado pelas colunas de `A`.

`T` é injetiva exatamente quando `ker(T)={0}`. `T:R^n→R^m` é sobrejetiva exatamente quando `rank(A)=m`.

### 4.4 Teorema posto-nulidade

**Teorema.** Se `T:V→W` é linear e `V` tem dimensão finita, então

`dim(V)=dim(ker(T))+dim(im(T))`.

As hipóteses são linearidade e domínio de dimensão finita. O contradomínio não precisa ter a mesma dimensão.

**Ideia da demonstração.** Tome uma base do núcleo e estenda-a a uma base do domínio. As imagens dos vetores adicionados formam uma base da imagem. Os vetores do núcleo desaparecem sob `T`; os demais contabilizam exatamente o posto.

### 4.5 Invertibilidade como propriedade estrutural

Para `T:R^n→R^n`, as seguintes afirmações são equivalentes:

- `T` é injetiva;
- `T` é sobrejetiva;
- `ker(T)={0}`;
- `rank(T)=n`;
- a matriz de `T` em qualquer base é invertível.

A igualdade das dimensões de domínio e contradomínio é essencial para concluir “injetiva se e somente se sobrejetiva”.

### Exemplo resolvido — núcleo e imagem de uma aplicação

Defina `T:R³→R²` por

`T(x,y,z)=(x-y,y+z)`.

Ela é linear porque cada componente é combinação linear das entradas. As imagens da base canônica são

```text
T(e_1)=(1,0),  T(e_2)=(-1,1),  T(e_3)=(0,1).
```

Logo

```text
A = [ 1 -1  0 ]
    [ 0  1  1 ].
```

Para o núcleo, resolvemos

```text
x-y = 0
y+z = 0.
```

Tomando `y=t`, obtemos `(x,y,z)=t(1,1,-1)`. Portanto,

`ker(T)=span((1,1,-1))` e `nullity(T)=1`.

As duas primeiras colunas `(1,0)` e `(-1,1)` são independentes, então geram `R²`. Assim,

`im(T)=R²` e `rank(T)=2`.

O teorema confirma `3=1+2`.

### Erros comuns

- Verificar linearidade apenas em alguns vetores de teste.
- Colocar `T(e_j)` nas linhas, e não nas colunas.
- Escrever `im(T)` como conjunto de entradas possíveis sem fornecer geração, equações ou base.
- Concluir injetividade a partir de `T(0)=0`; toda transformação linear satisfaz essa igualdade.
- Aplicar “injetiva equivale a sobrejetiva” quando as dimensões de domínio e contradomínio diferem.

### Conexão com IA

Uma camada sem viés é uma transformação linear; com viés, é afim. O núcleo contém perturbações que a camada não distingue. O posto limita quantas direções independentes da entrada podem sobreviver, mesmo que a saída tenha muitas coordenadas.

### Checkpoint 4 — sem solução

Seja `T:R³→R³` definida por

`T(x,y,z)=(x+z, y-z, x+y)`.

1. Construa a matriz canônica.
2. Determine bases do núcleo e da imagem.
3. Verifique posto-nulidade.
4. Decida, com justificativa estrutural, se `T` é invertível.

---

## Módulo 5 — Soma, interseção e complementos de subespaços

### Pergunta motivadora

Quando dois modelos lineares compartilham direções, como contar apenas uma vez a informação repetida e separar componentes independentes?

### 5.1 Interseção e soma

Se `U,W≤V` são subespaços, então

`U∩W={v:v∈U e v∈W}`

e

`U+W={u+w:u∈U, w∈W}`

também são subespaços.

A união `U∪W` geralmente não é subespaço. Ela só é subespaço quando `U⊆W` ou `W⊆U`: se houver `u∈U\W` e `w∈W\U`, então `u+w` não pode pertencer a apenas um deles.

### 5.2 Fórmula das dimensões

Para subespaços finito-dimensionais,

`dim(U+W)=dim(U)+dim(W)-dim(U∩W)`.

A subtração corrige a dupla contagem da interseção. A hipótese de dimensão finita permite contar vetores de bases.

**Ideia da demonstração.** Comece por uma base da interseção. Estenda-a separadamente a bases de `U` e de `W`. A união controlada das extensões forma uma base de `U+W`.

### 5.3 Soma direta e complementos

Escrevemos `V=U⊕W` quando:

1. `V=U+W`;
2. `U∩W={0}`.

Nesse caso, todo `v∈V` possui decomposição única `v=u+w`.

Um **complemento algébrico** de `U≤V` é um subespaço `W` tal que `V=U⊕W`. Ele geralmente não é único. Em dimensão finita, um complemento pode ser construído estendendo uma base de `U` a uma base de `V`; os vetores adicionados geram `W`.

Nada aqui envolve ângulo ou perpendicularidade. Um complemento ortogonal só faria sentido depois de escolher um produto interno.

### 5.4 Algoritmos para soma e interseção

Se as colunas de `P` formam uma base de `U` e as de `Q` uma base de `W`:

- uma base de `U+W` é extraída das colunas de `[P Q]` por pivôs;
- para a interseção, resolva `Pa=Qb`, isto é,

`[P -Q] (a,b)^T=0`.

Cada solução fornece um vetor comum `Pa=Qb`. Depois remova redundâncias entre esses vetores.

**Hipótese operacional:** `P` e `Q` devem usar a mesma base ambiente; misturar coordenadas de bases diferentes produz equações sem significado.

### Exemplo resolvido — dois planos coordenados

Em `R³`, tome

`U=span(e_1,e_2)` e `W=span(e_2,e_3)`.

Um vetor de `U` tem forma `(a,b,0)`; um vetor de `W`, forma `(0,c,d)`. Para estar na interseção,

`(a,b,0)=(0,c,d)`,

logo `a=0`, `d=0` e `b=c`. Portanto,

`U∩W=span(e_2)`.

A união das bases contém `e_1,e_2,e_3`, então `U+W=R³`. A fórmula confirma:

`dim(U+W)=2+2-1=3`.

Como `U∩W` não é `{0}`, a soma `U+W` não é direta.

Um complemento de `U` em `R³` é `span(e_3)`. Outro é `span(e_1+e_3)`: esse vetor não pertence a `U`, sua reta intersecta `U` apenas em zero, e com `U` gera `R³`. A não unicidade é explícita.

### Erros comuns

- Usar `U∪W` quando a operação correta é `U+W`.
- Somar dimensões sem descontar a interseção.
- Chamar qualquer subespaço disjunto de complemento; também é preciso gerar o espaço ambiente junto com `U`.
- Supor que complemento significa perpendicular.
- Obter coeficientes `(a,b)` de `[P -Q]` e tratá-los como o vetor da interseção; o vetor comum é `Pa=Qb`.

### Conexão com IA

Ao combinar dois conjuntos de características, direções compartilhadas não acrescentam dimensão duas vezes. Interseções modelam informação comum; somas modelam o repertório conjunto; uma soma direta garante decomposição única em componentes. A interpretação só é geométrica depois de fixar uma representação coerente.

### Checkpoint 5 — sem solução

Em `R⁴`, sejam

`U=span((1,0,1,0),(0,1,0,1))`

e

`W=span((1,1,1,1),(1,-1,1,-1),(0,0,1,0))`.

Encontre bases de `U∩W` e `U+W`, confira a fórmula das dimensões e decida se a soma é direta.

---

## Módulo 6 — Mudança de base

### Pergunta motivadora

Como a mesma transformação pode parecer uma matriz cheia em uma base e uma matriz diagonal em outra sem que seu efeito tenha mudado?

### 6.1 Matriz de uma base

Se `B=(b_1,...,b_n)` é base de `R^n`, defina

`P_B=[b_1 ... b_n]`,

onde cada `b_j` está escrito na base canônica. Então

`[v]_E=P_B[v]_B`.

Como as colunas de `P_B` formam base, `P_B` é invertível e

`[v]_B=P_B^-1[v]_E`.

Não é necessário construir a inversa explicitamente: resolver `P_Bc=v` por eliminação encontra `c=[v]_B`.

### 6.2 Transição entre duas bases

Para bases `B` e `C` do mesmo espaço,

`[v]_C=P_C^-1P_B[v]_B`.

A matriz `P_C^-1P_B` recebe coordenadas em `B` e devolve coordenadas em `C`. Leia sempre origem e destino; a inversa faz a transição contrária.

### 6.3 Matriz de uma transformação em bases escolhidas

Se `T:V→W`, `B` é base do domínio e `C` do contradomínio, a matriz `[T]_{C←B}` satisfaz

`[T(v)]_C=[T]_{C←B}[v]_B`.

Suas colunas são `[T(b_j)]_C`.

Se `A=[T]_{E←E}`, então

`[T]_{C←B}=P_C^-1 A P_B`.

Quando domínio e contradomínio são o mesmo espaço e usamos a mesma nova base `B`,

`[T]_B=P_B^-1AP_B`.

As matrizes `A` e `[T]_B` são **semelhantes**. Elas representam o mesmo operador em bases diferentes e têm o mesmo polinômio característico, determinante, traço e autovalores.

### 6.4 Implementação antes da biblioteca

Depois de executar a função `rref` do módulo 2, podemos resolver um sistema quadrado com solução única:

```python
def solve_unique(coeffs, rhs, tol=1e-12):
    reduced, pivots, inconsistent = rref(coeffs, rhs, tol)
    size = len(coeffs[0])
    if inconsistent or len(pivots) != size:
        raise ValueError("o sistema não tem solução única")
    return [reduced[i][-1] for i in range(size)]


def coordinates(vector, basis_columns):
    """basis_columns contém os vetores da base, um por coluna lógica."""
    dimension = len(vector)
    if len(basis_columns) != dimension:
        raise ValueError("é necessária uma base quadrada do espaço ambiente")
    if any(len(column) != dimension for column in basis_columns):
        raise ValueError("cada vetor da base deve ter a dimensão do ambiente")
    matrix = [
        [basis_columns[column][row] for column in range(dimension)]
        for row in range(dimension)
    ]
    return solve_unique(matrix, vector)
```

O contrato da função torna a hipótese explícita: as colunas precisam formar uma base. Se forem dependentes, a rotina rejeita o sistema em vez de inventar coordenadas.

### Exemplo resolvido — uma matriz diagonal escondida

Considere o operador em `R²` cuja matriz canônica é

```text
A = [2 1]
    [1 2].
```

Use a base `B=(b_1,b_2)` com `b_1=(1,1)` e `b_2=(1,-1)`. Temos

`T(b_1)=(3,3)=3b_1`,

`T(b_2)=(1,-1)=b_2`.

Logo, sem calcular inversa,

```text
[T]_B = [3 0]
        [0 1].
```

Para `x=(4,2)`, o módulo 1 mostrou `[x]_B=(3,1)`. Na base `B`,

`[T(x)]_B=(9,1)`.

Voltando à base canônica:

`T(x)=9b_1+b_2=(10,8)`.

Diretamente, `A(4,2)^T=(10,8)^T`. As duas rotas concordam porque descrevem o mesmo operador.

### Erros comuns

- Inverter a direção: `P_B` leva coordenadas em `B` para coordenadas canônicas, não o contrário.
- Misturar vetores em uma base com matrizes escritas em outra.
- Usar `PAP^-1` por memorização quando a convenção adotada exige `P^-1AP`.
- Calcular inversa explícita quando resolver um sistema é suficiente.
- Achar que uma matriz semelhante representa uma transformação diferente.

### Conexão com IA

Representações diferentes podem tornar uma operação mais simples. Uma mudança de base bem escolhida separa direções que o operador trata de modos distintos. Em pipelines de dados, essa ideia aparece em representações latentes e decomposições espectrais; aqui estudamos o mecanismo algébrico, ainda sem produto interno ou SVD.

### Checkpoint 6 — sem solução

Para

```text
A = [4 2]
    [1 3]
```

e `B=((2,1),(1,-1))`:

1. calcule `P_B` e `[T]_B=P_B^-1AP_B` por sistemas lineares;
2. converta `x=(5,1)` para coordenadas em `B`;
3. calcule `T(x)` nas duas bases e confira que os resultados representam o mesmo vetor.

---

## Módulo 7 — Autovalores, autovetores e diagonalização

### Pergunta motivadora

Quais direções uma transformação preserva, alterando apenas sua escala, e quando essas direções bastam para descrever todo o espaço?

### 7.1 Autovalores e autoespaços

Um vetor não nulo `v` é autovetor de `A` associado ao escalar `λ` quando

`Av=λv`.

O escalar `λ` é autovalor. Reorganizando,

`(A-λI)v=0`.

Existe solução não nula exatamente quando `A-λI` não é invertível. Para matrizes quadradas,

`det(A-λI)=0`.

O polinômio `p_A(λ)=det(A-λI)` é o polinômio característico, com a convenção adotada aqui. Alguns textos usam `det(λI-A)`; as raízes são as mesmas.

O **autoespaço** de `λ` é

`E_λ=ker(A-λI)`.

Ele contém o zero; o conjunto de autovetores é `E_λ\{0}`.

### 7.2 Multiplicidades

A multiplicidade algébrica de `λ` é sua multiplicidade como raiz de `p_A`. A multiplicidade geométrica é `dim(E_λ)`.

Para cada autovalor,

`1 ≤ multiplicidade geométrica ≤ multiplicidade algébrica`.

Autovetores associados a autovalores distintos são linearmente independentes. Essa afirmação vale sobre o corpo em que os autovalores e vetores existem.

### 7.3 Critério de diagonalização

Uma matriz `A∈R^(n×n)` é diagonalizável sobre `R` quando existe uma base real de autovetores. Se `P` contém esses autovetores nas colunas e `D` contém os autovalores correspondentes na diagonal, então

`AP=PD`

e, como `P` é invertível,

`A=PDP^-1`, equivalentemente `D=P^-1AP`.

Critérios úteis:

- `A` é diagonalizável se possui `n` autovalores distintos reais;
- em geral, é diagonalizável se a soma das dimensões dos autoespaços é `n`;
- uma raiz repetida não impede diagonalização, mas exige autoespaço com dimensão suficiente;
- uma matriz real pode ter autovalores complexos e não ser diagonalizável **sobre `R`**.

### 7.4 Procedimento algorítmico

1. Calcule `p_A(λ)`.
2. Encontre suas raízes no corpo escolhido.
3. Para cada raiz, resolva `(A-λI)v=0` e obtenha uma base de `E_λ`.
4. Conte autovetores independentes.
5. Se houver `n`, coloque-os nas colunas de `P`, na mesma ordem dos autovalores em `D`.
6. Verifique `AP=PD` antes de formar qualquer inversa.

Em dimensões grandes, calcular o polinômio característico simbolicamente não é o método numérico padrão. Aqui ele é adequado ao objetivo conceitual e a matrizes pequenas.

### Exemplo resolvido — dois autoespaços

Considere

```text
A = [4 1]
    [2 3].
```

O polinômio característico é

`det(A-λI)=(4-λ)(3-λ)-2=λ²-7λ+10=(λ-5)(λ-2)`.

Para `λ=5`,

```text
A-5I = [-1  1]
         [ 2 -2],
```

logo `x=y` e `E_5=span((1,1))`.

Para `λ=2`,

```text
A-2I = [2 1]
        [2 1],
```

logo `2x+y=0` e `E_2=span((1,-2))`.

Há dois autovetores independentes. Escolha

```text
P = [1  1]       D = [5 0]
    [1 -2],          [0 2].
```

As colunas e a diagonal usam a mesma ordem. A verificação `AP=PD` confirma

`A=PDP^-1`.

### Erros comuns

- Aceitar o vetor zero como autovetor.
- Resolver apenas `det(A-λI)=0` e não calcular os autoespaços.
- Confundir multiplicidade algébrica com dimensão do autoespaço.
- Misturar a ordem das colunas de `P` e dos valores na diagonal de `D`.
- Afirmar que toda matriz quadrada é diagonalizável.
- Omitir o corpo: diagonalização sobre `R` e sobre `C` podem ter respostas diferentes.

### Conexão com IA

Autovetores identificam direções invariantes de uma operação linear. Repetir uma transformação amplifica direções conforme potências dos autovalores. Esse mecanismo aparece em dinâmicas, propagação em grafos e métodos espectrais. PCA requer ainda produto interno, matriz de covariância simétrica e ortogonalidade; esses ingredientes não são provados neste curso.

### Checkpoint 7 — sem solução

Para

```text
A = [3 1 0]
    [0 3 0]
    [0 0 2],
```

calcule os autovalores, uma base de cada autoespaço e suas multiplicidades. Decida se `A` é diagonalizável e identifique exatamente qual contagem sustenta a decisão.

---

## Módulo 8 — Potências, dinâmicas e iteração de potência

### Pergunta motivadora

Como prever o efeito de aplicar a mesma transformação centenas de vezes sem multiplicar centenas de matrizes?

### 8.1 Potências por diagonalização

Se `A=PDP^-1`, então

`A^k=(PDP^-1)^k=PD^kP^-1` para todo inteiro `k≥0`.

Os fatores internos `P^-1P` se cancelam. Como `D` é diagonal,

`D^k=diag(λ_1^k,...,λ_n^k)`.

Isso reduz uma dinâmica

`x_(k+1)=Ax_k`

a escalas independentes nas coordenadas de autovetores. Se

`x_0=c_1v_1+...+c_nv_n`, então

`x_k=c_1λ_1^kv_1+...+c_nλ_n^kv_n`.

A fórmula exige uma base de autovetores. Sem diagonalização, ela não pode ser usada dessa forma.

### 8.2 Leitura qualitativa

Para uma dinâmica diagonalizável:

- se todos `|λ_i|<1`, então `x_k→0`;
- se algum termo com `|λ_i|>1` tem coeficiente inicial não nulo, essa componente cresce em módulo;
- `λ_i<0` alterna o sentido da componente;
- `|λ_i|=1` exige análise específica: a componente pode persistir ou oscilar.

Essas conclusões descrevem a decomposição exata. Em ponto flutuante ou em matrizes não diagonalizáveis, outros fenômenos precisam de ferramentas posteriores.

### 8.3 Iteração de potência

A iteração de potência procura uma direção dominante sem calcular todo o polinômio característico:

1. escolha `x_0≠0`;
2. calcule `y_k=Ax_k`;
3. normalize `x_(k+1)=y_k/||y_k||`;
4. estime o autovalor pelo quociente de Rayleigh `(x_k^TAx_k)/(x_k^Tx_k)`.

**Hipóteses de convergência na versão simples:** `A` deve possuir um autovalor dominante único em módulo, `|λ_1|>|λ_2|≥...`, e `x_0` deve ter componente não nula na direção de um autovetor dominante. Para a interpretação mais limpa do quociente de Rayleigh, usamos matrizes reais simétricas neste experimento. Se há empate em módulo ou componente dominante zero, a conclusão pode falhar.

Uma implementação pequena, ainda sem NumPy:

```python
from math import sqrt


def matvec(matrix, vector):
    if any(len(row) != len(vector) for row in matrix):
        raise ValueError("dimensões incompatíveis")
    return [sum(a * x for a, x in zip(row, vector)) for row in matrix]


def dot(left, right):
    return sum(x * y for x, y in zip(left, right))


def power_iteration(matrix, initial, steps=20, tol=1e-15):
    if len(matrix) != len(initial):
        raise ValueError("a matriz deve ser quadrada e compatível com o vetor")
    if any(len(row) != len(initial) for row in matrix):
        raise ValueError("a matriz deve ser quadrada e compatível com o vetor")
    norm = sqrt(dot(initial, initial))
    if norm <= tol:
        raise ValueError("o vetor inicial deve ser não nulo")
    vector = [value / norm for value in initial]

    for _ in range(steps):
        image = matvec(matrix, vector)
        norm = sqrt(dot(image, image))
        if norm <= tol:
            raise ValueError("a iteração atingiu o vetor zero")
        vector = [value / norm for value in image]

    image = matvec(matrix, vector)
    eigenvalue = dot(vector, image) / dot(vector, vector)
    residual = sqrt(
        sum((y - eigenvalue * x) ** 2 for x, y in zip(vector, image))
    )
    return eigenvalue, vector, residual


estimate = power_iteration([[2.0, 1.0], [1.0, 2.0]], [1.0, 0.0])
print(estimate)
```

O resíduo `||Av-λv||` mede quão bem o par aproximado satisfaz a equação. Resíduo pequeno é evidência numérica, não prova de que o valor exato foi identificado.

### 8.4 Síntese aplicada a dados

Uma aplicação responsável deve registrar:

- a matriz e o significado de linhas e colunas;
- a base original e qualquer nova base;
- se os cálculos são exatos ou aproximados;
- o resíduo de pares espectrais aproximados;
- a hipótese que permite interpretar a direção dominante;
- a limitação: correlação, causalidade ou importância semântica não decorrem automaticamente de um autovetor.

### Exemplo resolvido — dinâmica sem multiplicação repetida

Retome

```text
A = [4 1]
    [2 3],
```

com autovetores `v_1=(1,1)` para `λ_1=5` e `v_2=(1,-2)` para `λ_2=2`.

Para `x_0=(3,0)`, resolva

`(3,0)=c_1(1,1)+c_2(1,-2)`.

Das componentes, `c_1+c_2=3` e `c_1-2c_2=0`. Logo `c_2=1` e `c_1=2`.

Portanto,

`x_k=A^kx_0=2·5^k(1,1)+2^k(1,-2)`.

Para `k=2`,

`x_2=50(1,1)+4(1,-2)=(54,42)`.

Conferindo por multiplicação direta:

`Ax_0=(12,6)` e `A(12,6)=(54,42)`.

Como a componente em `v_1` não é zero e `|5|>|2|`, a direção normalizada de `x_k` se aproxima da direção de `(1,1)`.

### Erros comuns

- Usar `A^k=P^kD^k(P^-1)^k`; a identidade correta vem do cancelamento interno e é `PD^kP^-1`.
- Concluir convergência ao zero olhando apenas um autovalor.
- Ignorar que o vetor inicial pode não ter componente na direção dominante.
- Declarar sucesso da iteração apenas porque os números pararam de mudar na impressão; verifique resíduo e tolerância.
- Usar iteração de potência quando há empate no maior módulo sem discutir a hipótese violada.
- Transformar uma associação espectral em interpretação causal.

### Conexão com IA

Aplicações repetidas de operadores aparecem em difusão, propagação de mensagens e métodos iterativos. A direção dominante pode capturar o comportamento de longo prazo, mas apenas sob hipóteses explícitas. O hábito central para IA é auditar representação, escala, convergência e resíduo antes de atribuir significado ao resultado.

### Checkpoint 8 — sem solução

Considere

```text
A = [3 0]
    [0 -2]
```

e `x_0=(1,4)`.

1. Obtenha uma fórmula fechada para `A^kx_0`.
2. Descreva crescimento, alternância de sinal e direção normalizada.
3. Preveja o resultado da iteração de potência.
4. Repita a previsão para `x_0=(0,4)` e explique qual hipótese mudou.

---

## Mapa de dependências conceituais

```text
combinação linear
 ├─> sistemas lineares ──> eliminação ──> posto
 ├─> geração + independência ──> base ──> coordenadas
 └─> subespaços ──> soma/interseção/complemento

base + transformação linear
 ├─> matriz ──> núcleo/imagem ──> posto-nulidade
 └─> mudança de base ──> semelhança

sistemas homogêneos + mudança de base
 └─> autoespaços ──> diagonalização ──> potências/dinâmicas/iteração
```

O próximo passo é resolver as [listas de exercícios](./EXERCICIOS.md) nos pontos indicados pelo [plano do curso](./README.md). As avaliações não possuem gabarito neste repositório.
