
def solve(n, divisors):
    # Sort the divisors in ascending order
    divisors.sort()

    # Initialize the minimum possible value of x as 1
    x = 1

    # Iterate through the divisors and find the minimum possible value of x
    for d in divisors:
        if x % d != 0:
            x *= d

    # If the last divisor is not equal to x, then the input data is contradictory
    if x != divisors[-1]:
        return -1
    else:
        return x

# Main function
t = int(input())
for _ in range(t):
    n = int(input())
    divisors = list(map(int, input().split()))
    print(solve(n, divisors))

