
def get_start_time(current_time, duration):
    return (current_time + duration) % 24

def main():
    current_time, duration = map(int, input().split())
    start_time = get_start_time(current_time, duration)
    print(start_time)

if __name__ == '__main__':
    main()

