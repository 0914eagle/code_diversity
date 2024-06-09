
def f1(T, N, breaks):
    # Sort the breaks in non-decreasing order
    breaks.sort()

    # Initialize the number of minutes each musician will spend on stage
    on_stage = [0] * N

    # Iterate through the breaks and schedule them
    for i in range(N):
        # Calculate the number of minutes the musician will spend on stage before the break
        on_stage[i] = breaks[i] - breaks[i - 1] if i > 0 else breaks[i]

    return on_stage

def f2(T, N, breaks):
    # Initialize the number of minutes each musician will spend on stage
    on_stage = [0] * N

    # Iterate through the breaks and schedule them
    for i in range(N):
        # Calculate the number of minutes the musician will spend on stage before the break
        on_stage[i] = breaks[i] - breaks[i - 1] if i > 0 else breaks[i]

    return on_stage

if __name__ == '__main__':
    T, N = map(int, input().split())
    breaks = list(map(int, input().split()))
    on_stage = f1(T, N, breaks)
    print(*on_stage)

