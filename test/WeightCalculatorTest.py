from abcd.WeightCalculator import WeightCalculator
import pandas as pd

class WeightCalculatorTest(object):
    def test_dateTimeToSecs(self):
        date =[
                    '2007-02-28T23:59:59Z'
                    , '2007-03-01T00:00:00Z'
                    , '2008-02-28T23:59:59Z'
                    , '2008-03-01T00:00:00Z'
                    , '2008-03-01T00:00:01Z'
                    , '2008-03-01T00:01:00Z'
                    , '2008-03-01T01:00:00Z'
                    , '2008-03-02T00:00:00Z'
                    , '2008-04-01T00:00:00Z'
                    , '2009-03-01T00:00:00Z'
                ]
        for i in date:
            calculator = WeightCalculator(pd.DataFrame(date))
            print(calculator.dateTimeToSecs(i))

    def test_build(self):
        data = {'user' :[
                    1,3,2,1,2,3
                ],
                'check-in time' :[
                    '2008-03-01T00:00:00Z'
                    , '2008-03-01T00:00:01Z'
                    , '2008-03-01T00:01:00Z'
                    , '2008-03-01T01:00:00Z'
                    , '2008-03-02T00:00:00Z'
                    , '2008-04-01T00:00:00Z'
                ],
                'location id':[
                    1,3,2,3,2,2
                ]
               }
        df = pd.DataFrame(data=data)
        calculator = WeightCalculator(df)
        data = calculator.build(99999999999)
        print(calculator.rawDF)
        print(calculator.secsDF)
        print(calculator.graphDF)


    def run_test(self):
        self.test_dateTimeToSecs()
        self.test_build()

weightcalculatortest =  WeightCalculatorTest()
weightcalculatortest.run_test()

