# Material de Estudo — MAE111

Este texto é uma primeira exposição autoral e autocontida aos tópicos da ementa. Ele foi escrito para permitir estudo sem depender de uma aula simultânea, mas não pretende substituir um livro completo, a orientação docente nem uma coleção ampla de problemas. Use-o junto ao [plano do curso](./README.md) e às [listas de exercícios](./EXERCICIOS.md).

## Como ler matemática neste curso

Uma **definição** fixa o significado de um termo. Um **teorema** afirma algo que decorre das definições e de resultados anteriores. Antes de aplicar um teorema, verifique suas hipóteses; chamar uma função de contínua ou derivável sem justificativa é comparável a chamar uma função de software com um contrato que talvez não esteja satisfeito.

Nos exemplos, uma igualdade deve decorrer da anterior. Aproximações são indicadas por `≈`, e não por `=`. Gráficos e testes numéricos ajudam a formular conjecturas, mas não demonstram afirmações válidas para infinitos valores.

---

## Módulo 1 — Linguagem de funções reais

### 1.1 O que é uma função

Uma função real de variável real é uma regra que associa a cada elemento `x` de um conjunto `D ⊆ R` exatamente um número real `f(x)`. Escrevemos

`f: D → R`, `x ↦ f(x)`.

O conjunto `D` é o **domínio**. A **imagem** é o conjunto dos valores efetivamente produzidos:

`Im(f) = {f(x) : x ∈ D}`.

O contradomínio declarado e a imagem não precisam coincidir. Duas fórmulas idênticas com domínios distintos definem funções distintas. O gráfico de `f` é o conjunto de pontos `(x, f(x))` no plano.

Ao determinar o domínio de uma fórmula real, imponha simultaneamente todas as restrições:

- denominadores não podem ser zero;
- radicandos de raízes de índice par devem ser não negativos;
- argumentos de logaritmos devem ser positivos;
- outras operações podem trazer restrições próprias.

### Exemplo resolvido 1 — domínio por quadro de sinais

Determine o domínio de

`f(x) = sqrt((x - 1)/(x + 2))`.

Precisamos de `(x - 1)/(x + 2) ≥ 0` e `x ≠ -2`. Os pontos que mudam o sinal são `-2` e `1`. Analisando os intervalos:

- se `x < -2`, numerador e denominador são negativos, logo o quociente é positivo;
- se `-2 < x < 1`, os sinais são diferentes, logo o quociente é negativo;
- se `x ≥ 1`, ambos são não negativos, e `x = 1` é permitido.

Portanto,

`Dom(f) = (-∞, -2) ∪ [1, ∞)`.

Observe que `-2` nunca entra no domínio, mesmo que um procedimento algébrico posterior pareça cancelar algum fator.

### 1.2 Zeros, sinal, simetrias e variação

Um **zero** de `f` é um valor `a` do domínio tal que `f(a)=0`. A função é:

- **crescente** em um intervalo se `x1 < x2` implica `f(x1) ≤ f(x2)`;
- **estritamente crescente** se a desigualdade resultante é estrita;
- **par** se `f(-x)=f(x)` em um domínio simétrico;
- **ímpar** se `f(-x)=-f(x)` em um domínio simétrico;
- **limitada superiormente** se existe `M` com `f(x) ≤ M` para todo `x` do domínio.

Essas propriedades são globais ou relativas a intervalos. Um desenho convincente não substitui sua verificação.

### 1.3 Operações e composição

Soma, produto e quociente são definidos onde todas as expressões envolvidas fazem sentido. A composição

`(f ∘ g)(x) = f(g(x))`

exige duas condições: `x ∈ Dom(g)` e `g(x) ∈ Dom(f)`.

### Exemplo resolvido 2 — composição e domínio

Se `f(u)=sqrt(u)` e `g(x)=1-x²`, então

`(f ∘ g)(x)=sqrt(1-x²)`.

Como a saída de `g` precisa pertencer a `[0,∞)`, temos `1-x² ≥ 0`, ou `-1 ≤ x ≤ 1`. Já

`(g ∘ f)(x)=1-(sqrt(x))²=1-x`,

mas seu domínio continua sendo `[0,∞)`, herdado de `f`. Simplificar a fórmula não autoriza ampliar o domínio original.

### Erros comuns

- Tratar `f(x)` como multiplicação entre `f` e `x`.
- Informar apenas a fórmula e esquecer o domínio.
- Confundir `f(x+h)` com `f(x)+f(h)`.
- Cancelar fatores que podem ser zero sem registrar a restrição original.
- Ler monotonicidade pela ordem dos valores de `y`, sem comparar entradas em um intervalo.

### Conexão com IA e software

Uma função se parece com uma rotina pura, mas o domínio matemático é parte do contrato. `log(x)`, normalização por uma norma e certas funções de perda falham ou mudam de comportamento fora de seus domínios naturais. Em pipelines de aprendizado, composição de camadas é composição de funções; verificar dimensões não elimina a necessidade de verificar o domínio numérico.

### Checkpoint 1 — sem solução

1. Determine o domínio de `ln(4-x²)/(x-1)`.
2. Dê um exemplo de duas funções com a mesma fórmula e imagens diferentes por terem domínios diferentes.
3. Se `f(x)=1/(x-2)` e `g(x)=sqrt(x)`, determine os domínios de `f∘g` e `g∘f`.

---

## Módulo 2 — Famílias, transformações e inversas

### 2.1 Funções elementares

As principais famílias deste curso são:

- polinomiais, como `p(x)=3x³-2x+1`, definidas em todo `R`;
- racionais, quocientes de polinômios, definidas onde o denominador não zera;
- potências e raízes;
- exponenciais `a^x`, com `a>0` e `a≠1`;
- logarítmicas `log_a(x)`, inversas das exponenciais e definidas para `x>0`;
- trigonométricas e suas inversas em domínios restritos;
- funções definidas por partes.

Identidades úteis incluem

`a^(x+y)=a^x a^y`, `ln(ab)=ln(a)+ln(b)`, `sin²x+cos²x=1`.

A identidade logarítmica exige argumentos positivos no contexto real. Além disso, `ln(a+b)` não se separa em uma soma de logaritmos.

### 2.2 Transformações de gráficos

Partindo de `y=f(x)`:

- `f(x)+k` desloca o gráfico verticalmente por `k`;
- `f(x-h)` desloca-o horizontalmente por `h`;
- `a f(x)` escala valores verticalmente e pode refletir o gráfico;
- `f(bx)` produz escala horizontal pelo fator `1/|b|` e pode refletir;
- `|f(x)|` reflete para cima as partes abaixo do eixo;
- `f(|x|)` replica no lado esquerdo o comportamento do lado direito.

O sinal em `f(x-h)` costuma causar confusão: a entrada precisa ser `x=h` para alimentar `0` à função original, por isso o deslocamento é para a direita.

### Exemplo resolvido 1 — leitura de uma transformação

Considere

`g(x)=-2(x-3)²+5`.

Partindo de `f(x)=x²`, o gráfico se desloca 3 unidades à direita, sofre escala vertical por 2, reflete em relação ao eixo `x` e sobe 5 unidades. Seu vértice é `(3,5)`, a imagem é `(-∞,5]` e o eixo de simetria é `x=3`.

### 2.3 Injetividade e função inversa

Uma função é **injetiva** se entradas distintas têm saídas distintas. Somente uma função injetiva possui inversa em sua imagem. Se `f` não for injetiva em todo o domínio, pode ser possível restringi-lo.

A função inversa `f⁻¹` satisfaz

`f⁻¹(f(x))=x` e `f(f⁻¹(y))=y`

nos domínios correspondentes. O expoente `-1` nessa notação não significa recíproco.

### Exemplo resolvido 2 — restrição e inversão

`f(x)=x²` não é injetiva em `R`, pois `f(-2)=f(2)`. Restrinja `f` a `[0,∞)`. Para encontrar a inversa, escreva

`y=x²`, com `x≥0`.

Trocando os papéis das variáveis e isolando a saída,

`x=y²`, com `y≥0`, portanto `f⁻¹(x)=sqrt(x)` para `x≥0`.

### 2.4 Modelos e unidades

Uma fórmula só é um modelo depois que as variáveis, unidades, domínio e hipóteses são declarados. Crescimento exponencial `P(t)=P0 e^(kt)` supõe taxa relativa constante. Uma função afim `C(q)=C0+cq` pode modelar custo fixo mais custo marginal constante. Modelos são aproximações e seu domínio físico costuma ser menor que o domínio algébrico.

### Exemplo resolvido 3 — calibrando um modelo exponencial

Uma cultura começa com 200 células e dobra a cada 3 horas. Procure `P(t)=200e^(kt)`. A condição `P(3)=400` dá

`400=200e^(3k)`, então `e^(3k)=2` e `k=ln(2)/3`.

Logo,

`P(t)=200e^(t ln(2)/3)=200·2^(t/3)`.

O modelo não deve ser extrapolado indefinidamente: recursos limitados invalidariam a hipótese de taxa relativa constante.

### Erros comuns

- Confundir `f⁻¹(x)` com `1/f(x)`.
- Trocar deslocamentos horizontais e verticais.
- Aplicar propriedades de logaritmos a somas.
- Encontrar uma fórmula inversa sem informar domínio e imagem.
- Aceitar todas as raízes algébricas, mesmo quando violam o domínio físico.

### Conexão com IA e software

Funções de ativação são famílias com propriedades diferentes: ReLU é definida por partes; sigmoide é limitada; exponencial e logaritmo aparecem em softmax e log-verossimilhança. Transformações de entrada também aparecem na padronização. Invertibilidade importa em modelos de fluxo normalizante, mas a intuição geométrica vem antes da implementação.

### Checkpoint 2 — sem solução

1. Descreva todas as transformações que levam `y=|x|` a `y=3|x+2|-1`.
2. Restrinja `f(x)=(x-1)²+4` a um intervalo no qual seja inversível e encontre a inversa.
3. Um valor decai 15% por ano. Construa um modelo, declare o domínio temporal razoável e explique por que ele é exponencial.

---

## Módulo 3 — Limites

### 3.1 Aproximação local

Escrever

`lim_(x→a) f(x)=L`

significa que os valores de `f(x)` podem ser tornados arbitrariamente próximos de `L` escolhendo `x` suficientemente próximo de `a`, mas com `x≠a`. O valor `f(a)` pode ser `L`, outro número ou nem existir.

A definição formal é:

> Para todo `ε>0`, existe `δ>0` tal que, se `0<|x-a|<δ`, então `|f(x)-L|<ε`.

O desafio de uma prova `ε-δ` é escolher `δ` a partir de `ε`, sem depender do `x` particular.

### Exemplo resolvido 1 — uma prova linear

Mostre que `lim_(x→2) (3x-1)=5`.

Queremos `|(3x-1)-5|<ε`. Mas

`|(3x-1)-5|=|3x-6|=3|x-2|`.

Escolha `δ=ε/3`. Se `0<|x-2|<δ`, então

`|(3x-1)-5|=3|x-2|<3δ=ε`.

Isso conclui a prova.

### 3.2 Limites laterais e existência

`lim_(x→a-) f(x)` considera `x<a`; `lim_(x→a+) f(x)` considera `x>a`. O limite bilateral existe e vale `L` se, e somente se, os dois limites laterais existem e valem o mesmo número.

### Exemplo resolvido 2 — salto

Se

`f(x)=1`, para `x<0`, e `f(x)=2`, para `x≥0`,

então `lim_(x→0-)f(x)=1` e `lim_(x→0+)f(x)=2`. Como são diferentes, `lim_(x→0)f(x)` não existe, embora `f(0)=2` esteja definido.

### 3.3 Leis de limites e indeterminações

Quando os limites envolvidos existem, limites preservam soma, produto e quociente, neste último caso desde que o limite do denominador não seja zero. Polinômios podem ser avaliados por substituição direta. Funções racionais também, fora dos zeros do denominador.

Uma expressão `0/0` não é uma resposta: é uma **forma indeterminada** que sinaliza a necessidade de transformação. Fatoração, racionalização, identidade trigonométrica e confronto são técnicas frequentes.

### Exemplo resolvido 3 — fatoração

Calcule `lim_(x→3) (x²-9)/(x-3)`.

Para `x≠3`,

`(x²-9)/(x-3)=((x-3)(x+3))/(x-3)=x+3`.

Como o limite ignora o ponto `x=3`, o cancelamento é válido em uma vizinhança perfurada. Logo o limite é `6`.

### Exemplo resolvido 4 — racionalização

Calcule `lim_(x→0) (sqrt(1+x)-1)/x`.

Multiplicando pelo conjugado,

`[(sqrt(1+x)-1)/x]·[(sqrt(1+x)+1)/(sqrt(1+x)+1)]`

`= 1/(sqrt(1+x)+1)` para `x≠0`.

O limite é `1/2`.

### 3.4 Teorema do confronto e limite trigonométrico fundamental

Se `g(x)≤f(x)≤h(x)` perto de `a` e

`lim_(x→a)g(x)=lim_(x→a)h(x)=L`,

então `lim_(x→a)f(x)=L`.

Um resultado fundamental, com ângulos em radianos, é

`lim_(x→0) sin(x)/x = 1`.

Dele seguem limites como `lim_(x→0)(1-cos x)/x=0` e variantes obtidas por substituição.

### Exemplo resolvido 5 — mudança de escala

`lim_(x→0) sin(5x)/(2x)` pode ser escrito como

`(5/2)·[sin(5x)/(5x)]`.

Como `5x→0`, o termo entre colchetes tende a `1`; o limite é `5/2`.

### 3.5 Limites infinitos e no infinito

`lim_(x→a)f(x)=∞` descreve crescimento sem cota, não um número real. Isso pode indicar uma assíntota vertical `x=a`. Já `lim_(x→∞)f(x)=L` descreve comportamento para entradas grandes e pode indicar assíntota horizontal `y=L`.

Para funções racionais no infinito, compare graus ou divida numerador e denominador pela maior potência relevante.

### Exemplo resolvido 6 — comportamento assintótico

Calcule

`lim_(x→∞) (4x²-x+1)/(2x²+3x)`.

Dividindo por `x²`, obtemos

`(4-1/x+1/x²)/(2+3/x)`.

Os termos com `1/x` tendem a zero, então o limite é `4/2=2`.

### Erros comuns

- Substituir o ponto e concluir que `0/0=0`.
- Inferir um limite bilateral a partir de um único lado.
- Tratar `∞` como um número e fazer aritmética ordinária sem análise.
- Usar uma tabela finita como prova.
- Cancelar parcelas em uma soma, como se fossem fatores.
- Usar `lim sin(x)/x=1` com ângulos em graus.

### Conexão com IA e software

Limites descrevem estabilidade quando uma perturbação tende a zero e justificam derivadas usadas em otimização. Computacionalmente, avaliar uma fórmula perto de uma indeterminação pode produzir cancelamento catastrófico. Uma reescrita algebricamente equivalente pode ser numericamente mais estável, mas a evidência de ponto flutuante ainda não demonstra o limite.

### Checkpoint 3 — sem solução

1. Calcule `lim_(x→4) (sqrt(x)-2)/(x-4)` sem regra de l'Hôpital.
2. Determine os limites laterais de `(x+1)/|x+1|` em `x=-1`.
3. Prove pela definição que `lim_(x→1)(2x+4)=6`.

---

## Módulo 4 — Continuidade e seus teoremas

### 4.1 Continuidade em um ponto

Uma função `f` é contínua em `a` quando:

1. `f(a)` está definido;
2. `lim_(x→a)f(x)` existe;
3. `lim_(x→a)f(x)=f(a)`.

Em extremidades de intervalos, usa-se o limite lateral apropriado. A função é contínua em um intervalo se for contínua em todos os seus pontos.

Polinômios são contínuos em `R`; funções racionais são contínuas em seus domínios; raízes, exponenciais, logaritmos e trigonométricas são contínuas em seus domínios. Somas, produtos, quocientes válidos e composições de funções contínuas preservam continuidade.

### 4.2 Tipos de descontinuidade

- **Removível:** o limite existe, mas o valor falta ou é diferente dele.
- **Salto:** limites laterais finitos existem, mas diferem.
- **Infinita:** ao menos um limite lateral cresce sem cota.
- **Oscilatória:** não há aproximação a um único valor por oscilação persistente.

### Exemplo resolvido 1 — extensão contínua

Defina

`f(x)=(x²-1)/(x-1)` se `x≠1`, e `f(1)=c`.

Para `x≠1`, `f(x)=x+1`. Logo

`lim_(x→1)f(x)=2`.

A única escolha que torna `f` contínua em `1` é `c=2`.

### Exemplo resolvido 2 — dois parâmetros

Considere

`f(x)=ax+1` para `x<2`, e `f(x)=x²+b` para `x≥2`.

Para continuidade em `2`, é necessário

`lim_(x→2-)f(x)=f(2)=lim_(x→2+)f(x)`.

Isso produz `2a+1=4+b`. Há uma família de soluções: `b=2a-3`. Uma única condição não determina dois parâmetros.

### 4.3 Teorema do Valor Intermediário

> Se `f` é contínua em `[a,b]` e `N` está entre `f(a)` e `f(b)`, então existe `c∈[a,b]` tal que `f(c)=N`.

Em particular, se `f(a)` e `f(b)` têm sinais opostos, existe ao menos uma raiz em `(a,b)`. O teorema garante existência, não unicidade nem uma fórmula para a raiz.

### Exemplo resolvido 3 — existência de raiz

Seja `p(x)=x³+x-1`. Como polinômios são contínuos,

`p(0)=-1` e `p(1)=1`.

Pelo Teorema do Valor Intermediário, existe `c∈(0,1)` com `p(c)=0`. Além disso, se mais tarde soubermos que `p` é estritamente crescente, poderemos concluir que essa raiz é única; o TVI sozinho não basta.

### 4.4 Teorema dos Valores Extremos

> Se `f` é contínua no intervalo fechado e limitado `[a,b]`, então `f` atinge máximo e mínimo absolutos nesse intervalo.

As três hipóteses importam. Em `(0,1)`, a função `f(x)=x` não atinge máximo nem mínimo. Em `[0,1]`, `f(x)=1/x` para `x>0` com uma definição arbitrária em `0` pode não ser contínua nem limitada.

### Erros comuns

- Dizer que uma função é contínua porque seu gráfico “não levanta o lápis”, sem verificar o ponto.
- Aplicar o TVI a uma função descontínua ou fora de um intervalo fechado.
- Concluir unicidade de raiz a partir do TVI.
- Supor que toda função limitada atinge suas cotas.
- Ajustar `f(a)` para corrigir uma descontinuidade cujo limite nem existe.

### Conexão com IA e software

Continuidade formaliza robustez local: entradas próximas produzem saídas próximas. Redes com ativações contínuas geram composições contínuas, embora possam não ser deriváveis em todos os pontos. Continuidade também permite garantir que certos níveis de perda são atravessados ao longo de um caminho, mas não garante que um algoritmo os encontre.

### Checkpoint 4 — sem solução

1. Classifique a descontinuidade de `(x²-4)/(x-2)` quando a função não é definida em `2`.
2. Encontre uma condição sobre `a` e `b` para tornar contínua em `0` a função `f(x)=ax+b`, se `x<0`, e `f(x)=cos x`, se `x≥0`.
3. Use um teorema para provar que `cos x=x` possui uma solução em `[0,1]`, indicando todas as hipóteses.

---

## Módulo 5 — Derivada: definição e significado

### 5.1 Taxa média e taxa instantânea

A taxa média de variação de `f` entre `a` e `a+h` é

`[f(a+h)-f(a)]/h`, com `h≠0`.

Se o limite existe quando `h→0`, a **derivada de `f` em `a`** é

`f'(a)=lim_(h→0) [f(a+h)-f(a)]/h`.

Equivalentemente,

`f'(a)=lim_(x→a) [f(x)-f(a)]/(x-a)`.

Geometricamente, é a inclinação da reta tangente. Em um modelo posição-tempo, é a velocidade instantânea. A unidade de `f'` é “unidade da saída por unidade da entrada”.

### Exemplo resolvido 1 — derivada pela definição

Para `f(x)=x²`,

`f'(a)=lim_(h→0) [(a+h)²-a²]/h`

`=lim_(h→0) [2ah+h²]/h`

`=lim_(h→0)(2a+h)=2a`.

Portanto `f'(x)=2x`. A reta tangente em `x=3` tem inclinação `6` e passa por `(3,9)`:

`y-9=6(x-3)`.

### 5.2 Derivabilidade e continuidade

> Se `f` é derivável em `a`, então `f` é contínua em `a`.

A recíproca é falsa. Continuidade não garante uma tangente com inclinação finita única.

### Exemplo resolvido 2 — uma quina

Para `f(x)=|x|` em `0`, o quociente diferencial é

`(|h|-0)/h=|h|/h`.

Quando `h→0+`, o quociente tende a `1`; quando `h→0-`, tende a `-1`. A derivada não existe. Ainda assim, `|x|` é contínua em `0`.

Outros motivos para não derivabilidade incluem descontinuidade, tangente vertical e oscilação excessiva.

### 5.3 Função derivada e derivadas de ordem superior

Quando a derivada existe em vários pontos, `f'` é uma nova função. Sua derivada, `f''`, mede a taxa de variação de `f'`. Em movimento, se `s(t)` é posição, `s'(t)` é velocidade e `s''(t)` é aceleração.

Derivadas fundamentais:

- `(c)'=0`;
- `(x^n)'=nx^(n-1)` para os expoentes no domínio considerado;
- `(e^x)'=e^x`;
- `(a^x)'=a^x ln a`;
- `(ln x)'=1/x`, para `x>0`;
- `(sin x)'=cos x`;
- `(cos x)'=-sin x`.

As regras serão sistematizadas no módulo seguinte.

### 5.4 Linearização e diferencial

Perto de `x=a`, uma função derivável é aproximada por sua reta tangente:

`f(x)≈L(x)=f(a)+f'(a)(x-a)`.

Escrevendo `dx=x-a`, a variação linear prevista é `dy=f'(a)dx`. A variação real é `Δy=f(a+dx)-f(a)`. A diferença entre ambas tende a ser pequena em comparação com `dx` quando `dx→0`.

### Exemplo resolvido 3 — estimativa local

Estime `sqrt(4,04)`. Tome `f(x)=sqrt(x)` e `a=4`. Como `f(4)=2` e `f'(4)=1/(2sqrt(4))=1/4`,

`sqrt(4,04)≈2+(1/4)(0,04)=2,01`.

A estimativa é local; usar a mesma linearização longe de `4` pode produzir erro significativo.

### Erros comuns

- Substituir `h=0` antes de simplificar o quociente.
- Confundir `f'(a)` com `f(a)/a`.
- Supor que continuidade implica derivabilidade.
- Esquecer que a inclinação pode depender do ponto.
- Usar linearização longe do centro sem discutir erro.

### Conexão com IA e software

Treinamento por gradiente usa derivadas como sensibilidades locais. Uma diferença finita `[f(x+h)-f(x)]/h` pode conferir uma derivada implementada, mas `h` muito grande traz erro de aproximação e `h` muito pequeno traz arredondamento. Derivação automática aplica regras exatas ao grafo de operações; não é o mesmo que diferenciação numérica nem prova que o modelo é adequado.

### Checkpoint 5 — sem solução

1. Use a definição para encontrar a derivada de `f(x)=1/x` em um ponto `a≠0`.
2. Dê uma função contínua em `0` que não seja derivável ali e explique com derivadas laterais.
3. Linearize `f(x)=x^(1/3)` em `x=8` e use a linearização para estimar `8,12^(1/3)`.

---

## Módulo 6 — Regras de derivação

### 6.1 Álgebra de derivadas

Para funções deriváveis `f` e `g` e constante `c`:

- `(cf)'=cf'`;
- `(f+g)'=f'+g'`;
- `(fg)'=f'g+fg'`;
- `(f/g)'=(f'g-fg')/g²`, onde `g≠0`.

A derivada do produto não é o produto das derivadas. As fórmulas surgem da definição e preservam informações cruzadas sobre os dois fatores.

### Exemplo resolvido 1 — produto e quociente

Se `f(x)=x²e^x`, então

`f'(x)=2xe^x+x²e^x=e^x(x²+2x)`.

Se `g(x)=sin x/x`, para `x≠0`, então

`g'(x)=[x cos x-sin x]/x²`.

### 6.2 Regra da cadeia

Se `y=f(u)` e `u=g(x)`, então

`d/dx f(g(x))=f'(g(x))g'(x)`.

Ela deriva a composição de fora para dentro, multiplicando pelas taxas internas. Em uma composição com várias camadas, cada camada contribui com um fator.

### Exemplo resolvido 2 — composição em camadas

Derive `y=ln(1+e^(x²))`.

As camadas são logaritmo, soma, exponencial e quadrado:

`y'=[1/(1+e^(x²))]·e^(x²)·2x`

`=2xe^(x²)/(1+e^(x²))`.

O domínio é todo `R`, pois `1+e^(x²)>0`.

### 6.3 Derivação implícita

Nem toda curva vem isolada como `y=f(x)`. Se uma relação `F(x,y)=0` define localmente `y` como função de `x`, derive os dois lados lembrando que `y` depende de `x`.

### Exemplo resolvido 3 — círculo

Na curva `x²+y²=25`, derivando em relação a `x`:

`2x+2y y'=0`,

logo `y'=-x/y`, quando `y≠0`. No ponto `(3,4)`, a inclinação é `-3/4`. Nos pontos com `y=0`, a fórmula sinaliza tangentes verticais, e não uma divisão permitida por zero.

### 6.4 Derivadas de inversas

Se `f` é invertível, derivável e `f'(f⁻¹(x))≠0`, então

`(f⁻¹)'(x)=1/f'(f⁻¹(x))`.

Essa relação produz, por exemplo,

`(arctan x)'=1/(1+x²)`

e fórmulas para outras trigonométricas inversas em seus domínios.

### 6.5 Diferenciação logarítmica

Logaritmos transformam produtos em somas e expoentes em fatores. Para `y>0`, tomar `ln` dos dois lados pode simplificar potências variáveis.

### Exemplo resolvido 4 — potência variável

Para `y=x^x`, com `x>0`,

`ln y=x ln x`.

Derivando implicitamente,

`y'/y=ln x+1`.

Assim,

`y'=x^x(ln x+1)`.

### 6.6 Tabela ampliada

- `(tan x)'=sec²x`;
- `(sec x)'=sec x tan x`;
- `(arcsin x)'=1/sqrt(1-x²)` para `|x|<1`;
- `(arctan x)'=1/(1+x²)`;
- `(ln|x|)'=1/x` para `x≠0`.

Memorizar uma tabela não substitui identificar a estrutura. Antes de derivar, marque somas, produtos, quocientes e composições.

### Erros comuns

- Escrever `(fg)'=f'g'`.
- Omitir a derivada interna na regra da cadeia.
- Tratar `y` como constante na derivação implícita.
- Simplificar antes de registrar restrições de domínio.
- Aplicar logaritmo a uma expressão que pode não ser positiva sem usar `ln|·|` ou discutir intervalos.

### Conexão com IA e software

Backpropagation é a regra da cadeia organizada para reutilizar derivadas intermediárias. Em um grafo profundo, produtos repetidos de derivadas ajudam a explicar gradientes muito pequenos ou grandes. Entender a regra permite auditar uma implementação e interpretar o resultado, em vez de tratar `backward()` como uma caixa-preta.

### Checkpoint 6 — sem solução

1. Derive `[(x²+1)/(x-1)]³`, indicando domínio.
2. Encontre a reta tangente à curva `x³+y³=6xy` no ponto `(3,3)`.
3. Use diferenciação logarítmica para derivar `y=(sin x)^x` em um intervalo adequado.

---

## Módulo 7 — Aplicações de derivadas, Rolle e TVM

### 7.1 Extremos e pontos críticos

Um máximo absoluto de `f` em `D` ocorre em `c` se `f(c)≥f(x)` para todo `x∈D`; máximos locais comparam apenas uma vizinhança. Um **ponto crítico** do domínio é um ponto onde `f'(c)=0` ou `f'(c)` não existe.

> Teorema de Fermat: se `f` tem extremo local em um ponto interior `c` e é derivável em `c`, então `f'(c)=0`.

A recíproca é falsa: `f'(c)=0` não garante extremo. Em um intervalo fechado, candidatos a extremos absolutos incluem pontos críticos interiores e extremidades.

### 7.2 Teoremas de Rolle e do Valor Médio

> **Rolle:** se `f` é contínua em `[a,b]`, derivável em `(a,b)` e `f(a)=f(b)`, então existe `c∈(a,b)` com `f'(c)=0`.

> **Teorema do Valor Médio (TVM):** se `f` é contínua em `[a,b]` e derivável em `(a,b)`, então existe `c∈(a,b)` tal que
>
> `f'(c)=[f(b)-f(a)]/(b-a)`.

Rolle é o caso de taxa média zero. O TVM liga uma variação total a uma taxa instantânea e sustenta resultados como: se `f'=0` em um intervalo, então `f` é constante nele.

### Exemplo resolvido 1 — aplicação do TVM

Para `f(x)=sqrt(x)` em `[1,4]`, as hipóteses valem. A taxa média é

`[f(4)-f(1)]/(4-1)=(2-1)/3=1/3`.

Como `f'(x)=1/(2sqrt(x))`, buscamos

`1/(2sqrt(c))=1/3`.

Logo `sqrt(c)=3/2` e `c=9/4`, que pertence a `(1,4)`.

### 7.3 Crescimento, concavidade e esboço

Se `f'>0` em um intervalo, `f` é crescente ali; se `f'<0`, é decrescente. Mudança de sinal de `+` para `-` em um ponto crítico indica máximo local pelo teste da primeira derivada; de `-` para `+`, mínimo local.

Se `f''>0`, o gráfico é côncavo para cima; se `f''<0`, côncavo para baixo. Um ponto de inflexão exige mudança de concavidade. A condição `f''=0` apenas produz um candidato.

No teste da segunda derivada, se `f'(c)=0` e `f''(c)>0`, há mínimo local; se `f''(c)<0`, máximo local. Se `f''(c)=0`, o teste é inconclusivo.

### Exemplo resolvido 2 — análise de uma cúbica

Se `f(x)=x³-3x`, então

`f'(x)=3x²-3=3(x-1)(x+1)`.

Assim, `f` cresce em `(-∞,-1)` e `(1,∞)` e decresce em `(-1,1)`. Há máximo local em `x=-1`, com `f(-1)=2`, e mínimo local em `x=1`, com `f(1)=-2`.

Como `f''(x)=6x`, a concavidade muda em `x=0`; `(0,0)` é ponto de inflexão.

### 7.4 Otimização

Um procedimento confiável:

1. nomeie variáveis e unidades;
2. escreva a quantidade a otimizar;
3. use as restrições para obter uma função de uma variável;
4. determine o domínio físico;
5. encontre candidatos e compare valores;
6. interprete e verifique a resposta.

### Exemplo resolvido 3 — área máxima

Um retângulo tem perímetro `20 m`. Se os lados são `x` e `y`, então `2x+2y=20`, ou `y=10-x`, com `0<x<10`. A área é

`A(x)=x(10-x)=10x-x²`.

`A'(x)=10-2x`, então o único ponto crítico é `x=5`. Como `A''(x)=-2<0`, ele dá máximo. Logo `x=y=5 m` e a área máxima é `25 m²`.

### 7.5 Taxas relacionadas

Quando variáveis dependem do tempo, derive uma relação antes de substituir o instante. As unidades ajudam a detectar erros.

### Exemplo resolvido 4 — círculo em expansão

O raio de um círculo cresce a `2 cm/s`. Qual a taxa de variação da área quando `r=5 cm`?

De `A=πr²`, derivando em relação a `t`:

`dA/dt=2πr·dr/dt`.

No instante dado,

`dA/dt=2π·5·2=20π cm²/s`.

### 7.6 Regra de l'Hôpital

Sob hipóteses apropriadas, se `f(x)` e `g(x)` tendem ambos a `0` ou ambos crescem em módulo sem cota, e `g'(x)≠0` perto do ponto, então, quando o limite do quociente das derivadas existe,

`lim f(x)/g(x)=lim f'(x)/g'(x)`.

Ela se aplica a formas `0/0` e `∞/∞`, não a qualquer quociente. Outras formas, como `0·∞` ou `∞-∞`, precisam ser transformadas primeiro.

### Exemplo resolvido 5 — uso e limite da técnica

`lim_(x→0) (e^x-1)/x` tem forma `0/0`. Pela regra,

`lim_(x→0) e^x/1=1`.

Já `lim_(x→0) (1+x)^(1/x)` não é quociente `0/0`; é forma `1^∞`. Seria necessário tomar logaritmo e transformar o problema antes de considerar l'Hôpital.

### 7.7 Método de Newton

Para aproximar uma raiz de `f(x)=0`, linearize em `x_n` e use a raiz da reta tangente:

`x_(n+1)=x_n-f(x_n)/f'(x_n)`.

O método pode convergir rapidamente perto de uma raiz simples, mas pode divergir, entrar em ciclos ou falhar quando a derivada é zero. Uma aproximação numérica não substitui uma prova de existência.

### Erros comuns

- Procurar apenas pontos onde `f'=0` e esquecer extremidades ou pontos não deriváveis.
- Aplicar Rolle ou TVM sem verificar continuidade e derivabilidade nos intervalos corretos.
- Chamar todo ponto com `f''=0` de inflexão.
- Otimizar em um domínio algébrico que viola o problema físico.
- Substituir valores antes de derivar em taxas relacionadas.
- Usar l'Hôpital quando não há forma indeterminada adequada.

### Conexão com IA e software

Otimização de uma função de perda usa informação local, mas modelos reais têm muitas variáveis e pontos críticos complexos. O TVM fundamenta cotas de variação a partir de cotas da derivada, ideia próxima a controle de sensibilidade e constantes de Lipschitz. Método de Newton inspira algoritmos de segunda ordem, mas custo e estabilidade importam em alta dimensão.

### Checkpoint 7 — sem solução

1. Verifique as hipóteses do TVM para `f(x)=1/x` em `[1,4]` e encontre todos os valores garantidos de `c`.
2. Uma caixa sem tampa deve ter volume fixo. Formule, mas não resolva numericamente, a minimização da área de material em um caso de base quadrada.
3. Analise crescimento, extremos e concavidade de `f(x)=x⁴-4x²`.

---

## Módulo 8 — Integral definida e somas de Riemann

### 8.1 De somas a acumulação

Divida `[a,b]` em subintervalos

`a=x0<x1<...<xn=b`.

Escolha um ponto `x_i*` em cada subintervalo e forme a soma

`Σ_(i=1)^n f(x_i*) Δx_i`, onde `Δx_i=x_i-x_(i-1)`.

Se essas somas tendem a um único número quando a maior largura dos subintervalos tende a zero, independentemente das escolhas de amostra, `f` é integrável e definimos

`∫_a^b f(x) dx`

como esse limite. Funções contínuas em intervalos fechados são integráveis.

Para partições regulares, `Δx=(b-a)/n`. Pontos à esquerda, à direita ou médios produzem aproximações diferentes para `n` finito, mas convergem ao mesmo valor quando a função é integrável.

### 8.2 Área com sinal

A integral definida mede acumulação líquida. Regiões acima do eixo contribuem positivamente; abaixo, negativamente. A área geométrica entre o gráfico e o eixo é obtida integrando `|f|` ou separando onde o sinal muda.

### Exemplo resolvido 1 — integral pela definição

Calcule `∫_0^1 x dx` usando extremos direitos. Temos `Δx=1/n` e `x_i=i/n`. A soma é

`S_n=Σ_(i=1)^n (i/n)(1/n)`

`=(1/n²)Σ_(i=1)^n i`

`=(1/n²)·n(n+1)/2`

`=(n+1)/(2n)`.

Tomando `n→∞`, obtemos `1/2`.

### 8.3 Propriedades

Para funções integráveis:

- `∫_a^a f=0`;
- `∫_a^b f=-∫_b^a f`;
- `∫_a^b (αf+βg)=α∫_a^b f+β∫_a^b g`;
- `∫_a^b f=∫_a^c f+∫_c^b f`;
- se `f≤g`, então `∫_a^b f≤∫_a^b g`, para `a≤b`;
- se `m≤f≤M`, então `m(b-a)≤∫_a^b f≤M(b-a)`.

Se `f` é ímpar, `∫_(-a)^a f=0`. Se é par, `∫_(-a)^a f=2∫_0^a f`.

### Exemplo resolvido 2 — usar simetria e dados

Suponha `∫_0^2 f(x)dx=3` e `∫_2^5 f(x)dx=-1`. Então

`∫_0^5 f(x)dx=3+(-1)=2`.

Além disso, `∫_5^0 f(x)dx=-2`. Nenhuma fórmula de `f` foi necessária.

### 8.4 Antiderivadas

Uma função `F` é antiderivada de `f` em um intervalo se `F'=f`. Todas as antiderivadas diferem por uma constante nesse intervalo, por isso escrevemos

`∫ f(x)dx=F(x)+C`.

Essa integral **indefinida** representa uma família de funções; não é o mesmo objeto que a integral definida, que é um número. O Teorema Fundamental do Cálculo conectará os dois.

Algumas antiderivadas básicas:

- `∫x^n dx=x^(n+1)/(n+1)+C`, para `n≠-1`;
- `∫1/x dx=ln|x|+C` em intervalos que não cruzam zero;
- `∫e^x dx=e^x+C`;
- `∫cos x dx=sin x+C`;
- `∫sin x dx=-cos x+C`.

### Erros comuns

- Confundir soma de alturas com soma de áreas e esquecer `Δx`.
- Dizer que toda integral é área positiva.
- Misturar integral definida com `+C`.
- Aplicar fórmulas de simetria em intervalo não simétrico.
- Supor que qualquer função limitada é automaticamente integrável sem considerar o nível do curso e as hipóteses disponíveis.

### Conexão com IA e software

Somas de Riemann são um caso de discretização: uma acumulação contínua é aproximada por uma soma finita. Integrais aparecem na normalização de densidades e em valores esperados contínuos. Computação numérica aproxima a integral; o erro depende do método, da malha e da regularidade da função.

### Checkpoint 8 — sem solução

1. Escreva, sem calcular, uma soma de Riemann com extremos esquerdos para `∫_2^5 (1+x²)dx`.
2. Explique por que `∫_(-2)^2 x³ dx=0` não significa que a área geométrica seja zero.
3. A partir de propriedades de integrais, obtenha limites superior e inferior para `∫_0^1 e^(-x²)dx` sem encontrar uma antiderivada.

---

## Módulo 9 — Teorema Fundamental do Cálculo

### 9.1 Acumulação gera antiderivada

> **TFC, parte I:** se `f` é contínua em `[a,b]` e
>
> `G(x)=∫_a^x f(t)dt`,
>
> então `G` é derivável em `(a,b)` e `G'(x)=f(x)`.

A variável `t` é muda: ela evita conflito com o limite superior `x`. Intuitivamente, ao aumentar `x` em uma pequena quantidade `h`, a acumulação cresce aproximadamente como `f(x)h`; dividir por `h` revela `f(x)`.

### Exemplo resolvido 1 — derivar uma acumulação

Se

`G(x)=∫_1^(x²) cos(t²)dt`,

defina primeiro `H(u)=∫_1^u cos(t²)dt`. Pelo TFC, `H'(u)=cos(u²)`. Como `G(x)=H(x²)`, a regra da cadeia dá

`G'(x)=cos((x²)²)·2x=2x cos(x⁴)`.

Não foi preciso encontrar uma antiderivada elementar de `cos(t²)`.

Se ambos os limites variam, use

`∫_(u(x))^(v(x)) f(t)dt=∫_a^(v(x))f(t)dt-∫_a^(u(x))f(t)dt`.

Assim, a derivada é `f(v(x))v'(x)-f(u(x))u'(x)`.

### 9.2 Antiderivadas calculam integrais definidas

> **TFC, parte II:** se `f` é contínua em `[a,b]` e `F` é qualquer antiderivada de `f`, então
>
> `∫_a^b f(x)dx=F(b)-F(a)`.

Usa-se frequentemente a notação `[F(x)]_a^b`.

### Exemplo resolvido 2 — cálculo exato

`∫_0^2 (3x²-4x+1)dx`

`=[x³-2x²+x]_0^2`

`=(8-8+2)-0=2`.

O `+C` não aparece: qualquer constante cancelaria em `F(b)-F(a)`.

### 9.3 Teorema da variação líquida

Se `Q'(t)` é a taxa de mudança de uma quantidade, então

`Q(b)-Q(a)=∫_a^b Q'(t)dt`.

Isso distingue quantidade acumulada de taxa. Integrar velocidade dá deslocamento; integrar rapidez dá distância. Integrar vazão líquida dá variação de volume.

### Exemplo resolvido 3 — deslocamento e distância

Uma partícula tem velocidade `v(t)=2t-2` em `0≤t≤3`. O deslocamento é

`∫_0^3 (2t-2)dt=[t²-2t]_0^3=3`.

Para a distância, separe em `t=1`, onde a velocidade muda de sinal:

`∫_0^3 |2t-2|dt`

`=-∫_0^1(2t-2)dt+∫_1^3(2t-2)dt`

`=1+4=5`.

### 9.4 Substituição como regra da cadeia ao contrário

Se `u=g(x)` e `du=g'(x)dx`, então

`∫ f(g(x))g'(x)dx=∫f(u)du`.

Em uma integral definida, transforme também os limites ou volte à variável original antes de avaliá-los.

### Exemplo resolvido 4 — substituição definida

Calcule `∫_0^1 2x e^(x²)dx`. Tome `u=x²`, `du=2x dx`. Os novos limites são `u=0` e `u=1`:

`∫_0^1 e^u du=[e^u]_0^1=e-1`.

### Erros comuns

- Derivar o integrando em vez da função acumulação.
- Esquecer a regra da cadeia quando o limite é `g(x)`.
- Misturar limites em `x` com uma integral reescrita em `u`.
- Acrescentar `+C` ao resultado de uma integral definida.
- Confundir deslocamento com distância total.

### Conexão com IA e software

O TFC afirma que diferenciação e acumulação são operações inversas sob hipóteses adequadas. Em modelos contínuos, uma taxa instantânea pode reconstruir uma trajetória por integração. Neural ODEs exploram essa perspectiva, mas sua implementação numérica aproxima a trajetória e adiciona questões de erro e estabilidade que não alteram o teorema matemático.

### Checkpoint 9 — sem solução

1. Derive `F(x)=∫_(sin x)^(x²) ln(1+t²)dt`.
2. Calcule `∫_1^e (1/x)dx` pelo TFC e interprete o resultado.
3. Uma taxa `r(t)` muda de sinal. Explique como calcular acumulação líquida e acumulação total, distinguindo as duas.

---

## Módulo 10 — Técnicas de integração

Não existe uma regra universal simples para antiderivadas. A técnica é escolhida pela estrutura do integrando, e algumas funções elementares não têm antiderivada expressável por funções elementares.

### 10.1 Substituição

Procure uma composição acompanhada, a menos de constante, pela derivada da função interna.

### Exemplo resolvido 1

`∫ x/(1+x²) dx`.

Com `u=1+x²`, `du=2x dx`:

`∫ x/(1+x²)dx=(1/2)∫du/u=(1/2)ln(1+x²)+C`.

Como `1+x²>0`, o módulo é dispensável aqui.

### 10.2 Integração por partes

Da regra do produto,

`∫u dv=uv-∫v du`.

Escolha `u` para ficar mais simples ao derivar e `dv` para ser facilmente integrável. Logaritmos, funções trigonométricas inversas e polinômios frequentemente sugerem a escolha.

### Exemplo resolvido 2

Calcule `∫x e^x dx`. Tome `u=x`, `dv=e^x dx`, então `du=dx`, `v=e^x`:

`∫x e^x dx=xe^x-∫e^x dx=e^x(x-1)+C`.

### Exemplo resolvido 3 — repetição

Para `I=∫e^x cos x dx`, use partes duas vezes:

`I=e^x cos x+∫e^x sin x dx`

e

`∫e^x sin x dx=e^x sin x-I`.

Logo `I=e^x(cos x+sin x)-I`, portanto

`I=(e^x/2)(sin x+cos x)+C`.

### 10.3 Integrais trigonométricas

Identidades convertem produtos e potências:

`sin²x=(1-cos 2x)/2`,

`cos²x=(1+cos 2x)/2`,

`1+tan²x=sec²x`.

Em potências de seno e cosseno, uma potência ímpar permite separar um fator e usar substituição; se ambas são pares, identidades de meia-ângulo costumam ajudar.

### Exemplo resolvido 4

`∫sin³x cos²x dx`.

Escreva `sin³x=(1-cos²x)sin x`. Com `u=cos x`, `du=-sin x dx`:

`-∫(1-u²)u²du=-∫(u²-u⁴)du`

`=-u³/3+u⁵/5+C`

`=-cos³x/3+cos⁵x/5+C`.

### 10.4 Substituições trigonométricas

Expressões com raízes quadráticas podem combinar com identidades:

- `sqrt(a²-x²)`: use `x=a sin θ`;
- `sqrt(a²+x²)`: use `x=a tan θ`;
- `sqrt(x²-a²)`: use `x=a sec θ`, com intervalos apropriados.

A escolha transforma a raiz, mas exige cuidado ao retornar à variável original e ao controlar sinais.

### Exemplo resolvido 5

Calcule `∫dx/sqrt(9-x²)` para `|x|<3`. Tome `x=3sin θ`, com `θ∈(-π/2,π/2)`. Então `dx=3cos θ dθ` e `sqrt(9-x²)=3cos θ`. Logo

`∫dθ=θ+C=arcsin(x/3)+C`.

### 10.5 Frações parciais

Uma função racional própria pode ser decomposta após fatorar o denominador. Para fatores lineares distintos,

`1/[(x-1)(x+2)]=A/(x-1)+B/(x+2)`.

Multiplicando pelo denominador,

`1=A(x+2)+B(x-1)`.

Tomando `x=1`, `A=1/3`; tomando `x=-2`, `B=-1/3`. Portanto,

`∫dx/[(x-1)(x+2)]`

`=(1/3)ln|x-1|-(1/3)ln|x+2|+C`

em qualquer intervalo que não atravesse os polos. Se o grau do numerador for maior ou igual ao do denominador, faça divisão polinomial primeiro. Fatores repetidos e quadráticos irredutíveis exigem termos adicionais na decomposição.

### 10.6 Integrais impróprias

Quando o intervalo é infinito ou o integrando é ilimitado, a integral é definida por limite. Por exemplo,

`∫_1^∞ 1/x^p dx = lim_(b→∞)∫_1^b x^(-p)dx`.

Para `p>1`, o limite converge e vale `1/(p-1)`. Para `p≤1`, diverge. Em um ponto singular interno, separe a integral e exija convergência dos dois lados.

### Exemplo resolvido 6

`∫_1^∞ 1/x² dx`

`=lim_(b→∞)[-1/x]_1^b`

`=lim_(b→∞)(1-1/b)=1`.

Escrever diretamente `[-1/x]_1^∞` é apenas uma abreviação; a definição é o limite.

### 10.7 Como escolher uma técnica

1. Simplifique algebricamente e reconheça uma fórmula básica.
2. Procure composição mais derivada interna: substituição.
3. Procure produto cujo fator se simplifica ao derivar: partes.
4. Para funções racionais, faça divisão e frações parciais.
5. Para potências trigonométricas ou raízes quadráticas, use identidades adequadas.
6. Se houver limite infinito ou singularidade, trate como imprópria.
7. Ao final, derive sua antiderivada para conferir.

### Erros comuns

- Forçar substituição sem transformar todo o diferencial.
- Esquecer o sinal em integração por partes.
- Aplicar frações parciais antes da divisão polinomial.
- Abandonar módulos em logaritmos sem restringir o intervalo.
- Considerar toda integral imprópria convergente porque uma antiderivada formal existe.
- Misturar `x`, `u` e `θ` na mesma etapa sem relações explícitas.

### Conexão com IA e software

Densidades de probabilidade frequentemente exigem integrais impróprias e constantes de normalização. Muitas não têm forma elementar, levando a quadratura ou amostragem. Bibliotecas simbólicas tentam selecionar técnicas, mas podem devolver condições de domínio ou formas especiais; conferir por derivação e analisar convergência continuam sendo tarefas matemáticas.

### Checkpoint 10 — sem solução

1. Escolha e justifique uma técnica para `∫x² ln x dx`, sem concluir a conta.
2. Decomponha, sem integrar, `(2x+1)/(x²-x-2)` em frações parciais.
3. Determine para quais valores reais de `p` a integral `∫_0^1 x^(-p)dx` converge.

---

## Módulo 11 — Aplicações de integrais e síntese

### 11.1 Área entre curvas

Se `f(x)≥g(x)` em `[a,b]`, a área entre os gráficos é

`A=∫_a^b [f(x)-g(x)]dx`.

Encontre interseções e verifique qual função está acima. Se a ordem muda, separe a integral. Também é possível integrar em relação a `y` usando “direita menos esquerda”.

### Exemplo resolvido 1 — parábola e reta

Encontre a área entre `y=x` e `y=x²`. As interseções satisfazem `x=x²`, logo `x=0` ou `x=1`. Em `[0,1]`, `x≥x²`. Assim,

`A=∫_0^1(x-x²)dx`

`=[x²/2-x³/3]_0^1=1/2-1/3=1/6`.

### 11.2 Volumes por discos e anéis

Ao girar uma região em torno de um eixo, uma seção perpendicular pode formar disco ou anel:

`V=π∫_a^b [R(x)²-r(x)²]dx`,

onde `R` e `r` são raios externo e interno medidos até o eixo de rotação.

### Exemplo resolvido 2 — rotação em torno do eixo x

A região sob `y=sqrt(x)`, entre `x=0` e `x=4`, gira em torno do eixo `x`. Cada seção é um disco de raio `sqrt(x)`:

`V=π∫_0^4(sqrt(x))²dx=π∫_0^4x dx=8π`.

Se as unidades de `x` e `y` são centímetros, o volume está em `cm³`.

### 11.3 Cascas cilíndricas

Uma tira paralela ao eixo de rotação gera uma casca. Ao girar em torno do eixo `y`,

`V=2π∫_a^b (raio)(altura)dx`.

O método pode evitar resolver `x` em função de `y`.

### Exemplo resolvido 3 — mesmo sólido por cascas

A região sob `y=sqrt(x)`, `0≤x≤4`, gira em torno do eixo `y`. O raio é `x` e a altura é `sqrt(x)`:

`V=2π∫_0^4 x sqrt(x)dx`

`=2π[x^(5/2)/(5/2)]_0^4`

`=(4π/5)·32=128π/5`.

Este é outro eixo de rotação, portanto não deve coincidir com o volume do exemplo anterior.

### 11.4 Valor médio de uma função

Para `f` contínua em `[a,b]`, seu valor médio é

`f_med=1/(b-a)∫_a^b f(x)dx`.

O Teorema do Valor Médio para Integrais garante um `c∈[a,b]` com `f(c)=f_med`.

### Exemplo resolvido 4 — temperatura média

Se `T(t)=20+4t-t²` em `0≤t≤4` horas, então

`T_med=(1/4)∫_0^4(20+4t-t²)dt`

`=(1/4)[20t+2t²-t³/3]_0^4`

`=(1/4)(80+32-64/3)=68/3`.

A unidade continua sendo temperatura, pois a integral temperatura·tempo foi dividida pelo comprimento temporal.

### 11.5 Comprimento de arco

Para uma curva suave `y=f(x)` em `[a,b]`, aproximar pequenos trechos por segmentos e passar ao limite leva a

`L=∫_a^b sqrt(1+[f'(x)]²)dx`.

Nem sempre essa integral tem antiderivada elementar.

### Exemplo resolvido 5 — segmento reobtido

Para `f(x)=2x+1` em `[0,3]`, `f'(x)=2`. Então

`L=∫_0^3 sqrt(1+4)dx=3sqrt(5)`.

Isso coincide com a distância entre `(0,1)` e `(3,7)`:

`sqrt(3²+6²)=3sqrt(5)`.

### 11.6 Estratégia de modelagem integral

1. Identifique uma pequena contribuição: área de tira, volume de seção, trabalho elementar ou quantidade acumulada.
2. Expresse-a como “densidade ou taxa × pequena largura”.
3. Determine os limites e a variável de integração.
4. Passe à integral e só então escolha a técnica de cálculo.
5. Confira sinal, unidade, ordem de grandeza e dependência dos parâmetros.

O cálculo simbólico é apenas uma etapa. Uma integral correta para o objeto errado continua sendo uma solução errada.

### Erros comuns

- Integrar “curva de baixo menos curva de cima” e aceitar área negativa.
- Usar diâmetro no lugar de raio em discos e cascas.
- Esquecer o quadrado dos raios no método dos anéis.
- Calcular valor médio sem dividir pelo comprimento do intervalo.
- Escolher `dx` quando as seções descritas naturalmente exigem `dy`, sem reformular os limites.
- Omitir unidades e interpretação.

### Conexão com IA e software

Valor esperado é um valor médio ponderado por uma densidade. Áreas e volumes também lembram a integração de densidades para obter massa ou probabilidade. Métodos de Monte Carlo aproximam integrais por amostras, úteis em alta dimensão, mas aqui a prioridade é formular corretamente a integral unidimensional e entender o objeto acumulado.

### Checkpoint 11 — sem solução

1. Monte duas integrais equivalentes, uma em `x` e outra em `y`, para a área limitada por `y=x²` e `y=2x`.
2. Formule por anéis e por cascas o volume gerado pela rotação dessa região em torno do eixo `y`.
3. Explique, por unidades, por que `1/(b-a)∫_a^b f(x)dx` tem a mesma unidade de `f`.

---

## Síntese: o encadeamento do curso

Funções descrevem dependências. Limites formalizam comportamento local e permitem definir continuidade e derivada. Derivadas medem variação instantânea; seus teoremas conectam informação local a comportamento em intervalos. Somas de Riemann definem acumulação, e o Teorema Fundamental do Cálculo mostra que acumular e diferenciar são operações inversas sob hipóteses adequadas. Técnicas de integração ampliam o repertório de cálculos, enquanto aplicações exigem voltar ao significado das variáveis.

Antes das avaliações, você deve conseguir responder a quatro perguntas diante de qualquer solução:

1. Qual é o domínio e quais são as unidades?
2. Que definição ou teorema autoriza esta etapa?
3. As hipóteses foram verificadas?
4. O resultado é plausível em sinal, escala e comportamento limite?

Prossiga para as [dez listas de exercícios](./EXERCICIOS.md). As provas estão em [P1](./avaliacoes/P1.md), [P2](./avaliacoes/P2.md) e [PF](./avaliacoes/PF.md); abra cada uma apenas quando estiver pronto para realizá-la nas condições indicadas.
