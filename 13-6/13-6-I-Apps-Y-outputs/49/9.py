
def get_input():
    return list(map(int, input().split()))

def calculate_time(distance, speed):
    return distance / speed

def is_in_time(meeting_time, travel_time):
    return meeting_time >= travel_time

def main():
    distance, meeting_time, speed = get_input()
    travel_time = calculate_time(distance, speed)
    if is_in_time(meeting_time, travel_time):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

