# Instruções para gerar os cursos do `road-to-master.json`

Use este documento sempre que criar, completar ou revisar um curso derivado de [`road-to-master.json`](../road-to-master.json). O objetivo é produzir cursos autogerenciados, em português, fiéis às referências da UFRJ e adaptados à preparação para um mestrado em Inteligência Artificial.

O contrato pedagógico e de arquivos está em [`courses/README.md`](./README.md). A carga e a ordem global estão em [`ROADMAP.md`](./ROADMAP.md). [`MAE111`](./MAE111/) é a implementação de referência, não uma fonte de conteúdo para outras disciplinas.

## Resultado obrigatório

Para cada disciplina com `grade > 0`, produza:

```text
courses/<CODIGO_OFICIAL>/
├── README.md
├── MATERIAL_DE_ESTUDO.md
├── EXERCICIOS.md
└── avaliacoes/
    ├── P1.md
    ├── P2.md
    └── PF.md
```

O código da pasta usa a capitalização oficial, como `ICP144`. A chave do JSON continua sendo o identificador literal e sensível a maiúsculas usado por `link`; por exemplo, a pasta `MAE111` corresponde à chave `mae111`. Não renomeie chaves do JSON durante a geração de um curso.

## Fluxo de geração

### 1. Carregue o contexto

1. Leia o objeto atual da disciplina em `road-to-master.json`.
2. Resolva cada código de `link` como uma chave exata do mesmo JSON.
3. Leia `courses/README.md`, `courses/ROADMAP.md` e esta instrução.
4. Se a pasta do curso existir, leia todos os arquivos antes de editar e preserve soluções, anotações e outros trabalhos do estudante.
5. Consulte o perfil específico da disciplina neste documento.

**Concluído quando:** código, nome, `grade`, dependências, artefatos existentes e perfil específico estão identificados sem inferências pendentes.

### 2. Pesquise a disciplina real

Use fontes primárias nesta ordem:

1. página individual da disciplina no SIGA;
2. matriz curricular ou página institucional do curso na UFRJ;
3. programa detalhado publicado pelo instituto, departamento ou programa de pós-graduação responsável;
4. bibliografia indicada nessas fontes.

Registre no `README.md` do curso:

- URLs consultadas;
- código e nome oficiais;
- carga teórica, prática e total;
- créditos, quando disponíveis;
- ementa curta e programa detalhado;
- bibliografia oficial;
- diferenças entre o JSON, o SIGA e o programa detalhado.

Quando duas fontes oficiais divergirem, preserve as duas informações e explique qual controla o curso. Para `grade: 10`, prefira o programa oficial mais detalhado. Quando um dado não puder ser localizado, marque-o como não localizado; uma estimativa deve aparecer explicitamente como estimativa.

Os pré-requisitos administrativos omitidos intencionalmente do mapa não devem ser reinseridos. `link` é a ordem obrigatória do mapa personalizado, não uma cópia integral do SIGA.

**Concluído quando:** toda afirmação sobre UFRJ, carga, ementa, bibliografia e pré-requisito possui fonte primária ou rótulo de estimativa.

### 3. Calibre a cobertura

Calcule:

```text
fator_de_cobertura = grade / 10
carga_guiada = carga_oficial × fator_de_cobertura
carga_planejada = carga_guiada × 1,5
prática_e_avaliação = carga_guiada × 0,5
```

Use `grade` para selecionar conteúdo, não para reduzir rigor artificialmente:

| Grade | Seleção |
|---:|---|
| 9–10 | Todo o núcleo, tópicos de apoio e aprofundamentos oficiais relevantes |
| 7–8 | Todo o núcleo, principais tópicos de apoio e poucos aprofundamentos |
| 4–6 | Todo o núcleo necessário ao mapa e tópicos de apoio selecionados |
| 1–3 | Visão essencial voltada às dependências posteriores e à IA |
| 0 | Registre a disciplina no mapa, mas não gere o curso |

Classifique cada item da ementa como `núcleo`, `apoio` ou `aprofundamento`. Declare no `README.md` tudo o que foi condensado ou omitido. Um tópico exigido por uma disciplina posterior é núcleo mesmo quando seria secundário isoladamente.

Organize entre 2 e 12 módulos. Um módulo deve representar uma unidade conceitual ensinável e possuir carga explícita; não crie módulos apenas para atingir um número.

Dimensione a prática assim:

| Grade | Listas | Itens essenciais por lista | Item opcional |
|---:|---:|---:|---:|
| 1–3 | 2 | 2 | 1 |
| 4–6 | valor de `grade` | 3 | 1 |
| 7–9 | valor de `grade` | 4 | 1 |
| 10 | 10 | 4 | 1 |

Toda disciplina mantém P1, P2 e PF com dez questões em divisão 3 fáceis, 4 médias e 3 difíceis. A dificuldade é relativa à cobertura selecionada.

| Grade | Duração sugerida de cada prova |
|---:|---:|
| 1–3 | 30 minutos |
| 4–6 | 60 minutos |
| 7–8 | 90 minutos |
| 9–10 | 120 minutos |

Se as provas e listas não couberem em `prática_e_avaliação`, reduza o tamanho de cada tarefa, não ultrapasse silenciosamente a carga. Reserve a carga da PF mesmo no caminho de aprovação direta; nesse caso, use-a em uma síntese integradora.

**Concluído quando:** módulos, listas, avaliações e revisões cabem na carga planejada e cada redução causada por `grade` está declarada.

### 4. Faça um mapa de evidências

Antes de redigir, monte uma matriz de trabalho com estas colunas:

| Objetivo | Módulo | Exemplo | Lista | P1/P2 | PF |
|---|---|---|---|---|---|

Cada objetivo de núcleo deve aparecer em um módulo, ser praticado e ser avaliável. P1 cobre a primeira metade conceitual; P2 cobre a segunda e pode exigir conhecimentos acumulados; PF amostra os fundamentos cumulativos necessários para recuperação.

Use a matriz durante a escrita. Inclua no `README.md` uma versão resumida que permita ao estudante localizar onde cada bloco será aprendido e avaliado.

**Concluído quando:** não existe objetivo nuclear ensinado sem prática, cobrado antes de ser ensinado ou ausente de P1 e P2 em conjunto.

### 5. Escreva o `README.md`

Inclua, nesta ordem:

1. propósito do curso e perfil do estudante;
2. fontes oficiais e divergências encontradas;
3. ficha com código, carga oficial, `grade`, cobertura, carga planejada e `link`;
4. tópicos preservados, condensados e omitidos;
5. objetivos mensuráveis;
6. ordem pedagógica e dependências entre módulos;
7. tabela de módulos e horas, com total conferido;
8. divisão da carga de prática e avaliação;
9. mapa resumido de evidências;
10. materiais e ferramentas;
11. fluxo de estudo por módulo;
12. cronogramas para 4h e 10h por semana;
13. regra de avaliação e critério de conclusão.

Use a regra padrão:

```text
MP = (P1 + P2) / 2
MP >= 7           -> aprovação direta
3 <= MP < 7       -> PF
MP < 3            -> reprovação sem PF
MF = (MP + PF) / 2
MF >= 5           -> aprovação após PF
```

Exija a conclusão de pelo menos 75% das listas. Arredonde para cima quando a quantidade não produzir um inteiro.

**Concluído quando:** as tabelas de carga fecham, os dois cronogramas terminam na mesma carga total e todos os links locais apontam para arquivos existentes.

### 6. Escreva o `MATERIAL_DE_ESTUDO.md`

Comece explicando o escopo e como usar o material. Em cada módulo, mantenha esta sequência:

1. pergunta ou problema motivador;
2. definições e notação;
3. desenvolvimento conceitual;
4. teoremas, algoritmos ou métodos com hipóteses;
5. ao menos um exemplo resolvido inédito;
6. erros comuns;
7. conexão concreta com IA, quando ela existir;
8. checkpoint sem solução.

O texto deve ser autoral e autocontido como primeira exposição. Bibliografia protegida pode orientar estrutura e referências, mas seu texto não deve ser reproduzido. Código deve ser executável; matemática deve distinguir igualdade, aproximação, evidência numérica e prova.

Em cursos computacionais, apresente primeiro o mecanismo e só depois a biblioteca. Em cursos matemáticos, ferramentas simbólicas e numéricas servem para conferência posterior. Em cursos experimentais, registre semente, ambiente, métricas e limitações para permitir reprodução.

**Concluído quando:** todos os módulos planejados possuem explicação, exemplo, erros e checkpoint, sem depender de conteúdo ainda não introduzido.

### 7. Escreva o `EXERCICIOS.md`

Inclua um bloco de persona que explicite como as respostas serão julgadas. Depois declare carga, regra de entrega e ausência de gabaritos.

Cada lista deve:

- ser aberta somente depois dos módulos indicados;
- ter a quantidade de itens essenciais definida pela faixa de `grade`;
- ter um item opcional de extensão, experimento ou comunicação;
- indicar entregáveis verificáveis;
- misturar aplicação direta, integração de conceitos e análise de erros;
- caber no tempo reservado no plano;
- evitar repetir exemplos resolvidos trocando apenas números.

Distribua as listas de forma complementar às provas. Use desafios adequados ao perfil específico da disciplina, descrito mais abaixo.

**Concluído quando:** contagem, cobertura, ordem e carga de todas as listas conferem com o `README.md`.

### 8. Escreva P1, P2 e PF

Cada prova deve ter:

- persona e política de correção;
- condições de realização e duração;
- valor total 10,0;
- 3 questões fáceis de 0,5 ponto;
- 4 questões médias de 1,0 ponto;
- 3 questões difíceis de 1,5 ponto;
- exatamente 10 questões e nenhum gabarito.

Fácil aplica diretamente um conceito nuclear. Média combina conceitos ou exige justificativa. Difícil exige demonstração, projeto de algoritmo, interpretação experimental ou decisão com trade-offs, conforme a disciplina.

As provas devem caber na duração prevista. P1 e P2 não podem repetir literalmente exemplos, checkpoints ou listas. PF deve ser cumulativa, apropriada à recuperação e cobrir fundamentos em vez de concentrar apenas os tópicos mais difíceis.

Use a skill local `assessment-generator` para calibrar a divisão 3/4/3, preservando os nomes de arquivos deste contrato. Use `study-mode` apenas depois de uma tentativa do estudante, para corrigir ou ensinar sem revelar prematuramente o gabarito.

**Concluído quando:** cada prova tem 10 questões, soma 10,0, respeita a cobertura temporal e pode ser concluída no tempo declarado.

### 9. Audite antes de encerrar

Verifique todos estes itens:

- o JSON continua válido;
- todo `link` referencia uma chave existente e o grafo não possui ciclo;
- a pasta usa o código oficial e o `README.md` registra a chave do JSON;
- carga guiada, prática e total obedecem às fórmulas;
- a soma das horas dos módulos coincide com a carga guiada;
- cronogramas de 4h e 10h chegam ao mesmo total;
- todos os itens nucleares aparecem no mapa de evidências;
- exemplos resolvidos estão matematicamente ou tecnicamente corretos;
- código e comandos propostos foram executados quando possível;
- listas e provas cabem nas durações declaradas;
- cada prova possui exatamente 3/4/3 questões e soma 10,0;
- nenhum gabarito ou solução das avaliações foi incluído;
- links Markdown locais existem;
- fontes externas são primárias e suas URLs funcionam;
- nenhum trabalho do estudante foi sobrescrito.

Faça uma segunda leitura procurando especificamente afirmações falsas, notação ambígua, exercícios impossíveis, técnicas cobradas cedo demais e repetições disfarçadas.

**Concluído quando:** cada item foi verificado e qualquer limitação residual está registrada no relatório final.

### 10. Relate o resultado

Informe:

- arquivos criados ou alterados;
- fontes oficiais utilizadas;
- carga e efeito de `grade`;
- tópicos condensados ou omitidos;
- contagens de módulos, listas, exercícios e questões;
- verificações executadas;
- limitações ou fatos oficiais não encontrados.

## Ordem de produção

Gere em ordem topológica para que cursos posteriores possam reutilizar notação e resultados já estabelecidos:

| Fase | Cursos a gerar |
|---:|---|
| 1 | `MAE111` já produzido; `ICP144`, `ICP116`, `ICP361` |
| 2 | `ICP115`, `ICP238`, `MAE992`, `ICP368` |
| 3 | `MAD243`, `ICP248`, `ICP351`, `ICP365` |
| 4 | `ICP363`, `ICP019` |
| 5 | `ICP472`, `CPE727` |

Cursos da mesma fase podem ser produzidos em paralelo somente quando não houver dependência entre eles. Sempre releia o JSON: a ordem acima é um plano atual, não substitui `link`.

## Perfis específicos

### `icp144` / pasta `ICP144` — Matemática Discreta — grade 4

- **Recorte:** preserve combinatória básica, inclusão-exclusão, recorrências e os conceitos de grafos necessários a `ICP115` e `ICP368`; trate contagem de árvores, planaridade e cinco cores de forma condensada.
- **P1:** permutações, combinações, binomiais, inclusão-exclusão, Fibonacci e recorrências.
- **P2:** representação, grau, caminhos, conectividade, Euler, Hamilton, árvores, bipartição, planaridade e coloração.
- **Prática:** demonstrações curtas, construção de contraexemplos, modelagem por grafos e pequenos verificadores em Python.
- **Ferramentas:** Python padrão; `networkx` apenas depois da implementação ou análise manual.
- **Síntese:** modelar um problema real como grafo e justificar propriedades sem delegá-las à biblioteca.

### `mae111` / pasta `MAE111` — Cálculo Infinitesimal I — grade 10

- **Estado:** curso de referência já produzido; revise-o em vez de regenerá-lo sem solicitação explícita.
- **Fonte controladora:** programa detalhado do Instituto de Matemática, incluindo fundamentos dos reais, Taylor univariado e séries.
- **P1:** ideias fundamentais, integral de Riemann, cálculo operacional, completude, limites e continuidade.
- **P2:** TVM, Taylor univariado, TFC, inversas, construção de `ln`/`exp`, sequências e séries.
- **Prática:** cálculos, provas, modelagem e experimentos numéricos opcionais.
- **Ferramentas:** papel; Python e sistema simbólico somente para conferência posterior.

### `icp115` / pasta `ICP115` — Álgebra Linear Algorítmica — grade 6

- **Recorte:** preserve espaços, subespaços, independência, bases, coordenadas, transformações, sistemas, autovalores e diagonalização; comprima exemplos repetitivos em dimensão dois.
- **P1:** vetores, combinações, bases, subespaços, matrizes, transformações e eliminação gaussiana.
- **P2:** mudança de base, soma/interseção/complementos, autovalores, autovetores e diagonalização.
- **Prática:** demonstrações, cálculos manuais e implementação de eliminação, mudança de base e iteração simples.
- **Ferramentas:** Python e NumPy para conferência; as rotinas nucleares devem ser implementadas antes de chamar solucionadores prontos.
- **Síntese:** representar a mesma transformação em bases diferentes e analisar uma diagonalização aplicável a dados.

### `ICP116` — Estruturas de Dados — grade 10

- **Recorte:** cubra integralmente complexidade, listas, árvores de busca e balanceadas, heaps, tabelas hash, conjuntos disjuntos, filas de prioridade e ordenações da ementa.
- **P1:** análise assintótica, listas sequenciais/dinâmicas, recursão associada e algoritmos de ordenação iniciais.
- **P2:** árvores, balanceamento, heap, hash, conjuntos disjuntos, filas de prioridade, radix, quicksort e heapsort.
- **Prática:** implementação do zero, invariantes, testes aleatórios, análise amortizada quando pertinente e benchmarks interpretados.
- **Ferramentas:** Python, `pytest` e medição padrão; coleções prontas podem servir como oráculo, não como solução.
- **Síntese:** biblioteca de estruturas com testes, documentação de complexidade e benchmark reproduzível.

### `ICP238` — Introdução à Computação Numérica — grade 2

- **Recorte:** visão essencial de ponto flutuante, erro, condicionamento, Taylor, zeros, interpolação, integração e EDO; priorize reconhecimento de limitações e escolha de método.
- **P1:** representação, propagação de erro, condicionamento, Taylor e um método de zeros.
- **P2:** interpolação, quadratura e um método de passo único para EDO.
- **Prática:** dois notebooks curtos comparando método, erro e referência; derivação mínima necessária para interpretar resultados.
- **Ferramentas:** Python, NumPy e Matplotlib; SciPy apenas como referência comparativa.
- **Síntese:** demonstrar uma falha numérica causada por condicionamento ou cancelamento e explicar sua origem.

### `MAE992` — Cálculo Integral e Diferencial II — grade 10

- **Recorte:** cubra curvas, cinemática vetorial, funções multivariáveis, derivadas direcionais e parciais, diferencial, implícitas, Lagrange, Hessiana e EDOs de primeira e segunda ordem.
- **P1:** curvas; limites e derivadas multivariáveis; aproximação linear; gradiente; implícitas; Hessiana e otimização com restrições.
- **P2:** EDOs de primeira ordem e EDOs lineares de segunda ordem com coeficientes constantes.
- **Prática:** cálculos, provas de hipóteses, visualização de superfícies, campos vetoriais e verificação numérica de soluções.
- **Ferramentas:** Python, NumPy, Matplotlib e SciPy como apoio após solução analítica.
- **Síntese:** modelar e analisar um sistema dinâmico simples, conectando solução, estabilidade local e visualização.

### `ICP248` — Computação Científica e Análise de Dados — grade 9

- **Recorte:** preserve sistemas lineares, LU/QR, Jacobi/Seidel, mínimos quadrados, splines, potência, algoritmo QR, SVD, pseudoinversa, redução de dimensão, Newton e gradiente descendente.
- **P1:** modelagem de sistemas, métodos diretos/iterativos, condicionamento e ajuste por mínimos quadrados/splines.
- **P2:** autovalores, SVD, pseudoinversa, redução de dimensão e sistemas não lineares.
- **Prática:** implementar versões didáticas, comparar com bibliotecas e medir resíduo, erro, estabilidade e custo.
- **Ferramentas:** Python, NumPy, SciPy, pandas, Matplotlib e notebooks reproduzíveis.
- **Síntese:** pipeline numérico de dados que compare duas escolhas de método e justifique a mais adequada.

### `MAD243` — Estatística e Probabilidade — grade 10

- **Recorte:** cubra análise exploratória, probabilidade, variáveis aleatórias, distribuições, conjuntas/marginais/condicionais, esperança, teoremas limite, amostragem, estimação e testes.
- **P1:** exploração, axiomas, condicionamento, variáveis discretas/contínuas, distribuições conjuntas e esperança.
- **P2:** leis dos grandes números, TCL, distribuições amostrais, estimação, intervalos e testes de hipóteses.
- **Prática:** derivações, simulações, interpretação de incerteza e análise reproduzível de dados reais.
- **Ferramentas:** Python, NumPy, SciPy, pandas, Matplotlib ou Seaborn.
- **Síntese:** relatório estatístico que separe análise exploratória, inferência, suposições, tamanho de efeito e limitações.

### `ICP351` — Modelagem Matemática e Computacional — grade 8

- **Recorte:** preserve processo de modelagem, classificação, equações de diferenças/diferenciais, otimização, grafos e cadeias de Markov; selecione domínios aplicados relevantes a IA.
- **P1:** perguntas, hipóteses, variáveis, escalas, classificação e modelos por diferenças/EDOs.
- **P2:** otimização, grafos, Markov, calibração, validação e comunicação de limitações.
- **Prática:** formular antes de programar, estimar parâmetros, validar contra dados e fazer análise de sensibilidade.
- **Ferramentas:** Python, NumPy, SciPy, pandas, NetworkX e notebooks conforme o modelo.
- **Síntese:** estudo de modelagem completo com pergunta, formulação, calibração, validação e crítica.

### `ICP368` — Algoritmos e Grafos — grade 10

- **Recorte:** cubra representações, ordenação topológica, BFS/DFS, decomposição, recursão, guloso, programação dinâmica e fluxo máximo.
- **P1:** representações, percursos, conectividade, DAGs, ordenação topológica, recursão e decomposição.
- **P2:** projeto guloso, programação dinâmica, provas de correção e fluxo máximo.
- **Prática:** implementação, invariantes, contraexemplos para estratégias incorretas, correção e complexidade.
- **Ferramentas:** Python e `pytest`; NetworkX somente como oráculo ou comparação.
- **Síntese:** solucionar um problema em grafo por duas técnicas e comparar correção, custo e limites.

### `ICP361` — Programação Concorrente — grade 5

- **Recorte:** preserve processos, threads, memória compartilhada, mensagens, locks, semáforos, condições, deadlock, starvation, segurança, futuros e `async/await`; comprima ambientes alternativos.
- **P1:** modelos de concorrência, comunicação, condições de corrida e sincronização.
- **P2:** problemas clássicos, deadlock/starvation, thread safety, assíncrono, testes e desempenho.
- **Prática:** reproduzir falhas, controlar interleavings, testar propriedades e medir throughput/latência.
- **Ferramentas:** `threading`, `multiprocessing` e `asyncio`; Go pode ser extensão opcional para comparar modelos.
- **Síntese:** serviço concorrente acompanhado de teste de estresse, análise de segurança e perfil de desempenho.

### `ICP363` — Introdução ao Aprendizado de Máquina — grade 10

- **Recorte:** cubra história, paradigmas, ética, avaliação, regressão, árvores, Bayes, redes neurais, SVM, agrupamento, associação, reforço e programação em lógica indutiva.
- **P1:** formulação de problemas, ética, divisão de dados, métricas, regressão, árvores, Bayes e classificação linear.
- **P2:** redes, SVM, agrupamento, associação, reforço, lógica indutiva e comparação de paradigmas.
- **Prática:** implementar mecanismos centrais, usar pipelines, evitar vazamento e avaliar erro por subgrupo.
- **Ferramentas:** Python, NumPy, pandas, scikit-learn e Matplotlib; PyTorch apenas na introdução neural.
- **Síntese:** projeto reproduzível com baseline, validação, comparação de modelos, análise de erros e model card curto.

### `ICP365` — Otimização — grade 5

- **Recorte:** preserve modelagem, programação linear, inteira e não linear irrestrita; concentre aplicações em problemas computacionais e de IA.
- **P1:** formulação, geometria e solução de programação linear, dualidade apenas se confirmada no programa oficial detalhado.
- **P2:** integralidade, relaxações, condições de primeira/segunda ordem e métodos irrestritos.
- **Prática:** formular manualmente, resolver instâncias pequenas e interpretar certificado, convergência e sensibilidade.
- **Ferramentas:** Python, SciPy Optimize e PuLP ou OR-Tools quando compatíveis com o método estudado.
- **Síntese:** modelar o mesmo problema em versão contínua e inteira e explicar a diferença das soluções.

### `ICP019` — Álgebra Linear Aplicada — grade 5

- **Recorte:** preserve matrizes definidas positivas, Cholesky/QR, métodos iterativos espectrais, SVD/aproximação, condicionamento, esparsidade, blocos e pré-condicionamento.
- **P1:** estrutura positiva definida, fatorações, condicionamento e estabilidade.
- **P2:** autovalores/SVD iterativos, aproximação de baixa ordem, matrizes esparsas, blocos e pré-condicionadores.
- **Prática:** experimentos com matrizes densas e esparsas, medindo resíduo, erro, memória e convergência.
- **Ferramentas:** NumPy, SciPy Linear Algebra, SciPy Sparse e Matplotlib.
- **Síntese:** comparar duas representações ou fatorações em um problema de dados de porte crescente.

### `ICP472` — Metodologia da Pesquisa — grade 5

- **Recorte:** preserve tipos e processo de pesquisa, pergunta, relevância, revisão, ética, métodos, coleta, análise, planejamento e cronograma.
- **P1:** concepções de conhecimento, tipos de pesquisa, problema, pergunta, relevância e busca bibliográfica.
- **P2:** desenho metodológico, dados, análise, ética, redação, cronograma e avaliação de validade.
- **Prática:** fichamento, mapa de literatura, crítica de artigo, protocolo e escrita iterativa; código só quando fizer parte do método.
- **Ferramentas:** Markdown, BibTeX e gerenciador bibliográfico opcional.
- **Síntese:** proposta curta de pesquisa em IA com pergunta, lacuna, método, riscos, ética e plano de análise.

### `CPE727` — Aprendizado Profundo — grade 5

- **Fonte:** disciplina de mestrado do Programa de Engenharia Elétrica da COPPE; deixe explícito que não pertence à grade do BCC.
- **Recorte:** preserve estatística de ordem superior, otimização, regularização, modelos de energia/representação, redes convolutivas, redes recursivas e aplicações; tópicos modernos adicionais devem aparecer como extensão identificada.
- **P1:** fundamentos de treinamento, otimização, regularização e aprendizagem de representações/modelos de energia.
- **P2:** arquiteturas convolutivas e recursivas, desenho experimental e aplicações.
- **Prática:** implementação de treino, diagnóstico de gradientes, ablações, curvas de aprendizagem e reprodução controlada.
- **Ferramentas:** Python, PyTorch, NumPy e Matplotlib; registre sementes, versões, dispositivo e orçamento computacional.
- **Síntese:** experimento de deep learning com baseline, ablação, análise de falhas, custo e relatório reproduzível.

## Comando de execução

Para gerar uma disciplina, use uma solicitação neste formato:

```text
Gere o curso <CHAVE_DO_JSON> seguindo integralmente
courses/INSTRUCOES_DE_GERACAO.md. Pesquise primeiro as fontes oficiais,
preserve trabalhos existentes, produza todos os seis arquivos do contrato
e execute toda a auditoria antes de encerrar.
```

Para gerar todos, processe uma fase por vez e valide o grafo novamente entre fases. A conclusão de uma fase exige que todos os seus cursos tenham passado pela auditoria individual.
