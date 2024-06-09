
def get_starting_time(current_time, hours_later):
    return (current_time + hours_later) % 24

def main():
    current_time, hours_later = map(int, input().split())
    print(get_starting_time(current_time, hours_later))

if __name__ == '__main__':
    main()

