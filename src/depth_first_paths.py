class DepthFirstPaths:

    def __init__(self, graph, source):

        self._marked = [False] * graph.V  # quais vértices já foram visitados
        self._edge_to = [-1] * graph.V    # de qual vértice chegamos em cada um
        self._source = source
        self._order = []                  # ordem de visita dos vértices
        self._dfs(graph, source)
        
    #Explora recursivamente todos os vértices alcançáveis a partir de v.
    def _dfs(self, graph, v):
  
        self._marked[v] = True
        self._order.append(v)
        for w in graph.adj[v]:
            if not self._marked[w]:
                self._edge_to[w] = v
                self._dfs(graph, w)

    def has_path_to(self, v):
        """Retorna True se existe caminho da origem até v."""
        return self._marked[v]

    def path_to(self, v):
        """Reconstrói e retorna o caminho da origem até v, ou None se não existir."""
        if not self.has_path_to(v):
            return None
        path = []
        x = v
        while x != self._source:
            path.append(x)
            x = self._edge_to[x]
        path.append(self._source)
        path.reverse()
        return path

    def reachable(self):
        """Retorna a lista de todos os vértices alcançáveis a partir da origem."""
        return [v for v, visited in enumerate(self._marked) if visited]

    def visit_order(self):
        """Retorna a ordem em que os vértices foram visitados pelo DFS."""
        return list(self._order)
