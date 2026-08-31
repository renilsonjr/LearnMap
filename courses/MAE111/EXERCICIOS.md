# Listas de Exercícios — MAE111

## Persona acadêmica

**Papel:** Professora Helena Sampaio, docente de Cálculo I que corrige para formar hábitos de demonstração, cálculo e modelagem.

**Critérios:**

- Resultado sem desenvolvimento recebe pouco crédito.
- Domínio, ponto de acumulação, hipótese de teorema, convergência e unidade fazem parte da solução.
- Um experimento pode sugerir uma conjectura, mas não conta como prova.
- Uma solução curta e completa vale mais que uma sequência longa de manipulações sem justificativa.

## Contrato de carga e entrega

As dez listas são **obrigatórias** e foram dimensionadas para **2h30 cada**, totalizando 25h. Em toda lista:

- os itens **1–4 são essenciais** e determinam a entrega;
- o item **5 é sempre opcional** e não entra nas 25h;
- reserve aproximadamente 30 minutos por essencial e 30 minutos para revisão e diário de erros;
- a lista só deve ser aberta depois dos módulos indicados no título.

Uma lista conta como entregue somente com tentativas legíveis dos quatro essenciais e uma autoavaliação de cinco linhas. Para cumprir 75%, entregue pelo menos 8 das 10 listas. Respostas e gabaritos permanecem deliberadamente ausentes.

---

## Lista 1 — Após o Módulo 1: ideias fundamentais e funções

1. **Essencial:** Para `f(x)=sqrt((x-1)/(x+2))` e `g(x)=1/(x-3)`, determine domínio e imagem de `f`, e fórmula e domínio de `f∘g`. Registre separadamente cada restrição.
2. **Essencial:** Uma bola percorre `s(t)=20t-5t²` metros. Calcule a velocidade média entre `t` e `t+h`, obtenha a função velocidade instantânea como limite e use-a para localizar o instante de altura máxima no domínio físico.
3. **Essencial:** Para `|r|<1`, derive a fórmula da soma parcial `1+r+...+r^n` e passe ao limite. Compare, sem alegar uma prova baseada apenas em números, o comportamento das somas parciais de `Σ1/n` e `Σ1/n²`.
4. **Essencial:** Inscreva `n` retângulos de mesma largura sob `y=x` em `[0,1]`, usando extremos esquerdos. Escreva a área aproximada como somatório e calcule seu limite. Explique onde aparece a ideia de integral.
5. **Opcional, experimento Python:** trace as primeiras 200 somas parciais das séries geométrica de razão `1/2`, harmônica e `Σ1/n²`. Use o gráfico somente para formular perguntas que a teoria deverá responder.

**Entregável:** quatro essenciais, autoavaliação e uma frase identificando a passagem ao limite em cada item.

---

## Lista 2 — Após os Módulos 2–3: integral e cálculo operacional

1. **Essencial:** Para `f(x)=x²` em `[0,2]`, obtenha as somas inferiores e superiores nas partições regulares com `n` subintervalos. Mostre que a diferença tende a zero e calcule a integral usando `Σi²`.
2. **Essencial:** Derive `F(x)=x²e^(-x)+ln(1+x²)`, indique as regras usadas e encontre os pontos críticos que puder determinar exatamente. Não faça uma análise completa do gráfico.
3. **Essencial:** Se `A(x)=∫_1^(x²)(1+t³)dt`, encontre `A'(x)` pelo TFC e pela cadeia. Depois calcule `∫_0^1 2xe^(x²)dx` por substituição.
4. **Essencial:** Uma caixa sem tampa é feita cortando quadrados de lado `x` dos cantos de uma folha `20 cm × 12 cm`. Modele o volume, determine o domínio físico e localize o candidato a volume máximo por derivação.
5. **Opcional, experimento Python:** compare somas esquerda, direita e ponto médio para `∫_0^2x²dx`; apresente erro absoluto para três valores de `n`.

**Entregável:** quatro essenciais e autoavaliação. No item 4, inclua esboço, unidade e verificação do candidato.

---

## Lista 3 — Após o Módulo 4: reais, sequências e completude

1. **Essencial:** Explique como pares de naturais podem representar inteiros e como pares `(p,q)`, `q≠0`, podem representar racionais por classes de equivalência. Verifique que duas representações diferentes de `2/3` são equivalentes e que a soma não depende da representação nesse exemplo.
2. **Essencial:** Prove que `sqrt(2)` não é racional. Em seguida, explique por que uma expansão decimal infinita periódica representa um racional e por que `0,999...=1` não cria dois reais distintos.
3. **Essencial:** Mostre diretamente pelo critério de Cauchy que `a_n=Σ_(k=1)^n 1/2^k` é uma sequência de Cauchy. Descreva como uma classe de sequências racionais de Cauchy pode representar um número real e qual relação identifica duas sequências.
4. **Essencial:** Seja `A={x∈R:x²<5}`. Mostre que `A` é não vazio e limitado superiormente, use a propriedade do supremo para discutir `s=sup A` e explique como intervalos encaixantes com extremos racionais podem aproximar `s`. Relacione, em um parágrafo, supremo, Cauchy e Bolzano-Weierstrass.
5. **Opcional, desafio:** prove a propriedade dos intervalos encaixantes a partir da propriedade do supremo para intervalos fechados `[a_n,b_n]` com `a_n` crescente, `b_n` decrescente e `b_n-a_n→0`.

**Entregável:** quatro essenciais e autoavaliação, distinguindo claramente afirmações válidas em `Q` das que usam completude de `R`.

---

## Lista 4 — Após o Módulo 5: limites e continuidade rigorosos

1. **Essencial:** Seja `D={0}∪{1/n:n∈N}` e `f:D→R`, `f(x)=x²`. Identifique os pontos de acumulação de `D`, formule corretamente `lim_(x→0,x∈D)f(x)` e prove-o por `ε-δ`.
2. **Essencial:** Prove pelo critério sequencial que `lim_(x→a)f(x)=L`, com `a` ponto de acumulação de `D`, falha se existirem duas sequências em `D\{a}` tendendo a `a` cujas imagens tenham limites diferentes. Aplique o resultado a `f(x)=x/|x|` em `D=R\{0}`.
3. **Essencial:** A partir das definições, prove a regra do produto para limites finitos e use-a para justificar a regra do produto de derivadas. Indique onde a limitação local das funções é necessária.
4. **Essencial:** Classifique em `x=0` as funções `sin x/x` com o ponto removido, `1/x²`, `x/|x|` e `sin(1/x)`. Para cada uma, informe limites laterais relevantes e diferencie descontinuidade removível, salto, infinita e oscilatória.
5. **Opcional, desafio:** prove pela definição que `lim_(x→2,x∈R)x²=4`, construindo um `δ(ε)` explícito.

**Entregável:** quatro essenciais e autoavaliação. Toda expressão de limite deve indicar domínio e ponto de acumulação quando isso não for automático.

---

## Lista 5 — Após o Módulo 6: teoremas de continuidade e integrabilidade

1. **Essencial:** Use o TVI para provar que `x^3+2x-2=0` possui uma raiz em `(0,1)`. Dê um argumento separado para unicidade e identifique qual parte depende apenas de continuidade.
2. **Essencial:** Prove diretamente que `f(x)=x²` é uniformemente contínua em `[0,3]`. Depois mostre que `g(x)=1/x` não é uniformemente contínua em `(0,1)` construindo pares `x_n,y_n`.
3. **Essencial:** Enuncie o Teorema de Heine-Cantor e organize uma prova por contradição usando sequências e Bolzano-Weierstrass. Cada uso de compacidade ou continuidade deve ser identificado.
4. **Essencial:** Seja `f` contínua em `[a,b]`. Use continuidade uniforme para escolher uma partição cuja diferença entre soma superior e inferior seja menor que um `ε>0` dado. Conclua a integrabilidade de Riemann sem supor previamente o TFC.
5. **Opcional, desafio:** construa uma função limitada com uma única descontinuidade e mostre diretamente, por somas superiores e inferiores, que ela é integrável.

**Entregável:** quatro essenciais e autoavaliação. Nos itens 3–4, entregue um mapa lógico das dependências entre completude, compacidade, uniformidade e integrabilidade.

---

## Lista 6 — Após o Módulo 7: TVM, l'Hôpital e Taylor

1. **Essencial:** Use o TVM para provar `|e^x-e^y|≤e|x-y|` quando `x,y∈[0,1]`. Declare o intervalo e a cota da derivada.
2. **Essencial:** Calcule `lim_(x→0)(e^(2x)-1-2x)/x²` por l'Hôpital. Antes de cada aplicação, verifique forma indeterminada, derivabilidade em vizinhança perfurada e não anulamento dos denominadores relevantes.
3. **Essencial:** Encontre o polinômio de Taylor de grau 3 de `ln x` centrado em `1` e use o resto de Lagrange para limitar o erro em `x=1,1`.
4. **Essencial:** Aplique duas iterações do método de Newton a `x²-3=0` a partir de `x_0=2`. Explique sua origem na linearização e use Taylor para discutir por que se espera erro pequeno perto da raiz.
5. **Opcional, experimento Python:** compare o erro de Taylor de graus `1` a `6` para `e^x` em `[-1,1]` com uma cota teórica de resto.

**Entregável:** quatro essenciais e autoavaliação. O item 2 deve conter uma checklist explícita das hipóteses de l'Hôpital.

---

## Lista 7 — Após o Módulo 8: TFC, técnicas e aplicações

1. **Essencial:** Derive `F(x)=∫_(x²)^(cos x)sqrt(1+t⁴)dt`, identificando TFC e regra da cadeia. Não procure uma antiderivada do integrando.
2. **Essencial:** Calcule `∫x²ln x dx`, para `x>0`, e `∫(3x+1)/(x²+x-2)dx` em intervalos que evitem os polos. Justifique integração por partes e decomposição em frações parciais.
3. **Essencial:** Determine a convergência e, quando houver, o valor de `∫_1^∞1/x^(3/2)dx` e `∫_0^1ln x dx`. Escreva cada integral imprópria como limite antes de calcular.
4. **Essencial:** Encontre a área exata entre `y=x` e `y=x²` em `[0,1]`. Depois monte, sem necessidade de calcular, o volume gerado pela rotação dessa região em torno do eixo `x`.
5. **Opcional, experimento Python:** estime por Monte Carlo a **área exata obtida no item 4** e compare erro para tamanhos crescentes de amostra. A simulação não substitui a integral.

**Entregável:** quatro essenciais e autoavaliação, com conferência por derivação das antiderivadas do item 2.

---

## Lista 8 — Após o Módulo 9: inversas, logaritmo e exponencial

1. **Essencial:** Seja `f(x)=x³+x`. Prove que ela é contínua e estritamente crescente em `R`, conclua que a inversa é contínua e calcule `(f^(-1))'(2)` sem encontrar fórmula para a inversa.
2. **Essencial:** Partindo de `ln x=∫_1^x dt/t`, prove que `ln(ab)=ln a+ln b` para `a,b>0` por mudança de variável. Deduza a monotonicidade e a derivada de `ln`.
3. **Essencial:** Defina `exp` como inversa de `ln`. Demonstre `(exp x)'=exp x`, `exp(x+y)=exp x exp y` e derive `x^α` em `x>0` usando `x^α=exp(αln x)`.
4. **Essencial:** Resolva simbolicamente `y'=ky`, `y(0)=y_0`, usando propriedades de `exp`, e determine o tempo de duplicação para `k>0`. Declare por que a inversão por `ln` é legítima.
5. **Opcional, desafio:** mostre que uma função contínua e estritamente monótona em um intervalo tem inversa contínua, usando sequências ou o TVI.

**Entregável:** quatro essenciais e autoavaliação. Não use propriedades usuais de `ln` ou `exp` antes de deduzi-las da construção indicada.

---

## Lista 9 — Após o Módulo 10: sequências, séries e testes

1. **Essencial:** Analise convergência de `a_n=(1+2/n)^n` apenas até onde os teoremas estudados permitirem e prove que `b_n=Σ_(k=1)^n1/k²` é crescente e limitada usando comparação por blocos. Explique o papel da completude.
2. **Essencial:** Pelo critério de Cauchy para séries, prove que a série geométrica converge para `|r|<1` e que a série harmônica diverge agrupando termos em blocos.
3. **Essencial:** Determine a convergência de `Σ1/[n(n+2)]`, `Σ1/(n²+sqrt(n))` e `Σ1/sqrt(n²+1)` usando comparação ou comparação pelo limite. Nomeie a série de referência.
4. **Essencial:** Aplique os testes da razão ou da raiz a `Σn/3^n`, `Σ(2n)!/(n!)²10^n` e `Σ[(n+1)/(2n+1)]^n`. Diga quando o teste escolhido é inconclusivo.
5. **Opcional, experimento Python:** visualize a razão entre termo e série de referência nos itens 3–4, sem usar a figura como critério de convergência.

**Entregável:** quatro essenciais e autoavaliação, com uma tabela “série, teste, hipótese, conclusão”.

---

## Lista 10 — Após os Módulos 11–12: rearranjos, potências e trigonometria

1. **Essencial:** Classifique `Σ(-1)^(n-1)/n` e `Σ(-1)^(n-1)/n²` quanto a convergência absoluta ou condicional. Para a primeira, descreva como um rearranjo pode alterar a soma e por que o mesmo fenômeno não ocorre na segunda.
2. **Essencial:** Determine raio e intervalo de convergência de `Σ_(n=1)^∞(x-2)^n/[n3^n]`. Investigue as extremidades separadamente e escreva a série derivada no interior do raio.
3. **Essencial:** Use o teste `M` de Weierstrass para provar convergência uniforme de `Σx^n/n²` em `[0,1]`. Explique quais passagens ao limite com continuidade e integral ficam autorizadas e por que a diferenciação exige outro argumento.
4. **Essencial:** Defina `S(x)=Σ(-1)^n x^(2n+1)/(2n+1)!` e `C(x)=Σ(-1)^n x^(2n)/(2n)!`. Justifique convergência e diferenciação termo a termo, obtenha `S'=C`, `C'=-S` e deduza que `S²+C²` é constante.
5. **Opcional, experimento Python:** compare somas parciais de `S` e `C` com `math.sin` e `math.cos` para diferentes `x`; interprete o efeito do grau sem tratar a biblioteca como definição matemática.

**Entregável:** quatro essenciais e autoavaliação, incluindo um diagrama que separe convergência pontual, uniforme e absoluta.

---

## Preparação para avaliações

Faça a [P1](./avaliacoes/P1.md) somente após os módulos 1–6 e as listas 1–5. Faça a [P2](./avaliacoes/P2.md) somente após os módulos 7–12 e as listas 6–10. A [PF](./avaliacoes/PF.md) é usada apenas nas condições do [plano de avaliação](./README.md#avaliação-provisória).
