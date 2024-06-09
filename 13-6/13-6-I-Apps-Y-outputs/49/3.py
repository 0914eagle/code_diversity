
def get_distance_time(distance, speed):
    return distance / speed

def get_time_difference(planned_time, actual_time):
    return abs(planned_time - actual_time)

def will_he_arrive_in_time(distance, speed, planned_time):
    actual_time = get_distance_time(distance, speed)
    time_difference = get_time_difference(planned_time, actual_time)
    if time_difference == 0:
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    distance, planned_time, speed = map(int, input().split())
    print(will_he_arrive_in_time(distance, speed, planned_time))

