
def get_current_time(current_time):
    return current_time

def get_start_time(current_time, hours_to_add):
    return (current_time + hours_to_add) % 24

def main():
    current_time, hours_to_add = map(int, input().split())
    start_time = get_start_time(current_time, hours_to_add)
    print(start_time)

if __name__ == '__main__':
    main()

