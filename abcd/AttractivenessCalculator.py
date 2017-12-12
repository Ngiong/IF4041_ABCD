from graph import AdjListGraph

class AttractivenessCalculator(object):
    def __init__(self, graph: AdjListGraph):
        self.graph = graph

    def calculate(self, k1: int, k2: int):
        # Get all edges connecting node in k1 and node in k2, sum the edge weight
        sum_weight = 0
        cluster_node1 = [i for i in range(self.graph.n_V) if self.graph.cluster[i] == k1]
        cluster_node2 = [i for i in range(self.graph.n_V) if self.graph.cluster[i] == k2]

        for node1 in cluster_node1:
            for node2 in cluster_node2:
                if node2 in self.graph.adj_list[node1]: sum_weight += self.graph.adj_list[node1][node2]

        # Count each cluster members
        Q1 = len(cluster_node1)
        Q2 = len(cluster_node2)

        return sum_weight / (Q1 * Q2)