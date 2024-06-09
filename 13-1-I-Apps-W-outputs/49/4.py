
def solve(N):
    counter = 0
    for i in range(N-1, 0, -1):
        if N % i == 0:
            break
        counter += 1
    return counter

