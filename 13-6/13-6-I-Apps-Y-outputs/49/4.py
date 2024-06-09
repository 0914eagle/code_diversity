
def get_distance_time(distance, speed):
    return distance / speed

def is_in_time(distance, time, speed):
    return get_distance_time(distance, speed) <= time

if __name__ == '__main__':
    distance, time, speed = map(int, input().split())
    print("Yes") if is_in_time(distance, time, speed) else print("No")

