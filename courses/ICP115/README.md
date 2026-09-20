# ICP115 — Álgebra Linear Algorítmica

Curso autogerenciado, em português, para quem se prepara para um mestrado em Inteligência Artificial e já concluiu a base de Matemática Discreta prevista neste mapa. O curso trata vetores, espaços e transformações como objetos matemáticos e como estruturas computáveis: primeiro se define e calcula à mão; depois se implementa o mecanismo; por fim, usa-se NumPy para conferir resultados.

## Fontes oficiais e divergências

Foram consultadas estas fontes primárias da UFRJ:

- a [página individual de ICP115 no SIGA](https://siga.ufrj.br/sira/repositorio-curriculo/disciplinas/A77314FF-92A4-F79C-7132-D8E0C3F02040.html), que fornece nome, ementa e bibliografia;
- a [distribuição curricular do BCC no SIGA](https://siga.ufrj.br/sira/repositorio-curriculo/distribuicoes/402FED54-92A4-F79C-3ACF-54A4EA89ED35.html), que registra 5 créditos, 60h teóricas, 30h práticas, 0h de extensão e os requisitos administrativos ICP136 e ICP144;
- a [grade curricular publicada pelo Instituto de Computação](https://ic.ufrj.br/info/grade-curricular-bcc/), que confirma código, nome, 5 créditos, 90h e posição no terceiro período;
- as notas institucionais [Álgebra Linear Algorítmica](https://ic.ufrj.br/~collier/lectures/ala.pdf), de S. C. Coutinho, indicadas pela bibliografia do SIGA e usadas como segunda exposição.

Não foi localizado um programa oficial mais detalhado que a ementa do SIGA. Portanto, ela controla o núcleo deste curso; a organização em módulos é uma decisão pedagógica deste repositório.

As divergências e decisões são:

- o objeto `icp115` em `courses/road-to-master.json` reproduz a ementa oficial, mas deixa a bibliografia vazia; este plano registra abaixo as seis referências do SIGA;
- o SIGA exige administrativamente ICP136 e ICP144. O mapa personalizado mantém somente `icp144` em `link`; ICP136 não é reinserida, conforme o contrato do repositório;
- o JSON não separa a carga. O currículo oficial registra 60h teóricas e 30h práticas, total de 90h;
- a expressão oficial “complemento de subespaços” é tratada como **complemento algébrico**. Complemento ortogonal exigiria produto interno, que não consta da ementa e não é presumido.

### Bibliografia oficial

1. S. C. Coutinho. *Álgebra linear algorítmica*. Notas de aula.
2. T. Banchoff e J. Wermer. *Linear Algebra Through Geometry*. 2ª ed., Springer.
3. T. S. Blyth e E. F. Robertson. *Basic Linear Algebra*. Springer.
4. L. Smith. *Linear Algebra*. 3ª ed., Springer.
5. G. Strang. *Álgebra Linear e suas Aplicações*. Cengage.
6. L. N. Trefethen e D. Bau III. *Numerical Linear Algebra*. SIAM.

## Ficha do curso

| Item | Definição |
|---|---|
| Código oficial / pasta | `ICP115` |
| Chave literal no JSON | `icp115` |
| Nome oficial | Álgebra Linear Algorítmica |
| Créditos | 5 |
| Carga oficial | 90h: 60h teóricas, 30h práticas e 0h de extensão |
| `grade` | 6 de 10; fator de cobertura `0,6` |
| Carga guiada | 54h: 36h teóricas e 18h práticas guiadas |
| Prática, revisão e avaliação | 27h |
| Carga planejada | 81h |
| Dependência obrigatória do mapa | `icp144` |
| Avaliações | P1, P2 e PF condicional, 60 minutos cada |

Os cálculos seguem o contrato: `90h × 0,6 = 54h` guiadas; `54h × 0,5 = 27h` adicionais; total `81h`.

## Cobertura selecionada

### Preservado como núcleo

- vetores no plano e em `R^n`, combinação linear, geração, dependência e independência;
- subespaços, base, dimensão e coordenadas;
- sistemas lineares, operações elementares, forma escalonada, eliminação gaussiana, posto e interpretação do conjunto-solução;
- transformações lineares, matriz em bases escolhidas, núcleo, imagem e teorema posto-nulidade;
- soma, interseção e complementos algébricos de subespaços;
- mudança de base para vetores e operadores;
- autovalores, autovetores, polinômio característico e diagonalização;
- implementação didática de eliminação, mudança de base e iteração de potência simples.

### Condensado

- a primeira passagem geométrica em dimensão dois é incorporada aos módulos gerais, evitando repetir em `R²` toda definição depois apresentada em `R^n`;
- determinantes aparecem apenas como ferramenta para invertibilidade e polinômio característico, sem uma unidade independente;
- exemplos com autovalores concentram-se em matrizes reais pequenas, com discussão breve do caso em que não há base real de autovetores;
- demonstrações repetitivas de propriedades matriciais são substituídas por invariantes e provas representativas.

### Omitido por não constar do núcleo oficial

Produto interno, ortogonalidade, projeções ortogonais, Gram–Schmidt, mínimos quadrados, fatorações LU/QR/SVD, condicionamento e análise de estabilidade ficam para `ICP248` e `ICP019`. Formas canônicas de Jordan e teoria espectral complexa também ficam fora. Essas omissões reduzem aprofundamentos; não removem pré-requisitos de `ICP248`, `ICP351` ou `ICP365` previstos pelo mapa.

## Objetivos mensuráveis

Ao concluir as 81h, o estudante deverá ser capaz de:

1. representar vetores como combinações lineares e decidir se um conjunto gera um espaço ou é linearmente independente;
2. formular um sistema como matriz aumentada, executar eliminação gaussiana e classificar o conjunto-solução;
3. testar se um subconjunto é subespaço e obter bases, dimensão e coordenadas em subespaços de `R^n`;
4. verificar linearidade, construir a matriz de uma transformação e determinar núcleo, imagem, posto e nulidade;
5. calcular soma e interseção de subespaços, aplicar a fórmula das dimensões e construir complementos algébricos;
6. converter coordenadas e matrizes de operadores entre bases, verificando que o objeto linear não muda com sua representação;
7. calcular e interpretar autovalores e autoespaços, decidindo se um operador é diagonalizável;
8. usar uma diagonalização para calcular potências e analisar uma dinâmica linear discreta;
9. implementar versões didáticas de eliminação, mudança de coordenadas e iteração de potência, explicitando hipóteses e limitações;
10. distinguir igualdade exata, aproximação numérica, evidência computacional e demonstração.

## Ordem pedagógica e dependências

O curso começa com a linguagem vetorial e transforma a eliminação gaussiana no algoritmo central. A eliminação sustenta os testes de geração, independência, base, núcleo e imagem. Só depois dessas ferramentas aparecem operações entre subespaços e mudança de base. Autovalores vêm no final porque exigem domínio de sistemas homogêneos, bases e representação matricial; a diagonalização encerra o curso ao reunir todos esses conceitos.

```text
M1 Vetores e bases no plano
 └─> M2 Sistemas e eliminação
      └─> M3 Subespaços, independência e coordenadas
           └─> M4 Transformações, núcleo e imagem ── P1
                ├─> M5 Soma, interseção e complementos
                └─> M6 Mudança de base
                     └─> M7 Autovalores e autoespaços
                          └─> M8 Diagonalização e iteração ── P2
```

## Módulos e carga guiada

| Módulo | Conteúdo central | Teoria | Prática guiada | Total |
|---|---|---:|---:|---:|
| 1 | Vetores no plano, combinação linear, geração, independência, base e coordenadas | 4h | 2h | 6h |
| 2 | Matrizes, sistemas lineares, operações elementares e eliminação gaussiana | 5h | 3h | 8h |
| 3 | `R^n`, subespaços, bases, dimensão e coordenadas | 5h30 | 2h30 | 8h |
| 4 | Transformações lineares, matrizes, núcleo, imagem e posto-nulidade | 5h30 | 2h30 | 8h |
| 5 | Soma, interseção e complementos algébricos de subespaços | 4h | 2h | 6h |
| 6 | Mudança de base de vetores e operadores | 4h30 | 2h30 | 7h |
| 7 | Autovalores, autovetores, autoespaços e critérios de diagonalização | 4h | 2h | 6h |
| 8 | Diagonalização, potências, dinâmicas e iteração de potência simples | 3h30 | 1h30 | 5h |
| **Total** |  | **36h** | **18h** | **54h** |

## Prática, revisão e avaliação — 27h

| Atividade | Horas |
|---|---:|
| Seis listas, com três itens essenciais por lista | 15h |
| Retentativas dos checkpoints e diário de erros | 3h |
| Revisões dirigidas para P1 e P2 | 4h |
| Realização de P1 e P2 | 2h |
| Reserva para PF e preparação, ou síntese integradora | 3h |
| **Total** | **27h** |

Cada lista dispõe de 2h30: até 45 minutos por item essencial e 15 minutos de autoavaliação. O opcional não integra a carga. A reserva da PF é mantida mesmo em aprovação direta; nesse caso, ela serve para uma síntese que representa uma transformação em duas bases e analisa uma diagonalização aplicada a dados ou a uma dinâmica.

## Mapa resumido de evidências

| Objetivo nuclear | Módulo e exemplo | Lista | Avaliação regular | PF |
|---|---|---|---|---|
| Combinação, geração, independência e coordenadas | M1, decomposição em uma base do plano | L1 | P1 | Q1, Q4 |
| Sistemas e eliminação | M2, sistema `3 × 3` e algoritmo | L2 | P1 | Q2, Q5, Q8 |
| Subespaços, bases e dimensão | M3, plano por equação homogênea | L3 | P1 | Q4, Q9 |
| Transformações, núcleo, imagem e posto | M4, aplicação de `R³` em `R²` | L3 | P1 | Q3, Q6, Q9 |
| Soma, interseção e complementos | M5, dois planos coordenados | L4 | P2 | Q7, Q9 |
| Mudança de base | M6, operador em base de autovetores | L5 | P2 | Q6, Q10 |
| Autovalores, autovetores e diagonalização | M7, matriz com dois autoespaços | L6 | P2 | Q7, Q10 |
| Potências e iteração | M8, dinâmica diagonalizável e iteração de potência | L6 | P2 | Q10 |
| Implementação de eliminação, coordenadas e iteração | M2, M6 e M8, com código didático e hipóteses | L2, L5 e L6 | P1 Q8; P2 Q10 | Q8, Q10 |
| Exatidão, aproximação e evidência computacional | M2 e M8, tolerância e resíduo | L2 e L6 | P2 Q10 | Q10 |

## Materiais e ferramentas

- [Material de estudo](./MATERIAL_DE_ESTUDO.md): exposição autocontida dos oito módulos.
- [Listas de exercícios](./EXERCICIOS.md): seis listas obrigatórias, cada uma com três itens essenciais e um opcional.
- [P1](./avaliacoes/P1.md): módulos 1–4.
- [P2](./avaliacoes/P2.md): módulos 5–8, com uso cumulativo da primeira metade.
- [PF](./avaliacoes/PF.md): recuperação cumulativa dos fundamentos.
- papel ou tablet para cálculos e demonstrações;
- Python 3 para implementar os algoritmos nucleares;
- NumPy apenas para conferir uma solução já obtida ou comparar resultados após a implementação manual.

Não use `numpy.linalg.solve`, `eig`, `inv` ou rotinas equivalentes como solução de uma atividade que pede o mecanismo. Uma tolerância numérica é uma decisão do algoritmo, não uma prova de que um número real é zero.

## Fluxo de estudo por módulo

1. Leia a pergunta motivadora e tente respondê-la com o repertório atual.
2. Reescreva definições com seus próprios exemplos e contraexemplos.
3. Refaça o exemplo resolvido sem consultar a etapa seguinte.
4. Execute à mão o algoritmo antes de programá-lo; só então compare com NumPy.
5. Responda ao checkpoint sem solução e classifique qualquer erro como conceitual, algébrico, de hipótese, de representação ou numérico.
6. Abra a lista somente após os módulos indicados e refaça, 48 horas depois, o primeiro item que revelou erro conceitual.

## Cronogramas sugeridos

As fases são sequenciais e somam exatamente 81h. O checkpoint inicial pertence à carga guiada do módulo; as 3h adicionais de consolidação servem para retentativa e diário de erros.

### Ritmo de 4h por semana — 21 semanas

| Ordem | Fase | Horas | Acumulado | Conclusão aproximada |
|---:|---|---:|---:|---:|
| 1 | Módulo 1; depois, Lista 1 | 8h30 | 8h30 | semana 3 |
| 2 | Módulo 2; depois, Lista 2 | 10h30 | 19h | semana 5 |
| 3 | Módulo 3; depois, Lista 3 | 10h30 | 29h30 | semana 8 |
| 4 | Módulo 4; consolidação de 1h30; revisão de P1; P1 | 12h30 | 42h | semana 11 |
| 5 | Módulo 5; depois, Lista 4 | 8h30 | 50h30 | semana 13 |
| 6 | Módulo 6; depois, Lista 5 | 9h30 | 60h | semana 15 |
| 7 | Módulos 7–8; depois, Lista 6 | 13h30 | 73h30 | semana 19 |
| 8 | Consolidação de 1h30; revisão de P2; P2 | 4h30 | 78h | semana 20 |
| 9 | PF condicional ou síntese integradora | 3h | **81h** | semana 21 |

### Ritmo de 10h por semana — 9 semanas

| Ordem | Fase | Horas | Acumulado | Conclusão aproximada |
|---:|---|---:|---:|---:|
| 1 | Módulo 1; depois, Lista 1 | 8h30 | 8h30 | semana 1 |
| 2 | Módulo 2; depois, Lista 2 | 10h30 | 19h | semana 2 |
| 3 | Módulo 3; depois, Lista 3 | 10h30 | 29h30 | semana 3 |
| 4 | Módulo 4; consolidação de 1h30; revisão de P1; P1 | 12h30 | 42h | semana 5 |
| 5 | Módulo 5; depois, Lista 4 | 8h30 | 50h30 | semana 6 |
| 6 | Módulo 6; depois, Lista 5 | 9h30 | 60h | semana 6 |
| 7 | Módulos 7–8; depois, Lista 6 | 13h30 | 73h30 | semana 8 |
| 8 | Consolidação de 1h30; revisão de P2; P2 | 4h30 | 78h | semana 8 |
| 9 | PF condicional ou síntese integradora | 3h | **81h** | semana 9 |

No ritmo acelerado, as fases 5–6 e 7–8 compartilham semanas; a ordem interna continua obrigatória. Em ambos os ritmos, distribua o estudo por pelo menos dois dias da semana.

## Avaliação e conclusão

Cada prova vale 10,0 e segue a divisão de 3 questões fáceis de 0,5 ponto, 4 médias de 1,0 ponto e 3 difíceis de 1,5 ponto.

```text
MP = (P1 + P2) / 2
MP >= 7           -> aprovação direta
3 <= MP < 7       -> PF
MP < 3            -> reprovação sem PF
MF = (MP + PF) / 2
MF >= 5           -> aprovação após PF
```

As seis listas são obrigatórias. O critério de 75% é arredondado para cima: é necessário entregar pelo menos **5 listas completas**, cada uma com tentativas verificáveis dos três itens essenciais e autoavaliação.

O curso termina quando o estudante satisfaz a regra de nota aplicável, entrega ao menos cinco listas, corrige o diário de erros e conclui a PF ou a síntese integradora reservada. Resultados de biblioteca sem formulação, desenvolvimento e interpretação não demonstram os objetivos do curso.
