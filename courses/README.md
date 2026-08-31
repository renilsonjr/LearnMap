# Modelo dos cursos

Este diretório transforma as disciplinas de [`road-to-master.json`](../road-to-master.json) em cursos autogerenciados. O JSON define o mapa e a ordem; cada subdiretório contém a execução pedagógica de uma disciplina. A carga e a ordem global estão simuladas em [`ROADMAP.md`](./ROADMAP.md); o procedimento completo para agentes está em [`INSTRUCOES_DE_GERACAO.md`](./INSTRUCOES_DE_GERACAO.md).

[`MAE111`](./MAE111/) é a implementação de referência deste modelo.

## Contrato de uma disciplina

Cada curso deve conter:

```text
courses/<CODIGO>/
├── README.md
├── MATERIAL_DE_ESTUDO.md
├── EXERCICIOS.md
└── avaliacoes/
    ├── P1.md
    ├── P2.md
    └── PF.md
```

| Arquivo | Responsabilidade |
|---|---|
| `README.md` | Plano de ensino, objetivos, carga, módulos, cronogramas, avaliação e critérios de conclusão |
| `MATERIAL_DE_ESTUDO.md` | Explicação autoral, exemplos resolvidos, erros comuns, conexões com IA e checkpoints sem solução |
| `EXERCICIOS.md` | Prática progressiva adequada à natureza da disciplina, sem gabarito |
| `avaliacoes/P1.md` | Avaliação da primeira metade do curso |
| `avaliacoes/P2.md` | Avaliação da segunda metade do curso |
| `avaliacoes/PF.md` | Avaliação cumulativa, usada somente quando P1 e P2 não forem suficientes |

## Escala de cobertura

O campo `grade`, de 0 a 10, controla a quantidade de conteúdo produzido. Ele não representa nota, crédito ou dificuldade acadêmica.

`fator de cobertura = grade / 10`

A carga guiada inicial é a carga oficial da disciplina multiplicada pelo fator de cobertura. O planejamento reserva ainda 50% dessa carga para exercícios, revisões e avaliações:

`carga planejada = carga oficial × fator de cobertura × 1,5`

| Grade | Cobertura pretendida |
|---:|---:|
| 10 | Próxima de 100% da disciplina real |
| 8 | Aproximadamente 80% |
| 5 | Versão resumida, aproximadamente 50% |
| 2 | Visão essencial, aproximadamente 20% |
| 0 | Disciplina registrada, sem curso a produzir |

Mesmo em versões resumidas, os objetivos essenciais e as dependências conceituais devem permanecer visíveis. A redução ocorre primeiro em aprofundamentos, demonstrações secundárias, quantidade de exemplos e volume de exercícios; um pré-requisito necessário não deve ser silenciosamente removido.

## Fontes e fidelidade

- A ementa e a carga horária devem vir preferencialmente do SIGA ou de outra fonte institucional da UFRJ.
- O material explicativo deve ser autoral. Bibliografia protegida serve como referência, não como texto a ser reproduzido.
- Os tópicos preservam o rigor acadêmico da disciplina, mas exemplos, projetos e ritmo podem ser adaptados à preparação para Inteligência Artificial.
- `link` contém códigos do próprio JSON e representa a ordem obrigatória deste mapa personalizado. Ele não pretende reproduzir todos os pré-requisitos administrativos da UFRJ, pois alguns foram dispensados pelo conhecimento prévio do estudante.

## Avaliação padrão

- Cada prova vale 10,0.
- `MP = (P1 + P2) / 2`.
- `MP >= 7`: aprovação direta.
- `3 <= MP < 7`: realização da PF.
- `MP < 3`: reprovação sem PF.
- Depois da PF, `MF = (MP + PF) / 2`; `MF >= 5` representa aprovação.
- Pelo menos 75% das atividades obrigatórias devem ser entregues.
- P1, P2 e PF têm dez questões: 3 fáceis, 4 médias e 3 difíceis.
- Nas provas do modelo, questões fáceis valem 0,5, médias valem 1,0 e difíceis valem 1,5, totalizando 10,0.
- Provas e listas não incluem gabaritos. A correção posterior deve usar as skills locais de avaliação e tutoria.

## Desafios por natureza

| Área | Evidência principal de aprendizagem |
|---|---|
| Matemática | Cálculos, demonstrações, hipóteses de teoremas e modelagem |
| Algoritmos e estruturas | Implementação, testes, provas de correção e análise de complexidade |
| Computação numérica | Notebooks, análise de erro, estabilidade e comparação de métodos |
| Estatística | Derivações, interpretação, simulação e análise de dados |
| Modelagem | Formulação, hipóteses, calibração, validação e comunicação |
| Concorrência | Implementação, testes não determinísticos, diagnóstico e medição |
| Aprendizado de máquina | Experimentos reproduzíveis, métricas, análise de erros e projetos com dados |
| Metodologia da pesquisa | Leitura crítica, revisão bibliográfica e proposta de pesquisa |

Python é a linguagem padrão para atividades computacionais, sem impedir outra linguagem quando ela oferecer melhor contato com o fenômeno estudado.

## Ritmo e simultaneidade

Os cursos são autogerenciados e avançam por domínio, não por presença em um calendário fixo. Os cronogramas devem mostrar pelo menos os cenários de 4h e 10h semanais.

- Com 4h semanais, a referência é uma disciplina ativa.
- Com 10h semanais, podem existir até duas disciplinas ativas, desde que a soma das cargas semanais caiba no orçamento.
- Uma disciplina só começa quando todos os códigos de `link` estiverem concluídos.
- As sessões devem ser distribuídas em pelo menos dois dias da semana para permitir recuperação espaçada.
