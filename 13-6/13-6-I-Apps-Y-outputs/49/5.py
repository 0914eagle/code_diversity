
def calculate_time(distance, speed):
    return distance / speed

def check_arrival_time(distance, time, speed):
    required_time = calculate_time(distance, speed)
    if required_time <= time:
        return "Yes"
    else:
        return "No"

def main():
    distance, time, speed = map(int, input().split())
    print(check_arrival_time(distance, time, speed))

if __name__ == '__main__':
    main()

