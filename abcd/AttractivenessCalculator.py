from graph import AdjListGraph


class AttractivenessCalculator(object):
    def __init__(self, graph: AdjListGraph):
        self.graph = graph

    def calculate(self, k: int):
        return 0