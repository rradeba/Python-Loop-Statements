#task 1 

import random
moods = ["Happy", "Sad", "Angry", "Content", "Restful"]
week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for i in range(7):
    print("On " + week_days[i]+ " you are feeling " + random.choice(moods))





