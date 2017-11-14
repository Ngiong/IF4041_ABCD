from graph import EdgeListGraph


class EdgeListGraphTest(object):
    def testInput(self):
        n_V = 5
        n_E = 3
        el_graph = EdgeListGraph(n_V, n_E)
        el_graph.fromInput()

        el_graph.print()

    def testReadFromCSV(self):
        n_V = 196489 # maximum node index
        n_E = 68091
        el_graph = EdgeListGraph(n_V, n_E)
        el_graph.fromCSV('meet_edited.csv')

        el_graph.print()

    def runTest(self):
        # self.testInput()
        self.testReadFromCSV()


elgTest = EdgeListGraphTest()
elgTest.runTest()