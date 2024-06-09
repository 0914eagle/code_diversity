
def calculate_time(distance, speed):
    return distance / speed

def check_if_on_time(planned_time, actual_time):
    return planned_time >= actual_time

def main():
    distance, planned_time, speed = map(int, input().split())
    actual_time = calculate_time(distance, speed)
    if check_if_on_time(planned_time, actual_time):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

