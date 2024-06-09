
n, m = map(int, input().split())
candies = [list(map(int, input().split())) for _ in range(m)]

def calculate_time(start):
    time = 0
    for candy in candies:
        time += min(abs(candy[0] - start), n - abs(candy[0] - start)) + min(abs(candy[1] - candy[0]), n - abs(candy[1] - candy[0]))
    return time

for i in range(1, n+1):
    print(calculate_time(i), end=" ")
