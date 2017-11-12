from graph import AdjListGraph


class ClusterDensityCalculator(object):
    def __init__(self, graph: AdjListGraph):
        self.graph = graph

    def calculate(self, k: int):
        # Get all node in specified cluster (k)
        cluster_node = [i for i in range(self.graph.n_V) if self.graph.cluster[i] == k]

        # Sum total node_weight
        sum = 0
        for node in cluster_node:
            sum += self.graph.node_weights[node]

        return sum / len(cluster_node)