
import datetime

current_time = input()
explosion_time = input()

current_time = datetime.datetime.strptime(current_time, '%H:%M:%S')
explosion_time = datetime.datetime.strptime(explosion_time, '%H:%M:%S')

desired_time = explosion_time - current_time
desired_time = desired_time.total_seconds()

print(datetime.timedelta(seconds=desired_time))

