import datetime
import json

class Stress:
    def __init__(self,path):
        self.stress_data = []
        self.daily_stress = {}
        self.path = path
        file = open(self.path)
        stress_json = json.load(file)
        switch = {5:1, 4:2, 1:3, 2:4, 3:5}
        
        for item in stress_json:
            try:
                buf = item["level"]
            except KeyError:
                continue
            
            form = {"level": None, "time": None}
            form["level"] = switch[int(item["level"])]
            form["time"] = item["resp_time"]
            self.stress_data.append(form)

        for i in range(len(self.stress_data)):
            j = datetime.date.fromtimestamp(int(self.stress_data[i]["time"])).strftime('%d-%m-%Y')

            try:
                buf = self.daily_stress[j]
            except KeyError:
                self.daily_stress[j] = -1

            self.daily_stress[j] = max(self.stress_data[i]["level"],self.daily_stress[j])


    def get_daily_stress(self):
        return self.daily_stress

    def get_summary(self):
        
        print("No of data points available: ",len(self.daily_stress))
        cnt = 0
        Sum = 0
        for key in self.daily_stress:
            cnt += 1
            Sum += self.daily_stress[key]

        print("Average stress Level: ", Sum/cnt)



    