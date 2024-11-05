import matplotlib.pyplot as plt
import networkx as nx


class GraphVisualizer:
    def __init__(self, graph):
        self.graph = graph

    def display_graph(self, title="De Bruijn Graph"):
        plt.figure(figsize=(8, 6))
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, node_size=1500, node_color="lightblue", font_size=10,
                font_weight="bold", arrows=True)
        plt.title(title)
        plt.show()
