
def get_starting_time(current_time, hours_later):
    starting_time = current_time + hours_later
    return starting_time % 24

def main():
    current_time, hours_later = map(int, input().split())
    starting_time = get_starting_time(current_time, hours_later)
    print(starting_time)

if __name__ == '__main__':
    main()

