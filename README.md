# Trabalho Prático 1 — Resolução de Problemas com Grafos

Disciplina: Resolução de Problemas com Grafos
Orientador: Prof. Me Ricardo Carubbi

## Descrição

Programa que modela um grafo cujos vértices representam os estados da região Nordeste do Brasil e cujas arestas representam fronteiras terrestres entre esses estados. Implementa os algoritmos DFS e BFS para explorar o grafo e responder perguntas sobre conectividade e caminhos.

## Estrutura do projeto

```
Grafos/
├── README.md
├── dados/
│   └── nordeste.txt
└── src/
    ├── main.py
    ├── Graph.py
    ├── depth_first_paths.py
    └── breadth_first_paths.py
```

## Mapeamento de vértices (ordem alfabética)

| Índice | Estado |
|--------|--------|
| 0 | AL |
| 1 | BA |
| 2 | CE |
| 3 | MA |
| 4 | PB |
| 5 | PE |
| 6 | PI |
| 7 | RN |
| 8 | SE |

## Como executar

```bash
cd src
python main.py
```

O programa solicitará o estado de origem e o estado de destino (nome da sigla ou índice numérico) e exibirá:

- Se é possível ir de X até Y atravessando apenas fronteiras terrestres
- O caminho encontrado pela DFS
- O caminho encontrado pela BFS (menor número de fronteiras)
- Os estados alcançáveis a partir de X
- A ordem de visita da DFS
- A ordem de visita da BFS

## Dependências

```bash
pip install algs4
```
