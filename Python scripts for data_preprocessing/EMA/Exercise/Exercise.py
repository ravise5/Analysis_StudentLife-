import datetime
import json
class Exercise:
    def __init__(self,path):
        self.exercise_data = {}
        file = open(path)
        exercise_json = json.load(file)

        time = {"1":0,"2":15,"3":30,"4":60,"5":90}

        for item in exercise_json:
            try:
                buf = item["have"]
            except KeyError:
                continue
            date = datetime.date.fromtimestamp(int(item["resp_time"])).strftime('%d-%m-%Y')
            try:
                self.exercise_data[date]= time[item["exercise"]]+time[item["walk"]]
            except KeyError:
                self.exercise_data[date]= time[item["exercise"]]

    def get_exercise_data(self):
        return self.exercise_data