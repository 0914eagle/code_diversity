
def get_min_x(divisors):
    # Sort the divisors in ascending order
    divisors.sort()
    # Initialize the minimum possible x as the largest divisor
    x = divisors[-1]
    # Iterate through the divisors in descending order
    for d in divisors[-2::-1]:
        # If the current divisor is not a factor of the minimum possible x, return -1
        if x % d != 0:
            return -1
        # Otherwise, update the minimum possible x as the product of the current divisor and the current minimum possible x
        x = d * x
    # Return the minimum possible x
    return x

def main():
    # Read the number of queries
    t = int(input())
    # Iterate through the queries
    for _ in range(t):
        # Read the number of divisors
        n = int(input())
        # Read the list of divisors
        divisors = [int(x) for x in input().split()]
        # Find the minimum possible x
        x = get_min_x(divisors)
        # Print the answer
        print(x)

if __name__ == '__main__':
    main()

