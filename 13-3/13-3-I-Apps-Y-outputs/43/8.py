
def solve(N):
    count = 0
    for i in range(1, N+1):
        if i % 2 != 0 and len(list(filter(lambda x: i % x == 0, range(1, int(i**0.5) + 1)))) == 8:
            count += 1
    return count

