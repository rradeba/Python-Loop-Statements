#task 1 

import random
moods = ["Happy", "Sad", "Angry", "Content", "Restful"]
week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
time_of_day = ["morning", "afternoon", "evening"]
for d in range(7):
    for t in range(3):
        print("On " + week_days[d] +" "+ time_of_day[t] + " you were feeling " + random.choice(moods))
