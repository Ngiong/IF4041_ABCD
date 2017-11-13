from abcd import AttractivenessCalculator, ClusterDensityCalculator
from graph import AdjListGraph
from math import inf


class GraphClusterer(object):
    def __init__(self, graph: AdjListGraph):
        self.graph = graph
        self.attract_calc = AttractivenessCalculator(graph)
        self.dense_calc = ClusterDensityCalculator(graph)

    def calculate(self, k1: int, k2: int):
        density1 = self.dense_calc.calculate(k1)
        density2 = self.dense_calc.calculate(k2)
        attractiveness = self.attract_calc.calculate(k1, k2)

        return (attractiveness, density1+density2)

    def merge(self, k1: int, k2: int):
        self.graph.cluster = [k1 if cluster == k2 else cluster for cluster in self.graph.cluster]

    def cluster(self, k: int):
        self.graph.initClusters()
        working_memory = set(range(k))

        ###
        # Kayaknya ini ngga bisa kayak gini deh, karena bisa jadi node2 yg di komparasi pas di working memory
        # ngga bertetangga semua -> jadi ga merging
        #
        # Solusi: ngga perlu optimize, pake cara tradisional aja.
        ###
        for i in range(k, self.graph.n_V):
            working_memory.add(i)

            # Find the best cluster-pair to merge -> best difference
            couples = [(u, v) for u in working_memory for v in working_memory if u < v]
            max_couple = couples[0]; max_diff = -inf; max_diff_tuple = (0, 0)
            for (u, v) in couples:
                (attractiveness, density) = self.calculate(u, v)
                if max_diff < attractiveness-density and attractiveness >= density:
                    max_diff = attractiveness-density
                    max_couple = (u,v)
                    max_diff_tuple = (attractiveness, density)

            # only do merging if Attractiveness >= Sum of cluster density
            if max_diff_tuple[0] >= max_diff_tuple[1]:
                self.merge(max_couple[0], max_couple[1])
                working_memory.remove(max_couple[1])

    def traditional_clustering(self, k: int):
        self.graph.initClusters()
        working_memory = set(self.graph.cluster)

        stop = False
        while not(stop):
            couples = [(u, v) for u in working_memory for v in working_memory if u < v]
            max_couple = None; max_diff = -inf; max_diff_tuple = None
            for (u, v) in couples:
                (attractiveness, density) = self.calculate(u, v)
                if max_diff < attractiveness - density and attractiveness >= density:
                    max_diff = attractiveness - density
                    max_couple = (u, v)
                    max_diff_tuple = (attractiveness, density)

            # only do merging if Attractiveness >= Sum of cluster density
            if max_diff_tuple[0] >= max_diff_tuple[1]:
                self.merge(max_couple[0], max_couple[1])
                working_memory.remove(max_couple[1])

            else:
                stop = True




