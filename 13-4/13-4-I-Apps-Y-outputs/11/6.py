
def convert_to_24_hour(hour):
    return str(hour) if hour < 10 else str(hour)

def get_starting_time(current_time, contest_duration):
    starting_time = current_time + contest_duration
    return convert_to_24_hour(starting_time)

def main():
    current_time, contest_duration = map(int, input().split())
    print(get_starting_time(current_time, contest_duration))

if __name__ == '__main__':
    main()

