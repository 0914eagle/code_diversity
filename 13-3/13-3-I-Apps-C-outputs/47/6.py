
def f1(T, N, breaks):
    # Sort the breaks in non-decreasing order
    breaks.sort()

    # Initialize the number of minutes each musician will spend on stage
    minutes_on_stage = [0] * N

    # Iterate through the breaks and assign minutes to each musician
    for i in range(N):
        # Calculate the number of minutes the current musician will spend on stage
        minutes_on_stage[i] = breaks[i] - breaks[i - 1] if i > 0 else breaks[i]

    return minutes_on_stage

def f2(T, N, breaks):
    # Initialize the number of minutes each musician will spend on stage
    minutes_on_stage = [0] * N

    # Iterate through the breaks and assign minutes to each musician
    for i in range(N):
        # Calculate the number of minutes the current musician will spend on stage
        minutes_on_stage[i] = T - breaks[i] if i == N - 1 else breaks[i + 1] - breaks[i]

    return minutes_on_stage

if __name__ == '__main__':
    T, N = map(int, input().split())
    breaks = list(map(int, input().split()))
    print(*f1(T, N, breaks), sep='\n')

