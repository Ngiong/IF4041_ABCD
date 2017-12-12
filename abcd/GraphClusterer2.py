import operator
import csv

class GraphClusterer2(object):

    def label(self,x):
        ret = x
        parent = self.labelTree[x]
        while parent >= 0 :
            ret = parent
            parent = self.labelTree[ret]
        return ret

    def density(self,x):
        root = self.label(x)
        ret = self.clusterSum[root]/self.clusterCount[root]
        return ret

    def attractiveness(self,x,y):
        xLabel = self.label(x)
        yLabel = self.label(y)
        if(xLabel != yLabel):
            minNode, maxNode = min(xLabel, yLabel), max(xLabel, yLabel)
            ret = self.attractivenessSum[(minNode, maxNode)] / (self.clusterCount[minNode] * self.clusterCount[maxNode])
            return ret
        else:
            return -1

    def isInterInterested(self,x,y):
        xLabel = self.label(x)
        yLabel = self.label(y)

        if(xLabel != yLabel):
            minNode, maxNode = min(xLabel, yLabel), max(xLabel, yLabel)
            q = self.attractivenessCount[minNode, maxNode]
            if (q >= self.clusterCount[minNode] and q >= self.clusterCount[maxNode]):
                return True
            else:
                return False
        else:
            return -1

    def isMergeable(self, x, y):
        xLabel = self.label(x)
        yLabel = self.label(y)
        minNode, maxNode = min(xLabel, yLabel), max(xLabel, yLabel)
        if (minNode,maxNode) in self.edge:
            return self.isInterInterested(x, y) == True and self.attractiveness(x, y) >= self.density(x) + self.density(y)
        else:
            return False

    def removeEdge(self,x, y):
        xLabel = self.label(x)
        yLabel = self.label(y)
        minNode, maxNode = min(xLabel, yLabel), max(xLabel, yLabel)
        self.edge.pop((minNode, maxNode))
        self.attractivenessSum.pop((minNode, maxNode))
        self.attractivenessCount.pop((minNode, maxNode))

    def removeNode(self,x):
        xLabel = self.label(x)
        self.clusterSum.pop(x)
        self.clusterCount.pop(x)

    def merge(self,x, y):
        xLabel = self.label(x)
        yLabel = self.label(y)
        min1, max1 = min(xLabel, yLabel), max(xLabel, yLabel)
        self.removeEdge(min1, max1)

        for k in self.edge.copy():
            if k[0] == max1 or k[1] == max1:
                neighbor = -1
                if k[0] == max1:
                    neighbor = k[1]
                else:
                    neighbor = k[0]

                min2, max2 = min(min1, neighbor), max(min1, neighbor)
                if (min2,max2) in self.edge:
                   self.attractivenessCount[(min2,max2)] += self.attractivenessCount[k]
                   self.attractivenessSum[(min2, max2)] += self.attractivenessSum[k]
                else:
                    self.edge[(min2, max2)] = (min2, max2)
                    self.attractivenessCount[(min2, max2)] = self.attractivenessCount[k]
                    self.attractivenessSum[(min2, max2)] = self.attractivenessSum[k]
                self.removeEdge(k[0], k[1])

        self.labelTree[max1] = min1
        self.clusterSum[min1] += self.clusterSum[max1]
        self.clusterCount[min1] += self.clusterCount[max1]
        self.removeNode(max1)

    def load(self, csvFile):
        self.maxNode = -1
        self.edge = {}
        self.node = {}
        self.labelTree = {}
        self.clusterSum = {}
        self.clusterCount = {}
        self.attractivenessSum = {}
        self.attractivenessCount = {}
        filereader = csv.reader(open(csvFile), delimiter=",")
        for node1, node2, weight in filereader:
            min1, max1 = min(int(node1),int(node2)), max(int(node1),int(node2))
            self.edge[(min1, max1)] = (min1, max1)
            self.attractivenessSum[(min1, max1)] = int(weight)
            self.attractivenessCount[(min1, max1)] = 1

            if min1 in self.node:
                self.clusterSum[min1] += 1
            else:
                self.node[min1] = min1
                self.labelTree[min1] = -1
                self.clusterCount[min1] = 1
                self.clusterSum[min1] = 1

            if max1 in self.node:
                self.clusterSum[max1] += 1
            else:
                self.node[max1] = max1
                self.labelTree[max1] = -1
                self.clusterCount[max1] = 1
                self.clusterSum[max1] = 1


    def cluster(self, csvFile):
        print("load...")
        self.load(csvFile)
        print("clustering...")
        iter = 0
        changed = True
        while changed:
            iter += 1
            changed = False
            choosen = (-1,-1)
            for k1 in self.node:
                if self.labelTree[k1] == -1:
                    for k2 in self.node:
                        if self.labelTree[k2] == -1 and k1 != k2:
                            print("    [",iter,"]comparing cluster ", k2, " with ", k1, "...")
                            if(self.isMergeable(k1,k2)):
                                if choosen == (-1,-1):
                                    choosen = (k1,k2)
                                elif self.attractiveness(choosen[0],choosen[1]) < self.attractiveness(k1,k2):
                                    choosen = (k1,k2)
            if choosen != (-1,-1):
                self.merge(choosen[0], choosen[1])
                changed = True

        self.clusterDict = self.node.copy()
        for k in self.clusterDict:
            self.clusterDict[k] = self.label(k)

        self.clusterByNode= sorted(self.clusterDict.items(), key=operator.itemgetter(0))
        self.clusterByGroup= sorted(self.clusterDict.items(), key=operator.itemgetter(1))

    def cluster2(self, csvFile):
        print("load...")
        self.load(csvFile)
        print("clustering...")
        iter = 0
        changed = True
        while changed:
            iter += 1
            changed = False
            choosen = (-1, -1)
            for k in self.edge:
                k1 = self.label(k[0])
                k2 = self.label(k[1])
                if k1!=k2:
                    print("    [",iter,"]comparing cluster ", k1, " with ", k2, "...")
                    if (self.isMergeable(k1, k2)):
                        if choosen == (-1, -1):
                            choosen = (k1, k2)
                        elif self.attractiveness(choosen[0], choosen[1]) < self.attractiveness(k1, k2):
                            choosen = (k1, k2)
            if choosen != (-1,-1):
                self.merge(choosen[0], choosen[1])
                changed = True

        self.clusterDict = self.node.copy()
        for k in self.clusterDict:
            self.clusterDict[k] = self.label(k)

        self.clusterByNode= sorted(self.clusterDict.items(), key=operator.itemgetter(0))
        self.clusterByGroup= sorted(self.clusterDict.items(), key=operator.itemgetter(1))

