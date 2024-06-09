
def calculate_time(distance, speed):
    return distance / speed

def check_time(planned_time, actual_time):
    return planned_time >= actual_time

def main():
    distance, planned_time, speed = map(int, input().split())
    actual_time = calculate_time(distance, speed)
    print("Yes") if check_time(planned_time, actual_time) else print("No")

if __name__ == '__main__':
    main()

