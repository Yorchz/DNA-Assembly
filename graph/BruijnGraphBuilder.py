from collections import defaultdict
import networkx as nx


class BruijnGraphBuilder:
    def __init__(self, kmers):
        self.kmers = kmers
        self.graph = defaultdict(list)
        self.nx_graph = nx.DiGraph()

    def build_graph(self):
        for kmer in self.kmers:
            prefix = kmer[:-1]
            suffix = kmer[1:]
            self.graph[prefix].append(suffix)
            self.nx_graph.add_edge(prefix, suffix)
        return dict(self.graph), self.nx_graph
