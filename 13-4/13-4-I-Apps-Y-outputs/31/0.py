
def get_min_time(n, c, a, b):
    # Initialize the minimum time array
    min_time = [0] * (n + 1)

    # Loop through each floor
    for i in range(1, n + 1):
        # Get the minimum time to reach the current floor using the stairs
        stairs_time = min_time[i - 1] + a[i - 1]

        # Get the minimum time to reach the current floor using the elevator
        elevator_time = min_time[i - 1] + c + b[i - 1]

        # Compare the two times and set the minimum time for the current floor
        min_time[i] = min(stairs_time, elevator_time)

    return min_time

def main():
    n, c = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    min_time = get_min_time(n, c, a, b)
    print(*min_time)

if __name__ == '__main__':
    main()

