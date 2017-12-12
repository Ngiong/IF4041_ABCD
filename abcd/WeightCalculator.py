import pandas as pd

class WeightCalculator(object):

    #input dataframe yg ad kolom 'check-in time', 'location id', dan 'user
    def __init__(self,  data):
        self.rawDF= data.copy()

    def build(self, timeRange):
        self.secsDF = self.rawDF.copy()
        secs = self.secsDF['check-in time'].map(lambda x: self.dateTimeToSecs(x))
        self.secsDF['check-in time'] =  secs
        self.secsDF= self.secsDF.sort_values(['location id', 'check-in time'])
        self.secsDF= self.secsDF.reset_index(drop=True)

        adjTable = {}
        startIdx = 0
        endIdx = 1
        while(endIdx < len(self.secsDF.index)):
            if(self.secsDF['location id'][endIdx] == self.secsDF['location id'][startIdx]):
                while self.secsDF['check-in time'][endIdx] - self.secsDF['check-in time'][startIdx] > timeRange:
                    startIdx += 1
                for i in range(startIdx, endIdx):
                    node1 = min(self.secsDF['user'][i], self.secsDF['user'][endIdx])
                    node2 = max(self.secsDF['user'][i], self.secsDF['user'][endIdx])
                    if(node1 != node2):
                        if not ((node1, node2) in adjTable):
                            adjTable[(node1,node2)] = 0
                        adjTable[(node1, node2)] += 1

            else:
                startIdx = endIdx
            endIdx += 1

        self.graphDict = {'node 1':[], 'node 2':[], 'weight':[]}
        for i,j in adjTable:
            self.graphDict['node 1'].append(i)
            self.graphDict['node 2'].append(j)
            self.graphDict['weight'].append(adjTable[(i,j)])

        self.graphDF = pd.DataFrame(self.graphDict)
        self.graphDF.sort_values(['node 1', 'node 2'])

        return self.graphDF

    def getRawDF(self):
        return  self.rawDF

    def getSecsDF(self):
        return  self.secsDF

    def getGraphDF(self):
        return self.graphDF

    def dateTimeToSecs(self,dateTime):
        yyyy = int(dateTime[0:4])
        mm = int(dateTime[5:7])
        dd = int(dateTime[8:10])
        HH = int(dateTime[11:13])
        MM = int(dateTime[14:16])
        SS = int(dateTime[17:19])

        arrMonth = [0,31,59,90,120,151,181,212,243,273,304,334]

        secs = 0
        secs += yyyy*365*24*60*60 + ((yyyy+3)/4)*24*60*60
        secs += arrMonth[mm-1]*24*60*60
        if(yyyy%4 == 0 and mm > 2):
            secs += 24*60*60
        secs += (dd-1)*24*60*60
        secs += HH*60*60
        secs += MM*60
        secs += SS

        return secs;


