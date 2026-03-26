import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from algs4.graph import Graph
from depth_first_paths import DepthFirstPaths
from breadth_first_paths import BreadthFirstPaths

STATES = ['AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE']

DATA_FILE = os.path.join(os.path.dirname(__file__), 'dados', 'nordeste.txt')

#armazena as infos de oq eh vertice e oq eh aresta, e tem um metodo pra imprimir o grafo
def load_graph(path):
    with open(path) as f:
        v = int(f.readline())
        e = int(f.readline())
        g = Graph(v)
        for _ in range(e):
            a, b = f.readline().split()
            g.add_edge(a, b)
    return g


def name(v):
    return STATES[v]


def index(state):
    if state.isdigit():
        return int(state)
    return STATES.index(state.upper())


def fmt_path(path):
    return ' -> '.join(name(v) for v in path)


def main():
    graph = load_graph(DATA_FILE)

    print("Estados disponíveis:", ', '.join(f'{i}:{s}' for i, s in enumerate(STATES)))
    origin = input("\nEstado de origem: ").strip()
    dest   = input("Estado de destino: ").strip()

    src = index(origin)
    dst = index(dest)

    dfp = DepthFirstPaths(graph, src)
    bfp = BreadthFirstPaths(graph, src)

    print(f"\n{'='*55}")
    print(f"  Origem: {name(src)}   |   Destino: {name(dst)}")
    print(f"{'='*55}")

    # 1. É possível chegar?
    if dfp.has_path_to(dst):
        print(f"\nÉ possível ir de {name(src)} até {name(dst)}.")
    else:
        print(f"\nNão é possível ir de {name(src)} até {name(dst)}.")

    # 2. Caminho encontrado pelo DFS
    dfs_path = dfp.path_to(dst)
    print(f"\n[DFS] Caminho encontrado:")
    print(f"  {fmt_path(dfs_path) if dfs_path else 'Nenhum caminho encontrado.'}")

    # 3. Caminho encontrado pelo BFS (mais curto)
    bfs_path = bfp.path_to(dst)
    print(f"\n[BFS] Caminho encontrado (menor número de fronteiras):")
    print(f"  {fmt_path(bfs_path) if bfs_path else 'Nenhum caminho encontrado.'}")

    # 4. Estados alcançáveis a partir da origem
    reachable = dfp.reachable()
    print(f"\n[Alcançáveis] A partir de {name(src)}:")
    print(f"  {', '.join(name(v) for v in reachable)}")

    # 5. Ordem de visita do DFS
    print(f"\n[DFS] Ordem de visita:")
    print(f"  {' -> '.join(name(v) for v in dfp.visit_order())}")

    # 6. Ordem de visita do BFS
    print(f"\n[BFS] Ordem de visita:")
    print(f"  {' -> '.join(name(v) for v in bfp.visit_order())}")




if __name__ == '__main__':
    main()
