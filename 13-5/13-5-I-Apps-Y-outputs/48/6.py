
def get_min_x(divisors):
    # Sort the divisors in ascending order
    divisors.sort()
    # Initialize the minimum possible value of x
    x = 1
    # Iterate through the divisors
    for d in divisors:
        # If the current divisor is not a factor of x, return -1
        if x % d != 0:
            return -1
        # Otherwise, update x to be the least common multiple of x and d
        x = x * d // gcd(x, d)
    # Return the minimum possible value of x
    return x

def main():
    # Read the number of queries
    t = int(input())
    # Iterate through the queries
    for _ in range(t):
        # Read the number of divisors
        n = int(input())
        # Read the divisors
        divisors = [int(x) for x in input().split()]
        # Find the minimum possible value of x
        x = get_min_x(divisors)
        # Print the answer
        print(x)

if __name__ == '__main__':
    main()

