
def f1(T, N, breaks):
    # Initialize variables
    schedule = [0] * N
    current_time = 0
    break_time = 0

    # Loop through each musician
    for i in range(N):
        # Calculate the time the musician will spend on stage
        stage_time = T - breaks[i]

        # Check if the musician will be on stage at the same time as another musician
        if current_time + stage_time > break_time:
            # Calculate the time the musician will spend on stage before the break
            schedule[i] = break_time - current_time

            # Update the current time and break time
            current_time = break_time
            break_time += breaks[i]
        else:
            # Calculate the time the musician will spend on stage before the next break
            schedule[i] = stage_time

            # Update the current time
            current_time += stage_time

    return schedule

def f2(T, N, breaks):
    # Initialize variables
    schedule = [0] * N
    current_time = 0
    break_time = 0

    # Loop through each musician
    for i in range(N):
        # Calculate the time the musician will spend on stage
        stage_time = T - breaks[i]

        # Check if the musician will be on stage at the same time as another musician
        if current_time + stage_time > break_time:
            # Calculate the time the musician will spend on stage before the break
            schedule[i] = break_time - current_time

            # Update the current time and break time
            current_time = break_time
            break_time += breaks[i]
        else:
            # Calculate the time the musician will spend on stage before the next break
            schedule[i] = stage_time

            # Update the current time
            current_time += stage_time

    return schedule

if __name__ == '__main__':
    T, N = map(int, input().split())
    breaks = list(map(int, input().split()))
    schedule = f1(T, N, breaks)
    print(*schedule)

