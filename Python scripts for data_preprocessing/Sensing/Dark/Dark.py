import pandas as pd
import numpy as np
import datetime

class Dark:
    def __init__(self,path):
        self.dark_time = {}
        data = pd.read_csv(path)
        timestamp = np.array(data.iloc[:,0:2].values)

        avg     = np.array((timestamp[:,1]+timestamp[:,0])/2)
        duration = np.array(timestamp[:,1]-timestamp[:,0])

        
        duration = np.resize(duration,(duration.size,1))
        
        for i in range(duration.size):
            date = datetime.date.fromtimestamp(avg[i]).strftime('%d-%m-%Y')
            try:
                buf = self.dark_time[date]
            except KeyError:
                self.dark_time[date] = 0

            self.dark_time[date] += int(duration[i])

        for key in self.dark_time:
            self.dark_time[key] = round(self.dark_time[key]/3600)

    def get_dark_duration(self):
        return self.dark_time


        

        