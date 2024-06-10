
def divisibility_hack(b, d):
    # Initialize m to 1
    m = 1
    # Loop until m is valid or not found
    while True:
        # Calculate the reduction function for m
        f = (b ** m - 1) // (b - 1)
        # If f is divisible by d, m is valid
        if f % d == 0:
            return m
        # Otherwise, increment m and try again
        m += 1
    # If m is not found, return None
    return None

def main():
    # Read input
    b, d = map(int, input().split())
    # Check if divisibility hack is valid
    m = divisibility_hack(b, d)
    # Print output
    if m is None:
        print("no")
    else:
        print("yes")

if __name__ == '__main__':
    main()

