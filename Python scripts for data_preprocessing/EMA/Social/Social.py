import json
import datetime
class Social:
    def __init__(self,path):
        self.social_data = {}
        file = open(path)
        social_json = json.load(file)
        for item in social_json:
            try:
                buf = item["number"]
            except KeyError:
                continue
            
            date = datetime.date.fromtimestamp(int(item["resp_time"])).strftime('%d-%m-%Y')
            self.social_data[date] = int(item["number"])

    def get_social_data(self):
        return self.social_data;

    def get_summary(self):
        print("No of data points: ",len(self.social_data))
        cnt = 0
        Sum = 0
        for key in self.social_data:
            cnt += 1
            Sum += self.social_data[key]

        print("Average social interaction Level: ", Sum/cnt)



