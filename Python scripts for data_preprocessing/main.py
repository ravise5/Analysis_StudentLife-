from EMA.Stress.Stress import Stress
from EMA.Exercise.Exercise import Exercise
from EMA.Sleep.Sleep import Sleep
from EMA.Social.Social import Social
from Sensing.conversation.Calls import Calls
import pandas as pd



count = 0
first = True
# create objects of the classes
for i in range(6):
    for j in range(10):

        path_Stress = r"R:\3-2\datasets\Student_life_dataset\dataset\EMA\response\Stress\Stress_u%d%d.json"%(i,j)
        
        try:
            buf = open(path_Stress)
        except FileNotFoundError:
            continue

        combined = [] #dict to store features

        # Initialising the paths for exisiting files

        path_calls = r"R:\3-2\datasets\Student_life_dataset\dataset\sensing\conversation\conversation_u%d%d.csv"%(i,j)
        path_sleep = r"R:\3-2\datasets\Student_life_dataset\dataset\EMA\response\Sleep\Sleep_u%d%d.json"%(i,j)
        path_social = r"R:\3-2\datasets\Student_life_dataset\dataset\EMA\response\Social\Social_u%d%d.json"%(i,j)
        path_exercise = r"R:\3-2\datasets\Student_life_dataset\dataset\EMA\response\Exercise\Exercise_u%d%d.json"%(i,j)

        # Creating class objects

        stress = Stress(path_Stress)
        calls = Calls(path_calls)
        sleep = Sleep(path_sleep)
        social = Social(path_social)
        exercise = Exercise(path_exercise)

        # loading the data to dict.

        daily_stress = stress.get_daily_stress()
        exercise_data = exercise.get_exercise_data()
        sleep_quality = sleep.get_sleep_quality()
        sleep_hours = sleep.get_sleep_duration()
        social_data = social.get_social_data()
        no_calls = calls.get_calls_per_day()

        # combining the data from all features based on common timestamp i.e. date

        for key in daily_stress:
            if key in exercise_data:
                if key in sleep_hours:
                    if key in social_data:
                        if key in no_calls:
                            if key in sleep_quality:

                                form = {"No of calls":None,"Sleep hours":None,"Sleep quality":None,"Social":None,"Exercise":None,"Stress Level":None}
                                form["No of calls"] = no_calls[key]
                                form["Sleep hours"] = sleep_hours[key]
                                form["Sleep quality"] = sleep_quality[key]
                                form["Social"] = social_data[key]
                                form["Exercise"] = exercise_data[key]
                                form["Stress Level"] = daily_stress[key]
                                combined.append(form)

        

        df = pd.DataFrame(combined)

        

        
            

        df.to_csv("Stress.csv",mode = 'a' ,header=first)
        first = False
                                



 
        
# print(df)


# path = r"R:\3-2\qwe.json"
# buf = open(path)

