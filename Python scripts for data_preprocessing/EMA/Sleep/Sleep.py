import datetime
import json

class Sleep:
    def __init__(self,path):
        file = open(path)
        self.sleep_hours = {}
        self.sleep_quality = {}
        sleep_json = json.load(file)
        duration = {"0":None,"1":3,"2":3.5,"3":4,"4":4.5,"5":5,"6":5.5,"7":6,"8":6.5,"9":7,"10":7.5,"11":8,"12":8.5,"13":9,"14":9.5,"15":10,"16":10.5,"17":11,"18":11.5,"19":12}

        for item in sleep_json:
            try:
                buf = item["hour"]
            except KeyError:
                continue
            date  = datetime.date.fromtimestamp(int(item["resp_time"])).strftime('%d-%m-%Y')
            self.sleep_hours[date] = duration[item["hour"]]
            self.sleep_quality[date] = int(item["rate"])

    def get_sleep_duration(self):
        return self.sleep_hours;

    def get_sleep_quality(self):
        return self.sleep_quality;

    def get_summary(self):
        print("No of data points:", len(self.sleep_hours))
        
