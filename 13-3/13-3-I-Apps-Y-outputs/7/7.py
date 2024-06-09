
import datetime

current_time = input()
explosion_time = input()

current_time = datetime.datetime.strptime(current_time, '%H:%M:%S')
explosion_time = datetime.datetime.strptime(explosion_time, '%H:%M:%S')

time_diff = explosion_time - current_time

desired_time = current_time + datetime.timedelta(seconds=time_diff.total_seconds())

print(desired_time.strftime('%H:%M:%S'))

