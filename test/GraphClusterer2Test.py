from abcd.GraphClusterer2 import GraphClusterer2
from graph import EdgeListGraph, AdjListGraph
import operator


class GraphClusterer2Test(object):
    def testLabel(self):
        clusterer = GraphClusterer2()

        clusterer.node = {0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7}
        clusterer.labelTree = {0:-1, 1:0, 2:-1, 3:1, 4:2, 5:1, 6:-1, 7:2}

        for k in clusterer.node:
            print(clusterer.label(k))

    def testDensity(self):
        clusterer = GraphClusterer2()

        clusterer.node = {0:0, 1:1, 2:2}
        clusterer.labelTree = {0:-1, 1:-1, 2:0}
        clusterer.clusterSum = {0:6, 1:7, 2:8}
        clusterer.clusterCount = {0:2, 1:3, 2:1}

        for k in clusterer.node:
            print(clusterer.density(k))

    def testAttractiveness(self):
        clusterer = GraphClusterer2()

        clusterer.node = {0: 0, 1: 1, 2: 2, 3: 3}
        clusterer.labelTree = {0: -1, 1: -1, 2: 0, 3: -1}
        clusterer.attractivenessSum = {(0, 1): 15, (0,2): 10, (1,2): 10, (0,3):12, (1,3):14, (2,3):17 }
        clusterer.clusterCount = {0: 2, 1: 3, 2: 1, 3: 2}

        for k1 in clusterer.node:
            for k2 in clusterer.node:
                print(k1, "(",clusterer.label(k1),") ",k2, "(",clusterer.label(k2),") ", clusterer.attractiveness(k1,k2))


    def testIsInterInterested(self):
        clusterer = GraphClusterer2()

        clusterer.node = {0: 0, 1: 1, 2: 2, 3: 3}
        clusterer.labelTree = {0: -1, 1: -1, 2: 0, 3: -1}
        clusterer.attractivenessCount = {(0, 1): 2, (0,2): 2, (1,2): 2, (0,3):2, (1,3):2, (2,3):2 }
        clusterer.clusterCount = {0: 2, 1: 3, 2: 1, 3: 2}

        for k1 in clusterer.node:
            for k2 in clusterer.node:
                print(k1, "(",clusterer.label(k1),") ",k2, "(",clusterer.label(k2),") ", clusterer.isInterInterested(k1,k2))

    def testIsMergeable(self):
        clusterer = GraphClusterer2()

        clusterer.node = {0: 0, 1: 1, 2: 2, 3: 3}
        clusterer.edge = {(0, 1): 0, (0, 2): 1, (1, 2): 2, (0, 3): 3, (1, 3): 4, (2, 3): 5}
        clusterer.labelTree = {0: -1, 1: -1, 2: 0, 3: -1}
        clusterer.attractivenessCount = {(0, 1): 4, (0,2): 2, (1,2): 4, (0,3):2, (1,3):2, (2,3):2 }
        clusterer.attractivenessSum = {(0, 1): 30, (0, 2): 10, (1, 2): 10, (0, 3): 12, (1, 3): 14, (2, 3): 17}
        clusterer.clusterSum = {0: 6, 1: 6, 2: 8, 3:3}
        clusterer.clusterCount = {0: 2, 1: 3, 2: 1, 3: 2}

        for k1 in clusterer.node:
            for k2 in clusterer.node:
                print(k1, "(",clusterer.label(k1),") ",k2, "(",clusterer.label(k2),") ", clusterer.isMergeable(k1,k2))

    def testRemoveEdge(self):
        clusterer = GraphClusterer2()

        clusterer.edge = {(0,1):0, (0,2):1, (1,2): 2}
        clusterer.labelTree = {0: -1, 1: -1, 2: -1}
        clusterer.attractivenessCount = {(0, 1): 1, (0,2): 1, (1,2): 1}
        clusterer.attractivenessSum = {(0, 1): 10, (0,2): 10, (1,2): 10}

        clusterer.removeEdge(0,2)
        print(clusterer.edge)
        print(clusterer.attractivenessCount)
        print(clusterer.attractivenessSum)

    def testMerge(self):
        clusterer = GraphClusterer2()

        clusterer.node = {0: 0, 1: 1, 2: 2, 3: 3}
        clusterer.edge = {(0, 1): 0, (0, 2): 1, (1, 2): 2, (0, 3): 3, (1, 3): 4, (2, 3): 5}
        clusterer.labelTree = {0: -1, 1: -1, 2: -1, 3: -1}
        clusterer.clusterCount = {0: 1, 1: 2, 2: 3, 3: 4}
        clusterer.clusterSum = {0: 1, 1: 4, 2: 9, 3: 16}
        clusterer.attractivenessCount = {(0, 1): 1, (0, 2): 2, (1, 2): 3, (0, 3): 4, (1, 3): 5, (2, 3): 6}
        clusterer.attractivenessSum = {(0, 1): 1, (0, 2): 4, (1, 2): 9, (0, 3): 16, (1, 3): 25, (2, 3): 36}

        clusterer.merge(1,2)
        print("node : ",clusterer.node)
        print("edge : ",clusterer.edge)
        print("tree : ",clusterer.labelTree)
        print("total node count in cluster : ",clusterer.clusterCount)
        print("total node weight in cluster : ",clusterer.clusterSum)
        print("total edge count between cluster : ", clusterer.attractivenessCount)
        print("total edge weight between cluster : ", clusterer.attractivenessSum)

    def testLoad(self):
        clusterer = GraphClusterer2()
        clusterer.load("loadTest.csv")
        print("node : ", clusterer.node)
        print("edge : ", clusterer.edge)
        print("tree : ", clusterer.labelTree)
        print("total node count in cluster : ", clusterer.clusterCount)
        print("total node weight in cluster : ", clusterer.clusterSum)
        print("total edge count between cluster : ", clusterer.attractivenessCount)
        print("total edge weight between cluster : ", clusterer.attractivenessSum)


    def testCluster(self):
        csv = "meet_sampled_1000.csv"
        clusterer = GraphClusterer2()
        clusterer.cluster(csv)
        f = open("out1_"+csv, 'w')
        for k,v in clusterer.clusterByGroup:
            f.write(str(k)+","+str(v)+"\n")
            print(k,",",v)
        f.close()
        print(sorted(clusterer.clusterCount.items(), key=operator.itemgetter(1), reverse=True))

    def testCluster2(self):
        csv = "meet_sampled_1000.csv"
        clusterer = GraphClusterer2()
        clusterer.cluster2(csv)
        f = open("out2_"+csv, 'w')
        for k,v in clusterer.clusterByGroup:
            f.write(str(k)+","+str(v)+"\n")
            print(k,",",v)
        f.close()
        print(sorted(clusterer.clusterCount.items(), key=operator.itemgetter(1), reverse=True))

    def runTest(self):
        self.testLabel()
        print()
        self.testDensity()
        print()
        self.testAttractiveness()
        print()
        self.testIsInterInterested()
        print()
        self.testIsMergeable()
        print()
        self.testRemoveEdge()
        print()
        self.testMerge()
        print()
        self.testLoad()
        print()
        #self.testCluster()
        print()
        self.testCluster2()


gcTest = GraphClusterer2Test()
gcTest.runTest()
