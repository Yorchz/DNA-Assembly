import networkx as nx


class EulerianPath:
    def __init__(self, graph, nx_graph):
        self.graph = graph
        self.nx_graph = nx_graph
        self.path_manual = []
        self.path_nx = []

    def has_eulerian_path(self):

        return nx.has_eulerian_path(self.nx_graph)

    def find_path_manual(self):
        stack = []
        current = next(iter(self.graph))
        stack.append(current)

        while stack:
            if current in self.graph and self.graph[current]:
                stack.append(current)
                next_vertex = self.graph[current].pop()
                current = next_vertex
            else:
                self.path_manual.append(current)
                current = stack.pop()

        self.path_manual.reverse()
        return self.path_manual

    def find_path_nx(self):
        if not self.has_eulerian_path():
            raise nx.NetworkXError("Graph has no Eulerian paths.")

        eulerian_path_edges = list(nx.eulerian_path(self.nx_graph))
        self.path_nx = [edge[0] for edge in eulerian_path_edges] + [eulerian_path_edges[-1][1]]
        return self.path_nx
