
def solve(a, b, c):
    # Calculate the maximum number of candies Alice can have after the division
    return max(a, b, c)

q = int(input())

for i in range(q):
    a, b, c = map(int, input().split())
    print(solve(a, b, c))

