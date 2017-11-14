import numpy as np


class EdgeListGraph(object):
    def __init__(self, n_V, n_E):
        self.n_V = n_V
        self.n_E = n_E
        self.edge_list = np.zeros((n_E, 3)) # u <-> v, weight

    def fromInput(self):
        for i in range(self.n_E):
            idx = str(i)
            self.edge_list[i][0] = input('['+idx+'] '+'u: ')
            self.edge_list[i][1] = input('['+idx+'] '+'v: ')
            self.edge_list[i][2] = input('['+idx+'] '+'w: ')

    def fromCSV(self, path):
        self.edge_list = np.genfromtxt(path, delimiter=',', dtype=int)

    def print(self):
        for i in range(min(self.n_E, 20)):
            print(self.edge_list[i][0], end=' ')
            print(self.edge_list[i][1], end=' ')
            print(self.edge_list[i][2])