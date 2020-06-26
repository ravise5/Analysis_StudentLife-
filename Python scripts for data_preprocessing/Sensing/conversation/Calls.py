import pandas as pd
import numpy as np
import datetime

class Calls:
    def __init__(self,path):
        self.path = path
        self.call_dates = []
        self.calls_per_day = {}
        data = pd.read_csv(self.path)
        calls = np.array(data.iloc[:,0:2].values)
        calls_timestamp = np.array((calls[:,1]+calls[:,0])/2)
        calls_timestamp  = np.resize(calls_timestamp,(calls_timestamp.size,1))

        for i in range (calls_timestamp.size):
            self.call_dates.append(datetime.date.fromtimestamp(int(calls[i])).strftime('%d-%m-%Y'))
        
        count = 0
        n = len(self.call_dates)-1

        for i in range(len(self.call_dates)):
            count = count + 1
            self.calls_per_day[self.call_dates[i]] = count
            if(i<n):
                if(self.call_dates[i]!=self.call_dates[i+1]):
                    count = 0;

    def get_calls_per_day(self):
        return self.calls_per_day

    def get_summary(self):
        print("\nData Summary:\n")
        print("No of data points available: ",len(self.calls_per_day))
        cnt = 0
        Sum = 0
        for key in self.calls_per_day:
            cnt += 1
            Sum += self.calls_per_day[key]

        print("Average no of calls per day: ",Sum/cnt)
        



