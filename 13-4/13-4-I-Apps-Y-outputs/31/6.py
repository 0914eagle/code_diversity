
def get_min_time(n, c, a, b):
    # Initialize the minimum time array
    min_time = [0] * (n + 1)
    # Loop through each floor
    for i in range(1, n + 1):
        # Loop through each possible move
        for j in range(1, n + 1):
            # Calculate the time using the stairs
            stairs_time = sum(a[k - 1] for k in range(min(i, j), max(i, j)))
            # Calculate the time using the elevator
            elevator_time = c + sum(b[k - 1] for k in range(min(i, j), max(i, j)))
            # Update the minimum time
            min_time[i] = min(min_time[i], min_time[j] + min(stairs_time, elevator_time))
    return min_time

def main():
    n, c = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(*get_min_time(n, c, a, b))

if __name__ == '__main__':
    main()

