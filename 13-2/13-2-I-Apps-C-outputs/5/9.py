
def f1(n, r, m):
    # Initialize variables
    tricks = []
    expected_time = 0

    # Loop through each trick
    for i in range(m):
        # Read input for each trick
        t, p, d = map(int, input().split())

        # Add trick to list of tricks
        tricks.append((t, p, d))

        # Calculate expected time for each trick
        expected_time += t * p + d * (1 - p)

    # Calculate expected time for the entire route
    expected_time += n

    # Return expected time
    return expected_time

def f2(n, r, m):
    # Initialize variables
    tricks = []
    expected_time = 0

    # Loop through each trick
    for i in range(m):
        # Read input for each trick
        t, p, d = map(int, input().split())

        # Add trick to list of tricks
        tricks.append((t, p, d))

        # Calculate expected time for each trick
        expected_time += t * p + d * (1 - p)

    # Calculate expected time for the entire route
    expected_time += n

    # Return expected time
    return expected_time

if __name__ == '__main__':
    n = int(input())
    r = int(input())
    m = int(input())

    print(f1(n, r, m))
    print(f2(n, r, m))

