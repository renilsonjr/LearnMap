# Listas de Exercícios — ICP115

## Persona acadêmica

**Papel:** professora de Álgebra Linear e revisora de software científico, avaliando se o estudante conecta definição, cálculo, prova e implementação.

**Critérios de correção:**

- um resultado sem base, sistema, operações elementares ou justificativa perde o núcleo da pontuação;
- código deve explicitar entrada, hipótese, tolerância e caso de falha, além de incluir testes pequenos verificáveis à mão;
- NumPy pode atuar como oráculo depois da implementação pedida, mas sua saída não substitui a análise;
- exemplos numéricos sugerem propriedades; apenas um argumento geral as demonstra;
- notação, dimensões e base de cada coordenada fazem parte da resposta.

## Contrato de carga e entrega

As seis listas são obrigatórias e foram dimensionadas para **2h30 cada**, totalizando 15h. Em toda lista:

- os itens **1–3 são essenciais** e determinam a entrega;
- o item **4 é opcional** e não integra as 15h;
- reserve até 45 minutos por essencial e 15 minutos para autoavaliação;
- a lista só deve ser aberta depois dos módulos indicados no título.

Uma lista conta como entregue quando contém tentativas legíveis dos três essenciais, todos os artefatos pedidos e uma autoavaliação de cinco linhas. Para cumprir 75%, entregue pelo menos 5 das 6 listas. Respostas e gabaritos permanecem deliberadamente ausentes.

---

## Lista 1 — Após o Módulo 1: vetores, geração e coordenadas

1. **Essencial — cálculo e interpretação.** Sejam `u=(1,2)` e `v=(3,-1)`.
   - Verifique se `B=(u,v)` é base de `R²` por um critério explícito.
   - Encontre `[(7,3)]_B`.
   - Reconstrua o vetor a partir das coordenadas e explique por que a coluna obtida não precisa ser `(7,3)^T`.
2. **Essencial — independência sem determinante.** Em `R³`, considere `a=(1,0,1)`, `b=(0,1,1)` e `c=(1,1,k)`, com `k∈R`. Resolva a relação `αa+βb+γc=0` e classifique, para cada valor de `k`, se a lista é independente. Quando houver dependência, exiba uma relação não trivial.
3. **Essencial — auditoria de argumento.** Um colega escreve: “os vetores `p` e `q` não são múltiplos, então `(p,q,r)` é uma base de `R³` para qualquer `r`”. Produza um contraexemplo numérico e depois reescreva a afirmação com hipóteses suficientes. Justifique a versão corrigida.
4. **Opcional — visualização.** Faça um programa que receba dois vetores de `R²`, desenhe o paralelogramo gerado e permita comparar pares quase dependentes. Registre por que a área visual pequena não prova dependência exata em ponto flutuante.

**Entregável:** cálculos dos três essenciais, contraexemplo do item 3 e autoavaliação distinguindo geração de independência.

---

## Lista 2 — Após o Módulo 2: sistemas e eliminação

1. **Essencial — eliminação auditável.** Resolva por operações elementares e classifique em função de `t∈R`:

   ```text
   x +  y +  z = 2
   2x + 3y +  z = 5
   3x + 4y + 2z = t.
   ```

   Para cada caso, informe posto da matriz de coeficientes, posto da aumentada, pivôs, variáveis livres e conjunto-solução quando existir.
2. **Essencial — estrutura do homogêneo.** Para

   ```text
   A = [1  2 -1  0]
       [2  4  1  3]
       [0  0  3  3],
   ```

   encontre uma parametrização de `Ax=0`, uma base do espaço de soluções e sua dimensão. Substitua a forma paramétrica na equação original para verificar o resultado.
3. **Essencial — implementação.** Implemente eliminação gaussiana ou forma escalonada reduzida **sem** `numpy.linalg`. A função deve:
   - validar dimensões;
   - trocar linhas quando o pivô corrente for zero;
   - distinguir sistema inconsistente, solução única e infinitas soluções;
   - devolver pivôs e uma representação verificável do resultado;
   - passar por pelo menos quatro testes: um de cada classificação e um que exija troca de linhas.
4. **Opcional — experimento numérico.** Compare sua função com `numpy.linalg.solve` em sistemas quadrados aleatórios com solução única. Depois construa um exemplo com linhas quase dependentes e discuta como a tolerância muda a classificação observada.

**Entregável:** sequência de operações do item 1, parametrização verificada do item 2, código e saída dos quatro testes do item 3, além da autoavaliação.

---

## Lista 3 — Após os Módulos 3–4: subespaços e transformações

1. **Essencial — subespaço, base e coordenadas.** Considere

   `W={(x,y,z,w)∈R⁴ : x+y-z=0 e y+w=0}`.

   Prove que `W` é subespaço, obtenha uma base e a dimensão, e encontre as coordenadas de `(2,-1,1,1)` nessa base. Se o vetor não pertencer a `W`, identifique a inconsistência em vez de forçar coordenadas.
2. **Essencial — núcleo, imagem e estrutura.** Seja `T:R⁴→R³` dada por

   `T(x_1,x_2,x_3,x_4)=(x_1+x_2, x_2+x_3, x_1+2x_2+x_3)`.

   Construa a matriz canônica, encontre bases de `ker(T)` e `im(T)`, confira posto-nulidade e decida se `T` é injetiva ou sobrejetiva. Cada decisão deve citar um critério, não apenas as dimensões finais.
3. **Essencial — prova e contraexemplo.** Prove que, se `T:V→W` é linear e `(v_1,...,v_k)` é uma lista que gera `V`, então `(T(v_1),...,T(v_k))` gera `im(T)`. Depois mostre, por contraexemplo, que a imagem de uma lista independente não precisa ser independente.
4. **Opcional — codificação linear.** Construa uma matriz `C:R⁵→R³` de posto `3`. Produza dois vetores distintos com a mesma codificação, verifique que sua diferença pertence ao núcleo e escreva uma interpretação curta sobre perda de informação.

**Entregável:** provas dos itens 1 e 3, bases com verificação por substituição, matriz e tabela de dimensões do item 2, e autoavaliação.

---

## Lista 4 — Após o Módulo 5: soma, interseção e complementos

1. **Essencial — algoritmo de interseção.** Em `R⁴`, sejam

   `U=span((1,0,1,0),(0,1,0,1),(1,1,1,1))`

   e

   `W=span((1,1,0,0),(0,0,1,1),(1,0,0,1))`.

   Remova primeiro geradores redundantes. Depois use a equação matricial `[P -Q] (a,b)^T=0` para obter bases de `U∩W` e `U+W`. Verifique a fórmula das dimensões.
2. **Essencial — soma direta e decomposição.** Defina

   `A=span((1,1,0),(0,1,1))` e `B=span((1,0,1))` em `R³`.

   Decida se `R³=A⊕B`. Se a resposta for positiva, decomponha `(4,2,0)` de forma única como `a+b`; se for negativa, apresente o certificado que falha e construa um complemento válido de `A` para então fazer a decomposição.
3. **Essencial — teorema com hipóteses.** Prove que, se `V=U⊕W`, a decomposição `v=u+w` é única. Prove também a recíproca apropriada: se todo `v∈V` possui uma única decomposição desse tipo, então `V=U⊕W`. Identifique em qual passo aparece `U∩W={0}`.
4. **Opcional — gerador de complementos.** Implemente uma função que receba uma base de `U≤R^n`, estenda-a usando vetores canônicos e devolva uma base de algum complemento algébrico. Teste-a em dois subespaços e verifique as dimensões por eliminação.

**Entregável:** matrizes aumentadas e bases verificadas dos itens 1–2, demonstração em duas direções do item 3 e autoavaliação que diferencie união, soma e soma direta.

---

## Lista 5 — Após o Módulo 6: mudança de base

1. **Essencial — coordenadas em três bases.** Em `R³`, use

   `B=((1,1,0),(0,1,1),(1,0,1))`

   e

   `C=((1,0,0),(1,1,0),(1,1,1))`.

   Calcule as matrizes de base `P_B` e `P_C`, a transição `C←B` por sistemas lineares e as coordenadas de `v=(5,3,2)` nas bases `B` e `C`. Confira que a transição leva uma coluna à outra.
2. **Essencial — operador em bases diferentes.** Seja `T:R²→R²` dada na base canônica por

   ```text
   A = [5 -2]
       [6 -3],
   ```

   e seja `B=((1,1),(1,3))`. Calcule `[T]_B` de duas maneiras: pelas colunas `[T(b_j)]_B` e por `P_B^-1AP_B`. Aplique ambas as representações a `x=(2,4)` e reconcilie as colunas obtidas.
3. **Essencial — implementação e teste metamórfico.** Implemente conversão de coordenadas resolvendo sistemas, sem formar inversa explicitamente. Para pelo menos cinco vetores, verifique automaticamente a propriedade de ida e volta `B→C→B`. Inclua um teste em que as “colunas da base” são dependentes e a função deve rejeitar a entrada.
4. **Opcional — custo e precisão.** Compare formar a inversa com resolver um sistema usando rotinas de biblioteca em matrizes aleatórias. Não conclua superioridade universal pelo tempo de uma única execução; registre tamanho, semente, número de repetições, resíduo e ambiente.

**Entregável:** matrizes com indicação de origem e destino, duas derivações do item 2, código e relatório dos testes do item 3, e autoavaliação sobre a direção de cada transformação de coordenadas.

---

## Lista 6 — Após os Módulos 7–8: espectro, diagonalização e iteração

1. **Essencial — diagonalização completa.** Para

   ```text
   A = [2 0 0]
       [1 2 0]
       [0 0 4],
   ```

   calcule o polinômio característico, as multiplicidades algébricas e geométricas, bases dos autoespaços e decida se `A` é diagonalizável sobre `R`. Se não for, explique por que possuir autovalores reais não é suficiente.
2. **Essencial — dinâmica em uma base de autovetores.** Considere

   ```text
   B = [3 1]
       [1 3]
   ```

   e `x_0=(3,1)`. Diagonalize `B`, decomponha `x_0` na base escolhida, obtenha fórmula para `x_k=B^kx_0` e descreva o comportamento da direção normalizada. Confira sua fórmula para `k=2` por multiplicação direta.
3. **Essencial — experimento reproduzível.** Implemente a iteração de potência sem chamar `numpy.linalg.eig`. Use uma matriz simétrica `4×4` com autovalor dominante simples e:
   - registre matriz, vetor inicial, número de iterações e tolerância;
   - reporte estimativa do autovalor, vetor normalizado e resíduo `||Av-λv||` por iteração;
   - compare somente ao final com uma rotina de biblioteca;
   - execute um segundo caso que viole uma hipótese de convergência e explique o comportamento observado.
4. **Opcional — comunicação aplicada.** Escolha uma pequena matriz de transição, afinidade ou propagação com significado declarado. Analise uma direção dominante, mas escreva também um parágrafo separando resultado algébrico, interpretação plausível e afirmações que os dados não autorizam.

**Entregável:** cálculo espectral completo do item 1, derivação e conferência do item 2, código, tabela de resíduos e análise de hipóteses do item 3, além da autoavaliação.

---

## Preparação para avaliações

Faça a [P1](./avaliacoes/P1.md) somente após os módulos 1–4 e as listas 1–3. Faça a [P2](./avaliacoes/P2.md) somente após os módulos 5–8 e as listas 4–6. A [PF](./avaliacoes/PF.md) é usada apenas nas condições do [plano de avaliação](./README.md#avaliação-e-conclusão).
