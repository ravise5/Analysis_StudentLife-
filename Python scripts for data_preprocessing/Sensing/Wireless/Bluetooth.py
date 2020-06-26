import pandas as pd
import numpy as np 
import datetime

class Bluetooth:
    def __init__(self,path):
        self.no_ppl = {}
        df = pd.read_csv(path)
        timestamp = np.array(df.iloc[:,0:1].values)
        # print(timestamp)\
        count = 0

        date_prev = datetime.date.fromtimestamp(timestamp[0]).strftime('%d-%m-%Y')

        for i in range(timestamp.size):
            
            date = datetime.date.fromtimestamp(timestamp[i]).strftime('%d-%m-%Y')

            if(date != date_prev):
                count = 0
            
            count += 1

            self.no_ppl[date] = count 

            date_prev = date

    def get_no_ppl(self):
        return self.no_ppl;
