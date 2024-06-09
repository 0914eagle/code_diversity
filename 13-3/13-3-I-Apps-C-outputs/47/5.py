
def f1(T, N, breaks):
    # Initialize variables
    schedule = [0] * N
    current_time = 0
    break_time = 0

    # Loop through each break
    for i in range(N):
        # Calculate the time the musician will spend on stage before going on the break
        schedule[i] = breaks[i] - current_time

        # Update the current time and break time
        current_time += breaks[i]
        break_time += breaks[i]

        # If the break time is greater than the concert length, return an error
        if break_time > T:
            return -1

    # Return the schedule
    return schedule

def f2(...):
    # Implement function 2 here
    pass

if __name__ == '__main__':
    T = int(input())
    N = int(input())
    breaks = list(map(int, input().split()))
    schedule = f1(T, N, breaks)
    print(*schedule)

