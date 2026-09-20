# Material de Estudo — MAE111

Este texto autoral acompanha o programa detalhado da página oficial [Cálculo Infinitesimal I (MAE 111), IM/UFRJ](https://www.im.ufrj.br/index.php/pt/ensino/graduacao/programa-especial-de-matematica/ementas-do-programa-especial-de-matematica/324-calculo-infinitesimal-i-mae-111). É uma rota substancial e autocontida pelo curso, mas não pretende substituir um livro completo, aulas, monitoria ou uma coleção extensa de problemas.

Use-o com o [plano](./README.md) e as [listas](./EXERCICIOS.md). Definições fixam significados; teoremas só podem ser usados depois da verificação de hipóteses. Uma tabela ou execução de Python fornece evidência finita, não uma demonstração sobre infinitos objetos.

## Convenções

- `N={1,2,3,...}`; quando zero for incluído, isso será dito.
- Intervalos são subconjuntos de `R`; `D` denota em geral um domínio.
- `Σ_(n=1)^∞a_n` significa o limite das somas parciais, quando existe.
- `≈` indica aproximação; `=` indica igualdade.
- Nas primeiras unidades, algumas funções conhecidas são usadas operacionalmente. Sua construção rigorosa aparece depois.

---

## Módulo 1 — Ideias fundamentais

### 1.1 Funções e modelos

Uma função `f:D→R` associa a cada `x∈D` um único valor `f(x)`. Domínio, regra e contradomínio pertencem à especificação; a imagem é `{f(x):x∈D}`. Em uma composição `(f∘g)(x)=f(g(x))`, é necessário ter `x∈Dom(g)` e `g(x)∈Dom(f)`.

Um modelo adiciona significado: variáveis, unidades, domínio físico e hipóteses. `P(t)=P_0e^(kt)` pode representar crescimento com taxa relativa constante, mas não uma população ilimitada por toda a eternidade.

### Exemplo resolvido 1 — domínio como contrato

Para `f(x)=sqrt((x-1)/(x+2))`, o radicando deve ser não negativo e `x≠-2`. O quadro de sinais nos pontos `-2` e `1` dá

`Dom(f)=(-∞,-2)∪[1,∞)`.

Cancelar ou reescrever uma expressão mais tarde não pode recolocar `-2` no domínio original.

### 1.2 Quatro problemas de passagem ao limite

O Cálculo nasce quando um processo finito é refinado indefinidamente:

1. **Taxa instantânea:** taxas médias são calculadas em intervalos cada vez menores.
2. **Área:** polígonos ou retângulos cada vez mais finos aproximam uma região curva.
3. **Extremo:** uma taxa de variação ajuda a localizar onde uma quantidade para de crescer.
4. **Soma infinita:** somas parciais finitas podem se aproximar de um valor.

Neste módulo, a meta é enxergar a operação de limite antes de formalizá-la.

### Exemplo resolvido 2 — taxa e máximo

Uma posição vertical é `s(t)=20t-5t²`, para `0≤t≤4`. A taxa média entre `t` e `t+h` é

`[s(t+h)-s(t)]/h = 20-10t-5h`.

Ao fazer `h→0`, surge a velocidade `v(t)=20-10t`. Ela zera em `t=2`; antes disso é positiva e depois negativa. Portanto a altura máxima ocorre em `t=2`, e vale `s(2)=20`. A conclusão usa sinal e domínio, não apenas a equação `v=0`.

### Exemplo resolvido 3 — área inicial

Sob `y=x` em `[0,1]`, use `n` retângulos de largura `1/n` e altura no extremo direito `i/n`. A soma é

`S_n=Σ_(i=1)^n (i/n)(1/n)=n(n+1)/(2n²)`.

Logo `S_n→1/2`. Ainda falta definir precisamente quando uma função tem integral, mas a área já aparece como limite de somas.

### 1.3 Três séries inaugurais

A série geométrica tem soma parcial

`1+r+...+r^n=(1-r^(n+1))/(1-r)`, para `r≠1`.

Se `|r|<1`, então `r^(n+1)→0` e

`Σ_(n=0)^∞r^n=1/(1-r)`.

A série harmônica `Σ1/n` diverge. Agrupando após o primeiro termo,

`1/2 +(1/3+1/4)+(1/5+...+1/8)+...`,

cada bloco depois do primeiro tem soma pelo menos `1/2`; as somas parciais crescem sem limite.

Já `Σ1/n²` converge. Agrupe `n=2^k,...,2^(k+1)-1`: há `2^k` termos, cada um no máximo `1/2^(2k)`, então o bloco é no máximo `1/2^k`. A soma é dominada por uma geométrica convergente.

Esses argumentos serão reconstruídos com critérios gerais nos módulos 10 e 11.

### Erros comuns

- Tratar o domínio como detalhe de implementação.
- Confundir muitos passos numéricos com uma passagem ao limite demonstrada.
- Concluir que `v(t)=0` sempre dá máximo.
- Atribuir uma soma a uma série sem definir e analisar suas somas parciais.

### Conexão com IA

Treinamento usa taxas locais; normalização de densidades usa integrais; arquiteturas iterativas e expansões usam séries. A conexão útil é estrutural: todos exigem controle do que ocorre quando cresce o número de passos ou diminui uma escala. Computação não elimina a pergunta de convergência.

### Checkpoint 1 — sem solução

1. Identifique a passagem ao limite em uma aproximação de `sqrt(2)` por bisseção.
2. Obtenha a soma de `Σ_(n=1)^∞3/4^n` a partir de somas parciais.
3. Modele a área de um retângulo de perímetro fixo e formule, sem regras prontas, como detectar seu máximo.

---

## Módulo 2 — Integral definida

### 2.1 Partições e somas de Darboux

Uma partição de `[a,b]` é um conjunto finito

`P={a=x_0<x_1<...<x_n=b}`.

Para uma função limitada `f`, sejam `m_i=inf f([x_(i-1),x_i])` e `M_i=sup f([x_(i-1),x_i])`. Definimos

`L(f,P)=Σm_iΔx_i`, `U(f,P)=ΣM_iΔx_i`.

Toda soma inferior é menor ou igual a toda soma superior. A integral inferior é o supremo das somas inferiores; a superior é o ínfimo das superiores. `f` é integrável à Riemann quando ambas coincidem. Um critério equivalente, útil em provas, diz:

> Uma função limitada é integrável em `[a,b]` se, para todo `ε>0`, existe uma partição `P` com `U(f,P)-L(f,P)<ε`.

### 2.2 Somas de Riemann

Escolha `ξ_i∈[x_(i-1),x_i]` e forme

`Σf(ξ_i)Δx_i`.

Quando essas somas tendem ao mesmo valor à medida que a malha `max Δx_i` tende a zero, temos a mesma integral. A formulação por Darboux enfatiza cotas; a formulação por Riemann enfatiza amostras.

### 2.3 Somas de potências

Em partições regulares, integrais polinomiais pedem fórmulas para `Σi^k`. As primeiras são

`Σ_(i=1)^n i=n(n+1)/2`,

`Σ_(i=1)^n i²=n(n+1)(2n+1)/6`.

Uma estratégia geral usa o telescópio

`Σ[(i+1)^(k+1)-i^(k+1)]=(n+1)^(k+1)-1`.

Expandir pelo binômio isola `Σi^k` em termos de somas de potências menores. Isso produz recursivamente a fórmula necessária, ainda que não seja a forma fechada mais elegante.

### Exemplo resolvido 1 — `∫_0^2x²dx`

Com extremos direitos, `Δx=2/n` e `x_i=2i/n`:

`S_n=Σ(2i/n)²(2/n)=8/n³ Σi²`

`=8n(n+1)(2n+1)/(6n³)`.

O limite é `8/3`. Como `x²` é crescente, as somas esquerdas e direitas são também inferior e superior; a diferença entre elas tende a zero, certificando integrabilidade.

### Exemplo resolvido 2 — função constante por partes

Se `f=2` em `[0,1)` e `f=5` em `[1,3]`, uma partição contendo `1` separa as regiões constantes. A integral é

`2·(1-0)+5·(3-1)=12`.

Mudar o valor em um único ponto não altera as somas no limite: apenas um retângulo pode ser afetado, e sua largura pode ser tornada arbitrariamente pequena.

### 2.4 Métodos numéricos

Regras dos retângulos, ponto médio e trapézios substituem a função por modelos simples em cada subintervalo. O resultado é aproximação e precisa vir com malha e, quando disponível, cota de erro. Um valor impresso com muitas casas não é automaticamente preciso.

### Erros comuns

- Esquecer `Δx` em uma soma.
- Usar máximo quando a soma pedida é inferior.
- Colocar `+C` em integral definida.
- Supor integrabilidade de qualquer função limitada sem critério.

### Conexão com IA

Discretizar uma integral se parece com aproximar uma esperança por amostras, mas quadratura e Monte Carlo têm mecanismos de erro distintos. Em ambos, resolução finita não garante que o objeto limite exista.

### Checkpoint 2 — sem solução

1. Escreva somas superior e inferior para `f(x)=x` em uma partição regular de `[1,3]`.
2. Use a identidade telescópica com cubos para recuperar `Σi²`.
3. Dê uma razão matemática para a regra do ponto médio tender a superar extremos laterais em funções suaves.

---

## Módulo 3 — Cálculo operacional

### 3.1 Derivada

Em um ponto `a` no qual entradas do domínio se aproximam por ambos os lados relevantes, definimos

`f'(a)=lim_(h→0)[f(a+h)-f(a)]/h`,

com `a+h` no domínio e `h≠0`. A formulação rigorosa relativa a domínios virá no módulo 5. A derivada mede inclinação, velocidade ou sensibilidade local.

Para `f(x)=x²`,

`[(a+h)²-a²]/h=2a+h→2a`.

Logo `f'(x)=2x`.

### 3.2 Regras

Para funções deriváveis:

- `(f+g)'=f'+g'`;
- `(fg)'=f'g+fg'`;
- `(f/g)'=(f'g-fg')/g²`, onde `g≠0`;
- `(f∘g)'(x)=f'(g(x))g'(x)`.

A regra de potência precisa de domínio:

- `(x^n)'=nx^(n-1)` para inteiro `n≥1` em `R`;
- para inteiro negativo, a fórmula vale onde `x≠0`;
- expoentes racionais exigem restringir-se aos intervalos em que a potência real está definida e é derivável;
- para expoente real arbitrário `α`, a definição geral `x^α=exp(αln x)` e a fórmula `αx^(α-1)` valem em `x>0`. Extensões a `x≤0` precisam ser analisadas caso a caso.

Usaremos provisoriamente as fórmulas

`(sin x)'=cos x`, `(cos x)'=-sin x`, `(e^x)'=e^x`, `(ln x)'=1/x`.

Sua fundamentação aparece nos módulos 9 e 12.

### Exemplo resolvido 1 — cadeia e produto

Para `F(x)=e^(-x²)(1+x³)`,

`F'(x)=(-2x)e^(-x²)(1+x³)+3x²e^(-x²)`.

Cada fator mantém seu papel; derivar produto não significa multiplicar derivadas.

### 3.3 Derivação implícita e inversas

Na curva `x²+y²=25`, `y` depende de `x`. Derivando:

`2x+2yy'=0`, então `y'=-x/y` onde `y≠0`.

Para uma inversa diferenciável, a relação provisória é

`(f^(-1))'(y)=1/f'(f^(-1)(y))`.

Invertibilidade sozinha não basta; continuidade, monotonicidade e derivada não nula serão tratadas no módulo 9.

### 3.4 Gráficos e extremos

Pontos críticos do domínio satisfazem `f'=0` ou não têm derivada. O sinal de `f'` determina crescimento; o de `f''`, concavidade. Em intervalo fechado, extremos absolutos são procurados entre pontos críticos e extremidades.

### Exemplo resolvido 2 — quadro de sinais

Para `f(x)=x³-3x`, `f'=3(x-1)(x+1)`. A função cresce em `(-∞,-1)` e `(1,∞)` e decresce em `(-1,1)`. Há máximo local em `-1` e mínimo local em `1`. Como `f''=6x`, a concavidade muda em `0`, que é ponto de inflexão.

### 3.5 Cinemática e otimização

Se `s(t)` é posição, `s'` é velocidade e `s''` é aceleração. Em otimização:

1. declare variáveis e domínio físico;
2. escreva objetivo e restrições;
3. reduza a uma variável;
4. encontre e compare candidatos;
5. interprete unidade e sinal.

### Exemplo resolvido 3 — retângulo

Com perímetro `20`, lados `x` e `10-x` têm área `A=10x-x²`, `0<x<10`. `A'=10-2x` zera em `5`; `A''=-2<0`. A área máxima é `25`, obtida pelo quadrado.

### 3.6 TFC e métodos, primeira passagem

O Teorema Fundamental conecta acumulação e derivada:

`d/dx ∫_a^x f(t)dt=f(x)` para `f` contínua,

e, se `F'=f`,

`∫_a^b f=F(b)-F(a)`.

Substituição reverte a cadeia; integração por partes reverte o produto:

`∫f(g(x))g'(x)dx=∫f(u)du`,

`∫u dv=uv-∫v du`.

### Exemplo resolvido 4 — duas técnicas

Com `u=1+x²`,

`∫x/(1+x²)dx=(1/2)ln(1+x²)+C`.

Com `u=x`, `dv=e^x dx`,

`∫xe^x dx=xe^x-e^x+C`.

Derivar as respostas é a conferência natural.

### 3.7 Aplicações da integral

Acumulação líquida de uma taxa `r` é `∫r`; área geométrica exige separar sinais. Entre `f≥g`, a área é `∫(f-g)`. Volumes por anéis usam `π∫(R²-r²)`; por cascas, `2π∫(raio)(altura)`.

### Erros comuns

- Usar a potência sem examinar domínio e expoente.
- Omitir derivada interna na cadeia.
- Procurar só `f'=0` e esquecer pontos não deriváveis e extremidades.
- Integrar uma taxa e esquecer a condição inicial.
- Misturar área líquida com área geométrica.

### Conexão com IA

Backpropagation organiza a regra da cadeia; diferenças finitas apenas aproximam derivadas. Otimizadores usam informação local e não ganham garantia global apenas porque o gradiente zerou.

### Checkpoint 3 — sem solução

1. Derive `ln(1+e^(x²))` usando as regras provisórias.
2. Modele uma taxa relacionada em um círculo cujo raio varia no tempo.
3. Monte por anéis e cascas o volume de uma região simples em torno de eixos diferentes.

---

## Módulo 4 — Números reais, sequências e completude

### 4.1 De naturais a racionais

Os axiomas de Peano descrevem `N` por um elemento inicial, operação sucessor, injetividade do sucessor, ausência de predecessor do inicial e princípio de indução. Eles não são uma lista de todos os naturais; são regras que caracterizam sua estrutura.

Inteiros podem ser construídos com pares `(a,b)∈N_0²`, interpretados como `a-b`, sob

`(a,b)~(c,d)` se `a+d=b+c`.

Racionais são classes de pares `(p,q)` de inteiros com `q≠0`, onde

`(p,q)~(r,s)` se `ps=rq`.

Operações são definidas em representantes e devem ser provadas independentes deles.

### 4.2 Irracionalidade e bases

Se `sqrt(2)=p/q` em forma irredutível, então `p²=2q²`, logo `p` é par. Escrevendo `p=2k`, obtemos `q²=2k²`, então `q` também é par, contradizendo a forma irredutível. Portanto `sqrt(2)∉Q`.

Em base `b≥2`, uma expansão posicional finita é soma de potências de `b`; uma expansão infinita é limite de truncamentos. Há representações duplas, como `0,999...=1`, porque a cauda geométrica vale `1`. Isso não significa dois números reais, apenas duas escritas para a mesma classe limite.

### 4.3 Limites de sequências

Uma sequência é uma função `a:N→R`. Dizemos `a_n→L` se, para todo `ε>0`, existe `N` tal que `n≥N` implica `|a_n-L|<ε`.

Exemplo: `1/n→0`. Dado `ε>0`, escolha `N>1/ε`; então `n≥N` implica `1/n≤1/N<ε`.

Uma sequência é de Cauchy se, para todo `ε>0`, existe `N` tal que `m,n≥N` implica `|a_m-a_n|<ε`. Toda sequência convergente é de Cauchy. Em `R`, toda Cauchy converge; em `Q`, isso falha, pois racionais podem aproximar `sqrt(2)` sem limite racional.

### 4.4 Reais como completação de `Q`

Considere sequências de Cauchy racionais. Identifique `(a_n)` e `(b_n)` quando `a_n-b_n→0`. Um real é uma classe de equivalência desse tipo. Soma e produto são definidos termo a termo e provados bem definidos. Racionais entram como sequências constantes.

Essa construção explica a completude: uma sequência de classes de Cauchy que é Cauchy pode ser diagonalizada para produzir uma classe limite. Em um primeiro curso, importa compreender o mecanismo e saber quais resultados usam completude, mesmo que detalhes técnicos sejam delegados a um texto de Análise.

### 4.5 Supremo

Um corpo ordenado completo satisfaz:

> Todo subconjunto não vazio de `R` limitado superiormente possui supremo em `R`.

`s=sup A` significa: `s` é cota superior e nenhuma quantidade menor é cota superior. Equivalentemente, para todo `ε>0`, existe `a∈A` com `s-ε<a≤s`.

### Exemplo resolvido 1 — construindo `sqrt(3)`

Tome `A={x≥0:x²<3}`. O conjunto contém `1` e é limitado, por exemplo, por `2`. Seja `s=sup A`. Se `s²<3`, um incremento pequeno manteria o quadrado abaixo de `3`, contrariando a supremacia. Se `s²>3`, um decremento pequeno ainda seria cota superior, outra contradição. Logo `s²=3`.

As escolhas “pequenas” podem ser tornadas explícitas usando

`(s+h)²-s²=h(2s+h)`.

### 4.6 Formas equivalentes de completude

- **Convergência monótona:** sequência crescente e limitada converge ao supremo de seus valores.
- **Cauchy:** toda sequência de Cauchy real converge.
- **Bolzano-Weierstrass:** toda sequência limitada tem subsequência convergente.
- **Intervalos encaixantes:** intervalos fechados não vazios `I_(n+1)⊆I_n`, com comprimentos tendendo a zero, têm exatamente um ponto comum.

Esboço de Bolzano-Weierstrass: bissete um intervalo que contém toda a sequência; escolha a metade que contém infinitos termos e repita. Os intervalos encaixantes determinam um ponto, e escolhendo índices crescentes dentro deles obtemos uma subsequência convergente.

Esses enunciados não são meros sinônimos; demonstra-se que cada um implica os demais usando a ordem de `R`.

### Erros comuns

- Dizer que um conjunto possui supremo porque “parece fechado”.
- Confundir supremo com máximo: o supremo pode não pertencer ao conjunto.
- Supor que Cauchy sempre converge sem especificar o espaço.
- Tratar uma expansão decimal como definição independente de limite.

### Conexão com IA

Algoritmos iterativos produzem sequências. Mostrar que passos ficam próximos entre si não basta em qualquer espaço; a completude do ambiente importa. Em espaços de parâmetros finito-dimensionais usuais, herdamos a completude real, mas ainda precisamos provar que a sequência é Cauchy ou tem uma subsequência adequada.

### Checkpoint 4 — sem solução

1. Mostre que `a_n=2-1/n` é crescente, limitada e converge ao supremo de sua imagem.
2. Construa uma sequência racional de Cauchy que aproxima `sqrt(2)`.
3. Explique por que Bolzano-Weierstrass garante subsequência, não convergência da sequência inteira.

---

## Módulo 5 — Limites e continuidade rigorosos

### 5.1 Ponto de acumulação e limite relativo ao domínio

Seja `f:D→R`. Um ponto `a∈R` é **ponto de acumulação de `D`** quando toda vizinhança perfurada de `a` contém algum ponto de `D`. Não é necessário que `a∈D`.

Somente nessa situação definimos de modo não vacuamente informativo:

> `lim_(x→a,x∈D)f(x)=L` se, para todo `ε>0`, existe `δ>0` tal que, para todo `x∈D`,
>
> `0<|x-a|<δ` implica `|f(x)-L|<ε`.

As expressões “`x∈D`” e “`a` é ponto de acumulação” fazem parte da definição. Sem elas, poderíamos testar pontos onde a função nem existe ou aceitar qualquer `L` por vacuidade.

### Exemplo resolvido 1 — domínio discreto com acumulação

Se `D={0}∪{1/n:n∈N}` e `f(x)=x`, então `0` é ponto de acumulação. Dado `ε>0`, tome `δ=ε`. Para `x∈D`, se `0<|x|<δ`, então `|f(x)-0|=|x|<ε`. Logo o limite relativo a `D` é zero.

Cada `1/n` é isolado em `D`, portanto não é ponto de acumulação de `D` por pontos diferentes dele.

### 5.2 Critério sequencial

`lim_(x→a,x∈D)f(x)=L` se, e somente se, para toda sequência `(x_n)` em `D\{a}` com `x_n→a`, vale `f(x_n)→L`.

Para negar um limite, basta encontrar uma sequência que viole a conclusão; duas sequências com imagens tendendo a valores distintos são uma forma frequente.

### 5.3 Operações e confronto

Limites finitos preservam soma e produto; o quociente é preservado se o limite do denominador não é zero. O Teorema do Confronto afirma que, se `g≤f≤h` perto de `a` no domínio e ambos os extremos tendem a `L`, então `f→L`.

Um ingrediente para a regra do produto é que uma função com limite finito é limitada em alguma vizinhança perfurada. Assim,

`fg-LM=f(g-M)+M(f-L)`

pode ser controlado por duas parcelas.

### Exemplo resolvido 2 — prova `ε-δ`

Para provar `lim_(x→2)x²=4`, note

`|x²-4|=|x-2||x+2|`.

Restrinja `δ≤1`. Então `|x-2|<1` implica `1<x<3`, logo `|x+2|<5`. Escolha

`δ=min{1,ε/5}`.

Segue `|x²-4|<5δ≤ε`.

### 5.4 Limites laterais e infinitos

Limites à direita e à esquerda restringem `D` a `x>a` ou `x<a`. Um limite bilateral existe quando ambos existem e coincidem.

`lim_(x→a+)f(x)=+∞` significa: para todo `M>0`, existe `δ>0` tal que `x∈D` e `0<x-a<δ` implicam `f(x)>M`. Há definições análogas para `-∞`, lado esquerdo e infinito no domínio.

### 5.5 Continuidade e descontinuidades

`f:D→R` é contínua em `a∈D` se, para todo `ε>0`, existe `δ>0` tal que `x∈D` e `|x-a|<δ` implicam `|f(x)-f(a)|<ε`. Se `a` é ponto de acumulação, isso equivale a `lim_(x→a,x∈D)f(x)=f(a)`. Pontos isolados do domínio são contínuos pela definição relativa.

Classificações usuais, sempre relativas ao domínio e aos lados disponíveis:

- **removível:** existe limite bilateral finito, mas o valor falta ou difere dele;
- **salto:** os limites laterais finitos existem e são diferentes;
- **infinita:** ao menos um limite lateral relevante é `+∞` ou `-∞`; não basta dizer vagamente que a função “cresce”;
- **oscilatória ou de segunda espécie:** algum limite lateral não existe por oscilação sem valor limite, e não por simples divergência a `±∞`.

### 5.6 Regras de continuidade e derivação

Soma, produto, quociente com denominador não nulo e composição preservam continuidade. A prova da composição traduz primeiro a tolerância na saída de `f` em tolerância na entrada de `f`, depois usa continuidade de `g`.

As regras de derivação decorrem de manipulações do quociente diferencial mais regras de limites. Para o produto:

`[f(a+h)g(a+h)-f(a)g(a)]/h`

é separado adicionando e subtraindo `f(a+h)g(a)`. A continuidade implicada pela derivabilidade permite passar ao limite. A cadeia exige um cuidado adicional quando o incremento interno zera; uma formulação com função-erro resolve o caso sem divisão ilegítima.

### Erros comuns

- Definir limite em ponto que não é de acumulação sem notar a vacuidade.
- Esquecer que `x` deve pertencer ao domínio.
- Chamar `1/x²` de “salto infinito”; seus limites laterais são infinitos.
- Provar continuidade em `a` sem exigir `a∈D`.
- Dividir por um incremento que pode ser zero na prova da cadeia.

### Conexão com IA

Continuidade é estabilidade local relativa ao conjunto de entradas admissíveis. Dados vivem muitas vezes em subconjuntos do espaço ambiente; perturbações fora desse domínio podem não ter significado. A distinção entre limite relativo e ambiente evita testar robustez contra entradas impossíveis.

### Checkpoint 5 — sem solução

1. Determine os pontos de acumulação de `{1/n:n∈N}`.
2. Negue formalmente, com quantificadores, a afirmação `lim_(x→a)f(x)=L`.
3. Classifique a descontinuidade de `tan x` em `π/2` usando limites laterais com sinais.

---

## Módulo 6 — Teoremas de continuidade e integrabilidade

### 6.1 Valor intermediário e máximo

> **TVI:** se `f` é contínua em `[a,b]` e `N` está entre `f(a)` e `f(b)`, existe `c∈[a,b]` com `f(c)=N`.

Uma prova usa completude. Para `f(a)<N<f(b)`, considere os pontos até os quais `f` ainda fica abaixo de `N`, tome um supremo e use continuidade para excluir valores estritamente abaixo ou acima de `N` no ponto limite.

> **Teorema dos Valores Extremos:** se `f` é contínua em `[a,b]`, atinge máximo e mínimo.

Pelo critério sequencial, uma sequência de valores que se aproxima do supremo tem entradas em `[a,b]`; Bolzano-Weierstrass fornece subsequência convergente, e continuidade leva o limite ao valor máximo.

### Exemplo resolvido 1 — existência e unicidade

Para `p(x)=x³+x-1`, `p(0)=-1` e `p(1)=1`. Continuidade e TVI dão uma raiz em `(0,1)`. Como `p'(x)=3x²+1>0`, a função é estritamente crescente, então a raiz é única. TVI sozinho não dá unicidade.

### 6.2 Continuidade uniforme

Continuidade pontual permite que `δ` dependa de `a` e de `ε`. Continuidade uniforme exige:

> Para todo `ε>0`, existe `δ>0` tal que, para quaisquer `x,y∈D`, `|x-y|<δ` implica `|f(x)-f(y)|<ε`.

O mesmo `δ` funciona em todo o domínio.

`f(x)=1/x` é contínua em `(0,1)`, mas não uniformemente. Tome `x_n=1/n` e `y_n=1/(n+1)`: a distância das entradas tende a zero, enquanto a diferença das saídas vale `1`.

### 6.3 Heine-Cantor

> Toda função contínua em um intervalo fechado e limitado é uniformemente contínua.

Prova por contradição: se não fosse uniforme, haveria `ε_0>0` e pares `x_n,y_n` cada vez mais próximos com saídas separadas por ao menos `ε_0`. Bolzano-Weierstrass fornece subsequência `x_(n_k)→c`; como `|x_(n_k)-y_(n_k)|→0`, também `y_(n_k)→c`. Continuidade em `c` força as duas imagens a se aproximarem, contradição.

### 6.4 Contínua em compacto implica integrável

Se `f` é contínua em `[a,b]`, Heine-Cantor fornece, para qualquer `η>0`, uma escala `δ` tal que a oscilação de `f` em pontos distantes menos que `δ` seja menor que `η`. Escolha uma partição com malha menor que `δ`. Em cada subintervalo, `M_i-m_i≤η`. Portanto

`U(f,P)-L(f,P)=Σ(M_i-m_i)Δx_i≤η(b-a)`.

Dado `ε>0`, tome `η=ε/(b-a)` (com `a<b`). O critério de Darboux dá integrabilidade. Esta prova mostra a cadeia:

`completude → compactação sequencial → uniformidade → integrabilidade`.

### Exemplo resolvido 2 — controle uniforme explícito

Para `f(x)=x²` em `[0,3]`,

`|x²-y²|=|x-y||x+y|≤6|x-y|`.

Escolher `δ=ε/6` prova continuidade uniforme. O controle global `|x+y|≤6` seria impossível em todo `R`, embora `x²` seja contínua lá.

### Erros comuns

- Aplicar TVI sem intervalo fechado ou continuidade.
- Concluir unicidade pelo TVI.
- Trocar a ordem dos quantificadores na continuidade uniforme.
- Afirmar que toda função contínua em qualquer domínio é uniforme.
- Usar TFC para provar integrabilidade quando a integrabilidade é hipótese anterior do desenvolvimento.

### Conexão com IA

Uniformidade fornece uma escala de perturbação válida em todo um conjunto, mais próxima de uma garantia global de robustez que continuidade ponto a ponto. Em conjuntos compactos, continuidade transforma-se nessa garantia uniforme.

### Checkpoint 6 — sem solução

1. Prove que `sqrt(x)` é uniformemente contínua em `[0,∞)` ou encontre a dificuldade em usar apenas derivada limitada.
2. Dê uma função contínua em intervalo aberto que não atinja máximo.
3. Reconstitua a prova de integrabilidade escolhendo explicitamente `η` a partir de `ε`.

---

## Módulo 7 — TVM, l'Hôpital e Taylor

### 7.1 Rolle e Teorema do Valor Médio

> **Rolle:** se `f` é contínua em `[a,b]`, derivável em `(a,b)` e `f(a)=f(b)`, existe `c∈(a,b)` com `f'(c)=0`.

> **TVM:** se `f` é contínua em `[a,b]` e derivável em `(a,b)`, existe `c∈(a,b)` tal que
>
> `f'(c)=[f(b)-f(a)]/(b-a)`.

O TVM segue de Rolle ao subtrair de `f` a reta secante. Consequências: se `f'=0` num intervalo, `f` é constante; se `f'>0`, é estritamente crescente; se `|f'|≤M`, então `|f(x)-f(y)|≤M|x-y|`.

### Exemplo resolvido 1

Para `f(x)=sqrt(x)` em `[1,4]`, a inclinação secante é `1/3`. Como `f'(x)=1/(2sqrt(x))`, o ponto garantido satisfaz `1/(2sqrt(c))=1/3`, logo `c=9/4`.

### 7.2 Regra de l'Hôpital com hipóteses

Uma versão lateral finita é:

> Se `f` e `g` são deriváveis numa vizinhança perfurada unilateral de `a`; `g(x)≠0` e `g'(x)≠0` nessa vizinhança; `f(x),g(x)→0` ou ambos têm módulo tendendo a infinito no lado considerado; e `f'(x)/g'(x)→L` nesse lado, com `L` finito ou infinito, então `f(x)/g(x)→L`.

Há versões à esquerda, à direita, bilaterais e para `x→±∞`. A derivabilidade não precisa valer no próprio `a`, mas deve valer na vizinhança perfurada adequada. O denominador original e sua derivada precisam permitir os quocientes onde o teorema é aplicado.

A regra trata `0/0` e `∞/∞`. Formas `0·∞`, `∞-∞`, `1^∞`, `0^0` e `∞^0` precisam ser reescritas.

### Exemplo resolvido 2

Para `x→0`, `(e^x-1-x)/x²` é `0/0`. As funções são deriváveis perto de zero, e `2x≠0` na vizinhança perfurada. Uma aplicação dá

`(e^x-1)/(2x)`, ainda `0/0`. Na segunda, a derivada do novo denominador é `2≠0`, e o limite vira `e^x/2→1/2`.

Reverificar a forma antes da segunda aplicação não é burocracia; é parte do teorema.

### 7.3 Polinômio de Taylor

Se `f` tem derivadas suficientes perto de `a`, o polinômio de Taylor de grau `n` é

`T_n(x)=Σ_(k=0)^n f^(k)(a)(x-a)^k/k!`.

Sob as hipóteses do teorema de Taylor, existe `ξ` entre `a` e `x` tal que o resto é

`R_n(x)=f^(n+1)(ξ)(x-a)^(n+1)/(n+1)!`.

Isso transforma aproximação local em estimativa de erro.

### Exemplo resolvido 3 — exponencial

Para `e^x` em `a=0`,

`T_3(x)=1+x+x²/2+x³/6`.

Em `|x|≤0,1`, `|e^ξ|≤e^0,1`, então

`|R_3(x)|≤e^0,1|x|^4/24`.

A cota pode não ser o erro exato, mas é uma garantia.

### 7.4 Método de Newton

Linearizar `f` em `x_n` e zerar a reta dá

`x_(n+1)=x_n-f(x_n)/f'(x_n)`.

Taylor explica a convergência rápida perto de raiz simples sob regularidade; longe dela, o método pode divergir ou cair onde `f'=0`.

### Erros comuns

- Usar TVM sem continuidade nas extremidades.
- Aplicar l'Hôpital a um quociente que não tem forma adequada.
- Derivar numerador e denominador sem verificar `g'≠0`.
- Tratar Taylor como identidade global sem controlar o resto.
- Supor convergência de Newton para qualquer chute.

### Conexão com IA

O TVM converte cota de gradiente em cota de variação. Taylor fundamenta aproximações quadráticas e análise local de otimizadores. A garantia depende de região e resto; um modelo local não descreve automaticamente uma paisagem inteira.

### Checkpoint 7 — sem solução

1. Use o TVM para provar uma cota para `|ln x-ln y|` em `[1,2]`.
2. Escreva todas as hipóteses para aplicar l'Hôpital a um limite lateral.
3. Determine o Taylor de grau 4 de `cos x` em zero com cota de resto em `[-1/2,1/2]`.

---

## Módulo 8 — TFC, técnicas e aplicações

### 8.1 Os dois teoremas fundamentais

> Se `f` é contínua e `A(x)=∫_a^x f(t)dt`, então `A'(x)=f(x)`.

A prova compara `[A(x+h)-A(x)]/h` com valores mínimo e máximo de `f` no pequeno intervalo e usa continuidade.

> Se `F'=f` em `[a,b]`, então `∫_a^b f(x)dx=F(b)-F(a)`.

A segunda parte pode ser provada comparando somas de Riemann com incrementos de `F` via TVM.

### Exemplo resolvido 1 — limites variáveis

Se `G(x)=∫_(x²)^(sin x)e^(t²)dt`, então

`G'(x)=e^(sin²x)cos x-e^(x^4)2x`.

Não é necessário integrar `e^(t²)`.

### 8.2 Variação líquida

Se `Q'=r`, então `Q(b)-Q(a)=∫_a^b r`. Para velocidade, isso é deslocamento; distância integra `|v|`. Para vazão líquida, o sinal registra entrada menos saída.

### 8.3 Técnicas

- **Substituição:** reconhece `f(g(x))g'(x)`.
- **Partes:** `∫u dv=uv-∫v du`.
- **Frações parciais:** decompõe função racional própria após fatorar o denominador.
- **Identidades/substituições trigonométricas:** tratam potências e raízes quadráticas.
- **Integral imprópria:** substitui infinito ou singularidade por limite; cada singularidade interna exige limite separado.

### Exemplo resolvido 2 — partes

`∫x ln x dx`, `x>0`. Tome `u=ln x`, `dv=x dx`. Então

`=x²ln x/2-∫x/2 dx`

`=x²ln x/2-x²/4+C`.

### Exemplo resolvido 3 — frações parciais

`1/[(x-1)(x+2)]=(1/3)/(x-1)-(1/3)/(x+2)`.

Logo, em intervalos sem os polos,

`∫dx/[(x-1)(x+2)]=(1/3)ln|x-1|-(1/3)ln|x+2|+C`.

### Exemplo resolvido 4 — imprópria

`∫_1^∞x^(-2)dx=lim_(b→∞)[-1/x]_1^b=1`.

A antiderivada formal só ganha significado depois da existência do limite.

### 8.4 Áreas, volumes e valor médio

Se `f≥g`, área é `∫(f-g)`. Discos e anéis usam quadrados dos raios; cascas usam circunferência, altura e espessura. O valor médio de `f` em `[a,b]` é

`f_med=(1/(b-a))∫_a^b f`.

### Exemplo resolvido 5 — área

Entre `y=x` e `y=x²`, as interseções são `0` e `1`, e `x≥x²` nesse intervalo. A área é

`∫_0^1(x-x²)dx=1/6`.

### Erros comuns

- Acrescentar `+C` a integral definida.
- Misturar limites em `x` depois de substituir por `u`.
- Integrar através de singularidade sem separar limites.
- Produzir área negativa por inverter curva superior e inferior.

### Conexão com IA

Integrais normalizam densidades e calculam esperanças. Muitas não têm antiderivada elementar; quadratura e amostragem aproximam, mas a formulação e a convergência continuam matemáticas.

### Checkpoint 8 — sem solução

1. Derive uma integral com os dois limites dependendo de `x`.
2. Escolha técnicas para três integrais de estruturas diferentes e justifique sem calcular.
3. Formule por cascas um volume em torno de uma reta que não seja eixo coordenado.

---

## Módulo 9 — Inversas, logaritmo e exponencial

### 9.1 Teorema da inversa em uma variável

> Se `f` é contínua e estritamente monótona em um intervalo `I`, então `f(I)` é intervalo e `f^(-1):f(I)→I` é contínua e estritamente monótona.

> Se, além disso, `f` é derivável em `x_0∈I`, `f'(x_0)≠0` e `y_0=f(x_0)`, então `f^(-1)` é derivável em `y_0` e
>
> `(f^(-1))'(y_0)=1/f'(x_0)`.

Mera bijetividade não garante continuidade da inversa em domínios arbitrários; mera derivabilidade não basta quando `f'(x_0)=0`. Para `f(x)=x³`, a inversa é contínua, mas sua derivada real finita não existe em zero.

### Exemplo resolvido 1

`f(x)=x+x³` tem `f'=1+3x²>0`, é contínua e cresce de `-∞` a `∞`; logo tem inversa contínua em `R`. Como `f(1)=2`,

`(f^(-1))'(2)=1/f'(1)=1/4`.

### 9.2 Construção do logaritmo

Para `x>0`, defina

`ln x=∫_1^x dt/t`.

Pelo TFC, `(ln x)'=1/x`; portanto `ln` é estritamente crescente. Com a substituição `t=au`,

`ln(ab)=∫_1^(ab)dt/t=∫_1^a dt/t+∫_a^(ab)dt/t`

`=ln a+∫_1^b du/u=ln a+ln b`.

Disso seguem `ln(1/x)=-ln x` e `ln(x^n)=nln x` para inteiros. Pode-se provar que `ln x→∞` quando `x→∞`, por exemplo comparando incrementos em potências de `2`; por simetria, tende a `-∞` em `0+`. Logo sua imagem é `R`.

### 9.3 Construção da exponencial

Defina `exp:R→(0,∞)` como a inversa de `ln`. Pelo teorema da inversa,

`exp'(x)=1/[ln'(exp x)]=exp x`.

Como `ln(ab)=ln a+ln b`, a injetividade de `ln` dá

`exp(x+y)=exp x exp y`.

Definimos `e=exp(1)` e `e^x=exp x`.

### 9.4 Potências reais

Para `x>0` e `α∈R`, defina

`x^α=exp(αln x)`.

Pela cadeia,

`d/dx x^α=exp(αln x)·α/x=αx^(α-1)`.

Esta é a regra geral no semieixo positivo. Para expoentes inteiros ela se estende aos domínios algébricos usuais; para racionais com denominador ímpar pode haver extensão a negativos, mas derivabilidade em zero deve ser examinada separadamente.

### Exemplo resolvido 2 — equação de crescimento

Se `y'=ky` e `y(0)=y_0`, a função `y=y_0exp(kt)` satisfaz ambas. Para `y_0>0`, também se pode separar `y'/y=k`, integrar e usar `ln y=kt+C`. Se `k>0`, o tempo de duplicação resolve `exp(kT)=2`, então `T=ln2/k`.

### Erros comuns

- Invocar a fórmula da inversa sem monotonicidade/continuidade e sem `f'≠0`.
- Usar propriedades de `ln` como premissas quando elas deveriam ser deduzidas da integral.
- Definir `x^α` para `x<0` e `α` real arbitrário.
- Confundir `f^(-1)` com `1/f`.

### Conexão com IA

Log-sum-exp e log-verossimilhança usam propriedades que agora foram construídas, não apenas memorizadas. Transformações invertíveis precisam de derivadas não nulas para jacobianos locais bem comportados.

### Checkpoint 9 — sem solução

1. Prove `ln(x/y)=ln x-ln y` a partir da propriedade do produto.
2. Explique por que `exp` é convexa usando derivadas.
3. Analise a regra de potência para `x^(2/3)` em zero e em valores negativos.

---

## Módulo 10 — Sequências e séries numéricas

### 10.1 Sequências

Além da definição `ε-N`, usamos:

- toda sequência convergente é limitada;
- limites preservam operações válidas;
- sequência monótona e limitada converge por completude;
- toda sequência limitada tem subsequência convergente por Bolzano-Weierstrass;
- em `R`, Cauchy equivale a convergência.

### Exemplo resolvido 1 — recorrência

Se `a_1=1` e `a_(n+1)=sqrt(2+a_n)`, prove por indução `1≤a_n≤2`. A função `sqrt(2+x)` é crescente, e `a_2>a_1`; indução mostra monotonicidade. Logo há limite `L∈[1,2]`. Passando ao limite,

`L=sqrt(2+L)`, então `L²-L-2=0`. O intervalo seleciona `L=2`.

Resolver a equação sem antes provar convergência não seria válido.

### 10.2 Séries e critério de Cauchy

Uma série `Σa_n` converge quando `s_N=Σ_(n=1)^N a_n` converge. Necessariamente `a_n→0`, mas isso não é suficiente, como mostra a harmônica.

Critério de Cauchy:

> `Σa_n` converge se, e somente se, para todo `ε>0` existe `N` tal que `m>n≥N` implica `|a_(n+1)+...+a_m|<ε`.

### 10.3 Séries básicas

- geométrica `Σr^n`: converge para `|r|<1`;
- `p`-série `Σ1/n^p`: converge se, e somente se, `p>1`;
- harmônica é o caso divergente `p=1`.

O teste da integral compara soma e área para função positiva decrescente. Para `f(x)=x^(-p)`, a integral imprópria converge exatamente quando `p>1`.

### 10.4 Comparação

Se `0≤a_n≤b_n` eventualmente e `Σb_n` converge, então `Σa_n` converge. Se `a_n≥b_n≥0` e `Σb_n` diverge, `Σa_n` diverge.

No teste da comparação pelo limite, se `a_n,b_n>0` e `a_n/b_n→c` com `0<c<∞`, as séries têm o mesmo comportamento.

### Exemplo resolvido 2

Para `Σ1/(n²+1)`, temos `0<1/(n²+1)≤1/n²`, logo converge. Para `Σ1/sqrt(n²+1)`,

`[1/sqrt(n²+1)]/(1/n)=n/sqrt(n²+1)→1`,

então diverge como a harmônica.

### 10.5 Razão e raiz

Para termos não negativos ou valores absolutos, se

`lim |a_(n+1)/a_n|=L`

ou `lim root(n)(|a_n|)=L`, então a série converge se `L<1` e diverge se `L>1`. Para `L=1`, o teste é inconclusivo.

### Exemplo resolvido 3

Em `Σn/3^n`,

`a_(n+1)/a_n=((n+1)/n)/3→1/3`,

portanto converge. O mesmo teste aplicado a `Σ1/n²` produz limite `1` e nada conclui, embora a série converja.

### Erros comuns

- Passar ao limite em recorrência antes de provar que ele existe.
- Concluir convergência apenas de `a_n→0`.
- Inverter o sentido útil de uma comparação.
- Declarar divergência quando razão ou raiz dá `1`.

### Conexão com IA

Séries aparecem em aproximações e em análises de erro acumulado. Um erro por etapa tender a zero não garante erro total finito; é a série dos erros que precisa de controle.

### Checkpoint 10 — sem solução

1. Analise uma sequência recursiva por monotonicidade e limitação.
2. Use o critério de Cauchy para explicar a divergência harmônica.
3. Escolha, sem executar, o teste mais informativo para quatro séries de formas distintas.

---

## Módulo 11 — Convergência absoluta, rearranjos e séries de potências

### 11.1 Absoluta e condicional

`Σa_n` converge absolutamente se `Σ|a_n|` converge. Convergência absoluta implica convergência: pelo critério de Cauchy,

`|Σ_(k=n+1)^m a_k|≤Σ_(k=n+1)^m|a_k|`.

Se `Σa_n` converge mas `Σ|a_n|` diverge, a convergência é condicional.

### 11.2 Séries alternadas

> Se `b_n≥0`, `b_(n+1)≤b_n` e `b_n→0`, então `Σ(-1)^(n-1)b_n` converge.

As somas parciais pares e ímpares comprimem o limite por lados opostos. O erro após `N` termos tem módulo no máximo `b_(N+1)`.

Assim, `Σ(-1)^(n-1)/n` converge condicionalmente; a série dos módulos é harmônica. Já `Σ(-1)^(n-1)/n²` converge absolutamente.

### 11.3 Rearranjos

Reordenar uma soma finita não muda nada. Para séries:

- rearranjos de série absolutamente convergente convergem para a mesma soma;
- pelo teorema de rearranjo de Riemann, os termos de uma série real condicionalmente convergente podem ser rearranjados para convergir a qualquer real prescrito ou para divergir.

A ideia é acumular termos positivos até ultrapassar o alvo, depois negativos até ficar abaixo, repetindo. Como os termos tendem a zero, as ultrapassagens encolhem.

### 11.4 Séries de potências

Uma série de potências centrada em `a` é

`Σc_n(x-a)^n`.

Existe um raio `R∈[0,∞]` tal que ela converge absolutamente para `|x-a|<R` e diverge para `|x-a|>R`. Nas extremidades, cada ponto precisa de análise própria.

Quando existe,

`1/R=limsup root(n)(|c_n|)`.

Se a razão `|c_n/c_(n+1)|` tem limite, ela frequentemente fornece `R`.

### Exemplo resolvido 1 — raio e bordas

Para

`Σ_(n=1)^∞ (x-1)^n/(n2^n)`,

o teste da razão dá `|x-1|/2`, então `R=2`. Em `x=3`, resulta `Σ1/n`, divergente. Em `x=-1`, resulta `Σ(-1)^n/n`, convergente condicional. O intervalo é `[-1,3)`.

Dentro do raio, a série pode ser derivada formalmente para

`Σ_(n=1)^∞(x-1)^(n-1)/2^n`,

mas a justificativa uniforme vem no próximo módulo.

### Erros comuns

- Chamar toda série alternada de convergente sem monotonicidade e termo nulo.
- Confundir condicional com divergente.
- Reordenar série condicional como se fosse soma finita.
- Incluir extremidades automaticamente no intervalo de uma série de potências.

### Conexão com IA

Somar gradientes, perdas ou atualizações em ordens diferentes pode interagir com arredondamento mesmo em somas finitas. O fenômeno matemático de rearranjos condicionais é mais profundo: sem convergência absoluta, a própria soma infinita depende da ordem.

### Checkpoint 11 — sem solução

1. Obtenha uma cota de erro para uma série alternada.
2. Explique por que partes positiva e negativa de uma série condicional têm somas infinitas.
3. Determine raio e teste duas extremidades de uma série de potências inédita.

---

## Módulo 12 — Convergência uniforme e construção das trigonométricas

### 12.1 Pontual versus uniforme

`f_n→f` pontualmente em `D` quando, para cada `x` e `ε`, o índice necessário pode depender de `x`. A convergência é uniforme quando

`sup_(x∈D)|f_n(x)-f(x)|→0`.

Em `[0,1]`, `f_n(x)=x^n` converge pontualmente para a função que vale `0` em `[0,1)` e `1` em `1`. O limite é descontínuo, logo a convergência não pode ser uniforme, pois limite uniforme de funções contínuas é contínuo.

### 12.2 Teste `M` de Weierstrass

Se `|f_n(x)|≤M_n` para todo `x∈D` e `ΣM_n` converge, então `Σf_n` converge uniforme e absolutamente em `D`. O critério de Cauchy uniforme segue da comparação das caudas.

Convergência uniforme autoriza, sob hipóteses usuais:

- preservar continuidade;
- trocar limite e integral em intervalo compacto;
- controlar o erro por uma única cauda em todo o domínio.

Ela não autoriza automaticamente trocar limite e derivada. Para isso, um teorema típico exige convergência das derivadas uniformemente e convergência da série original em ao menos um ponto.

### 12.3 Diferenciação de séries de potências

Uma série de potências converge uniformemente em todo intervalo fechado `|x-a|≤r<R`. Dentro do raio, pode ser derivada e integrada termo a termo; as séries derivada e integral têm o mesmo raio. Nada disso decide automaticamente as extremidades.

### Exemplo resolvido 1 — série geométrica como função

Para `|x|<1`,

`Σ_(n=0)^∞x^n=1/(1-x)`.

Em `[-r,r]`, `r<1`, o teste `M` usa `|x^n|≤r^n`, dando convergência uniforme. Derivando no interior,

`Σ_(n=1)^∞n x^(n-1)=1/(1-x)²`.

Não há convergência uniforme em todo `(-1,1)`: se houvesse, a função limite `1/(1-x)` estaria, a partir de algum índice, uniformemente próxima de uma soma parcial polinomial limitada nesse intervalo e seria limitada, o que é falso quando `x→1-`.

### 12.4 Construção de seno e cosseno

Defina, sem apelar inicialmente à geometria,

`S(x)=Σ_(n=0)^∞(-1)^n x^(2n+1)/(2n+1)!`,

`C(x)=Σ_(n=0)^∞(-1)^n x^(2n)/(2n)!`.

O teste da razão dá raio infinito. Em todo intervalo compacto, a convergência é uniforme e podemos derivar termo a termo:

`S'=C`, `C'=-S`, `S(0)=0`, `C(0)=1`.

Então

`d/dx[S(x)²+C(x)²]=2SS'+2CC'=2SC-2CS=0`.

Como o valor em zero é `1`, segue

`S(x)²+C(x)²=1`.

As funções assim construídas são o seno e o cosseno. Paridade vem das potências: `S` é ímpar e `C` é par. Fórmulas de adição podem ser obtidas mostrando que, para `y` fixo, ambos os lados resolvem o mesmo sistema diferencial com os mesmos valores iniciais.

Para conectar à periodicidade, demonstra-se que `C` possui um primeiro zero positivo `α`; define-se `π=2α`. As fórmulas de adição então produzem periodicidade e a interpretação geométrica usual. A prova completa da existência do primeiro zero exige estimativas das séries e continuidade; o ponto importante aqui é que trigonometria pode ser construída a partir de completude, séries e diferenciação, em vez de assumida.

### Exemplo resolvido 2 — aproximação certificada

Para aproximar `sin(0,2)`, use

`S_1=0,2-(0,2)³/6`.

Como os termos seguintes alternam e diminuem em módulo, o erro é no máximo `(0,2)^5/120`. Temos simultaneamente um algoritmo e uma garantia.

### Erros comuns

- Confundir convergência em cada ponto com uma taxa uniforme em todos os pontos.
- Trocar derivada e série apenas porque cada termo é derivável.
- Usar o raio para decidir extremidades.
- Definir seno pela série e depois usar propriedades geométricas não deduzidas como prova da própria construção.

### Conexão com IA

Aproximações polinomiais de ativações precisam de erro uniforme na região operacional, não apenas boa aproximação em amostras. O teste `M` e cotas de cauda fornecem garantias independentes dos pontos testados.

### Checkpoint 12 — sem solução

1. Mostre que `Σx^n/n²` converge uniformemente em `[0,1]`.
2. Dê uma sequência de funções deriváveis que converge uniformemente, mas cujas derivadas não convergem para a derivada do limite.
3. Deduza a paridade de `S` e `C` diretamente das séries.

---

## Mapa de dependências

O percurso completo é:

`problemas → limites intuitivos → operação diferencial/integral → completude de R → limites rigorosos → continuidade uniforme e integrabilidade → TVM/Taylor → TFC → inversas e ln/exp → séries → uniformidade → trigonometria`.

Antes de aceitar uma solução, pergunte:

1. O objeto está definido no domínio declarado?
2. Qual passagem ao limite está sendo feita?
3. Que forma de completude ou convergência a autoriza?
4. As hipóteses do teorema estão verificadas?
5. O resultado tem sinal, unidade e escala plausíveis?

Prossiga pelas [listas na ordem indicada](./EXERCICIOS.md). As avaliações são [P1](./avaliacoes/P1.md), [P2](./avaliacoes/P2.md) e [PF](./avaliacoes/PF.md).
