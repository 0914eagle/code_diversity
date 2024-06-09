
def get_min_time(n, c, a, b):
    # Initialize the minimum time array
    min_time = [0] * (n + 1)

    # Loop through each floor
    for i in range(1, n + 1):
        # Loop through each possible previous floor
        for j in range(1, i + 1):
            # Calculate the time it takes to reach the current floor from the previous floor using the stairs
            stairs_time = a[j - 1] + min_time[j]

            # Calculate the time it takes to reach the current floor from the previous floor using the elevator
            elevator_time = c + b[j - 1] + min_time[j]

            # Update the minimum time array with the minimum of the two times
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

