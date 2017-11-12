import numpy as np

from graph import EdgeListGraph


class AdjListGraph(object):
    def __init__(self, n_V, n_E):
        self.n_V = n_V
        self.n_E = n_E
        self.adj_list = dict()
        for i in range(n_V):
            self.adj_list[i] = dict()
        self.node_weights = np.zeros(n_V)
        self.cluster = np.zeros(n_V)

    def createFromEdgeListGraph(self, graph: EdgeListGraph):
        self.n_V = graph.n_V
        self.n_E = graph.n_E
        edge_list = graph.edge_list
        for i in range(graph.n_E):
            u = edge_list[i][0]; v = edge_list[i][1]; w = edge_list[i][2]
            self.adj_list[u][v] = w; self.adj_list[v][u] = w
            self.node_weights[u] += 1; self.node_weights[v] += 1

    def randomClusters(self, K: int):
        self.cluster = np.random.randint(K, size=self.n_V)

    def print(self):
        print('n_V = ', self.n_V)
        print('n_E = ', self.n_E)
        for u in range(self.n_V):
            print('['+str(u)+'] : ', end='')
            for v in self.adj_list[u]:
                print(str(v)+'/'+str(self.adj_list[u][v])+' ', end='')
            print()
