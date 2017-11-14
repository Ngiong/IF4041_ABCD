from abcd.GraphClusterer import GraphClusterer
from graph import EdgeListGraph, AdjListGraph


class GraphClustererTest(object):
    def testClustering(self):
        n_V = 196490  # maximum node index
        n_E = 68091
        el_graph = EdgeListGraph(n_V, n_E)
        el_graph.fromCSV('meet_edited.csv')

        al_graph = AdjListGraph(n_V, n_E)
        al_graph.createFromEdgeListGraph(el_graph)
        # al_graph.printDegrees()

        graph_clusterer = GraphClusterer(al_graph)
        graph_clusterer.traditional_clustering(10)
        print('SUCCESS')


    def runTest(self):
        self.testClustering()


gcTest = GraphClustererTest()
gcTest.runTest()
