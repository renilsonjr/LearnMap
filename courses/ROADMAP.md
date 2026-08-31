# Roadmap de preparação para Inteligência Artificial

Esta simulação aplica o [modelo dos cursos](./README.md) às 16 disciplinas de [`road-to-master.json`](../road-to-master.json). Ela serve para dimensionar o projeto antes da produção dos demais materiais; não é um calendário imutável.

## Premissas

- `grade` controla cobertura: a carga guiada é `carga oficial × grade/10`.
- Exercícios, revisão e avaliações acrescentam 50% à carga guiada.
- O ano de planejamento possui 46 semanas de estudo e 6 de pausa.
- Com 4h semanais, há uma disciplina ativa; com 10h, podem existir até duas.
- Toda dependência em `link` deve estar concluída antes do início da disciplina dependente.
- Pré-requisitos da UFRJ omitidos intencionalmente do mapa não entram na carga.

## Carga por disciplina

| Código | Disciplina | Grade | Carga oficial | Carga planejada | Dependências do mapa |
|---|---|---:|---:|---:|---|
| `icp144` | Matemática Discreta | 4 | 60h | 36h | — |
| `mae111` | Cálculo Infinitesimal I | 10 | 90h | 135h | — |
| `icp115` | Álgebra Linear Algorítmica | 6 | 90h | 81h | `icp144` |
| `ICP116` | Estruturas de Dados | 10 | 60h | 90h | — |
| `ICP238` | Introdução à Computação Numérica | 2 | 30h | 9h | `mae111` |
| `MAE992` | Cálculo Integral e Diferencial II | 10 | 60h | 90h | `mae111` |
| `ICP248` | Computação Científica e Análise de Dados | 9 | 60h | 81h | `icp115`, `MAE992`, `ICP238` |
| `MAD243` | Estatística e Probabilidade | 10 | 60h | 90h | `MAE992` |
| `ICP351` | Modelagem Matemática e Computacional | 8 | 60h | 72h | `MAE992`, `icp115` |
| `ICP368` | Algoritmos e Grafos | 10 | 60h | 90h | `icp144`, `ICP116` |
| `ICP361` | Programação Concorrente | 5 | 60h | 45h | — |
| `ICP363` | Introdução ao Aprendizado de Máquina | 10 | 60h | 90h | `ICP248`, `MAD243` |
| `ICP365` | Otimização | 5 | 60h | 45h | `icp115`, `ICP238` |
| `ICP019` | Álgebra Linear Aplicada | 5 | 60h | 45h | `ICP248` |
| `ICP472` | Metodologia da Pesquisa | 5 | 60h | 45h | `ICP351`, `ICP363` |
| `CPE727` | Aprendizado Profundo | 5 | 45h | 33h45 | `ICP363`, `ICP365`, `ICP019` |

### Totais

| Medida | Carga |
|---|---:|
| Soma das cargas oficiais, antes de aplicar `grade` | 975h |
| Conteúdo guiado após aplicar `grade` | 718h30 |
| Exercícios, revisões e avaliações | 359h15 |
| **Plano completo** | **1.077h45** |

As cargas oficiais vêm do [currículo vigente do BCC/UFRJ no SIGA](https://siga.ufrj.br/sira/repositorio-curriculo/distribuicoes/402FED54-92A4-F79C-3ACF-54A4EA89ED35.html); `CPE727` vem do [catálogo do Programa de Engenharia Elétrica da COPPE](https://www.pee.ufrj.br/disciplinas/). A carga planejada é uma decisão deste mapa, não uma equivalência acadêmica emitida pela universidade.

## Ordem por dependências

As fases representam conjuntos liberados pelo grafo. Dentro de cada fase, a simultaneidade depende do orçamento semanal.

| Fase | Disciplinas | Condição para avançar |
|---:|---|---|
| 1 | `mae111`, `icp144`, `ICP116`, `ICP361` | Concluir as bases necessárias para a trilha escolhida |
| 2 | `MAE992`, `ICP238`, `icp115`, `ICP368` | `MAE992`, `ICP238` e `icp115` liberam o núcleo quantitativo |
| 3 | `MAD243`, `ICP248`, `ICP351`, `ICP365` | Concluir `ICP248` e `MAD243` antes de aprendizado de máquina |
| 4 | `ICP363`, `ICP019` | Concluir ambas e também `ICP365` antes de aprendizado profundo |
| 5 | `CPE727`, `ICP472` | Síntese técnica e preparação para pesquisa |

`ICP361` é independente no mapa e pode ocupar uma janela em que uma segunda disciplina ainda esteja bloqueada. As fases não autorizam violar um `link`: por exemplo, `ICP248` só começa quando seus três requisitos estiverem concluídos.

## Simulação de duração

| Disponibilidade | Semanas líquidas | Anos com 46 semanas de estudo | Estratégia |
|---:|---:|---:|---|
| 4h/semana | aproximadamente 270 | aproximadamente 5,9 anos | Uma disciplina por vez |
| 10h/semana | aproximadamente 108 | aproximadamente 2,4 anos | Até duas disciplinas simultâneas |

Esses são limites de planejamento obtidos por divisão da carga. Reprovações, semanas incompletas e reforços aumentam a duração; aproveitamento demonstrado em checkpoints pode reduzi-la sem remover objetivos essenciais.

## Primeiro curso produzido

[`MAE111`](./MAE111/) possui 135h planejadas:

- 4h por semana: 34 semanas;
- 10h por semana: 14 semanas.

O cronograma detalhado está no [plano da disciplina](./MAE111/README.md#cronogramas-sugeridos).
