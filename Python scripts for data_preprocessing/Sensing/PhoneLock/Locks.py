import pandas as pd 
import numpy as np 
import datetime

class Locks:
    def __init__(self,path):
        self.locks_duration = {}
        df = pd.read_csv(path)
        timestamp = np.array(df.iloc[:,0:2].values)
        avg     = np.array((timestamp[:,1]+timestamp[:,0])/2)
        duration = np.array(timestamp[:,1]-timestamp[:,0])

        duration = np.resize(duration,(duration.size,1))
        
        for i in range(duration.size):
            date = datetime.date.fromtimestamp(avg[i]).strftime('%d-%m-%Y')

            try:
                buf = self.locks_duration[date]
            except KeyError:
                self.locks_duration[date] = 0

            self.locks_duration[date] += int(duration[i])

        for key in self.locks_duration:
            self.locks_duration[key] = round(self.locks_duration[key]/3600)

    def get_locks_duration(self):
        return self.locks_duration



