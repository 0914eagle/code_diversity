
def f1(N, M, conditions):
    # Initialize the number of ways to paint the squares
    num_ways = 1

    # Loop through each condition
    for l, r, x in conditions:
        # Calculate the number of ways to paint the squares in this range
        num_ways *= comb(N, x)

        # Update the number of ways to paint the squares after this range
        num_ways %= 1000000007

    return num_ways

def f2(N, M, conditions):
    # Initialize the number of ways to paint the squares
    num_ways = 1

    # Loop through each condition
    for l, r, x in conditions:
        # Calculate the number of ways to paint the squares in this range
        num_ways *= comb(N, x)

        # Update the number of ways to paint the squares after this range
        num_ways %= 1000000007

    return num_ways

def comb(n, k):
    # Calculate the binomial coefficient
    if k > n - k:
        k = n - k
    if k == 0:
        return 1
    result = 1
    for i in range(1, k + 1):
        result *= n - i + 1
        result //= i
    return result

if __name__ == '__main__':
    N, M = map(int, input().split())
    conditions = []
    for _ in range(M):
        l, r, x = map(int, input().split())
        conditions.append((l, r, x))
    print(f1(N, M, conditions))
    print(f2(N, M, conditions))

