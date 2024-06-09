
def get_input():
    return list(map(int, input().split()))

def calculate_time(distance, speed):
    return distance / speed

def check_time(meeting_time, travel_time):
    return meeting_time >= travel_time

def main():
    distance, meeting_time, speed = get_input()
    travel_time = calculate_time(distance, speed)
    print("Yes") if check_time(meeting_time, travel_time) else print("No")

if __name__ == '__main__':
    main()

