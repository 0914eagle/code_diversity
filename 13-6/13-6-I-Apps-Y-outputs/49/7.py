
def calculate_time(distance, speed):
    return distance / speed

def is_on_time(meeting_time, travel_time):
    return meeting_time >= travel_time

def main():
    distance, meeting_time, speed = map(int, input().split())
    travel_time = calculate_time(distance, speed)
    if is_on_time(meeting_time, travel_time):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

