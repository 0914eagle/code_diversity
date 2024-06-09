
def get_starting_time(current_time, duration):
    return (current_time + duration) % 24

def main():
    current_time, duration = map(int, input().split())
    print(get_starting_time(current_time, duration))

if __name__ == '__main__':
    main()

