
def get_available_mb(x, n, p):
    # Initialize a list to store the number of megabytes available in each month
    available_mb = [x] * (n + 1)

    # Loop through the list of megabytes spent in each month
    for i in range(n):
        # Subtract the number of megabytes spent in the current month from the total available megabytes
        available_mb[i + 1] = available_mb[i] - p[i]

    # Return the number of megabytes available in the next month
    return available_mb[-1]

def main():
    # Read the input from stdin
    x = int(input())
    n = int(input())
    p = [int(i) for i in input().split()]

    # Call the function to get the number of megabytes available in the next month
    available_mb = get_available_mb(x, n, p)

    # Print the output to stdout
    print(available_mb)

if __name__ == '__main__':
    main()

