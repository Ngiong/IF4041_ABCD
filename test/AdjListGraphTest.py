from graph import EdgeListGraph, AdjListGraph


class AdjListGraphTest(object):
    def testConvert(self):
        n_V = 5
        n_E = 3
        el_graph = EdgeListGraph(n_V, n_E)
        el_graph.fromInput()

        al_graph = AdjListGraph(n_V, n_E)
        al_graph.createFromEdgeListGraph(el_graph)
        al_graph.print()

    def runTest(self):
        self.testConvert()

algTest = AdjListGraphTest()
algTest.runTest()