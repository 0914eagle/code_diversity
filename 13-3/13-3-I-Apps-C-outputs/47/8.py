
def f1(T, N, breaks):
    # Sort the breaks in non-decreasing order
    breaks.sort()

    # Initialize the number of minutes spent on stage for each musician
    minutes_on_stage = [0] * N

    # Iterate through the breaks and assign minutes on stage
    for i in range(N):
        minutes_on_stage[i] = breaks[i]
        if i < N - 1:
            minutes_on_stage[i + 1] += breaks[i]

    # Return the number of minutes spent on stage for each musician
    return minutes_on_stage

def f2(T, N, breaks):
    # Initialize the number of minutes spent on stage for each musician
    minutes_on_stage = [0] * N

    # Iterate through the breaks and assign minutes on stage
    for i in range(N):
        minutes_on_stage[i] = T - breaks[i]

    # Return the number of minutes spent on stage for each musician
    return minutes_on_stage

if __name__ == '__main__':
    T, N = map(int, input().split())
    breaks = list(map(int, input().split()))
    print(*f1(T, N, breaks), sep='\n')

