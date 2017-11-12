from graph import EdgeListGraph


class EdgeListGraphTest(object):
    def testInput(self):
        n_V = 5
        n_E = 3
        el_graph = EdgeListGraph(n_V, n_E)
        el_graph.fromInput()

        el_graph.print()

    def runTest(self):
        self.testInput()


elgTest = EdgeListGraphTest()
elgTest.runTest()