
def get_min_time(n, c, a, b):
    # Initialize the minimum time array
    min_time = [0] * (n + 1)
    
    # Loop through each floor
    for i in range(1, n + 1):
        # Loop through each possible move
        for j in range(1, n + 1):
            # Calculate the time required to move from the current floor to the destination floor
            time_required = c + sum(b[j - 1:i]) if j < i else sum(a[j - 1:i])
            
            # Update the minimum time if the current time is less than the previous minimum time
            if min_time[i] > min_time[j] + time_required:
                min_time[i] = min_time[j] + time_required
    
    return min_time

def main():
    n, c = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    min_time = get_min_time(n, c, a, b)
    print(*min_time)

if __name__ == '__main__':
    main()

