
def get_current_time(current_time):
    return current_time

def get_starting_time(current_time, hours_to_add):
    return (current_time + hours_to_add) % 24

def main():
    current_time, hours_to_add = map(int, input().split())
    starting_time = get_starting_time(current_time, hours_to_add)
    print(starting_time)

if __name__ == '__main__':
    main()

