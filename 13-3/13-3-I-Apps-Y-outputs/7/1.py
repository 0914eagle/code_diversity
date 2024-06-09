
import datetime

current_time = input()
explosion_time = input()

current_time = datetime.datetime.strptime(current_time, '%H:%M:%S')
explosion_time = datetime.datetime.strptime(explosion_time, '%H:%M:%S')

desired_time = explosion_time - current_time

print(desired_time)

