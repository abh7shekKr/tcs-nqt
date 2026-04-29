# speed, distance and time

import math
distance = int(input("Enter distance : "))
time_in_minutes = int(input("Enter time : "))

if time_in_minutes < 1 or time_in_minutes > 60:
    print("error")
else:
    time_in_hours = time_in_minutes/60
    speed = math.floor(distance/time_in_hours)

    print(speed)