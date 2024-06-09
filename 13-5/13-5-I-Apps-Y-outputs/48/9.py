
def get_min_x(divisors):
    # Sort the divisors in ascending order
    divisors.sort()
    # Initialize the minimum possible x as the product of the first two divisors
    x = divisors[0] * divisors[1]
    # Iterate through the remaining divisors
    for i in range(2, len(divisors)):
        # Check if the current divisor is a divisor of x
        if x % divisors[i] != 0:
            # If it is not, return -1 as the input data is contradictory
            return -1
        # Otherwise, update x to be the product of the current divisor and the previous x
        x *= divisors[i]
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
        # Call the get_min_x function to find the minimum possible x
        x = get_min_x(divisors)
        # Print the answer
        print(x)

if __name__ == '__main__':
    main()

