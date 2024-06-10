
def get_available_megabytes(x, n, months):
    # Initialize a list to store the available megabytes for each month
    available_megabytes = [x] * (n + 1)

    # Loop through the months and calculate the available megabytes for each month
    for i in range(n):
        available_megabytes[i + 1] = available_megabytes[i] - months[i]

    # Return the available megabytes for the last month
    return available_megabytes[-1]

def main():
    # Read the input
    x = int(input())
    n = int(input())
    months = [int(input()) for _ in range(n)]

    # Calculate the available megabytes for the last month
    available_megabytes = get_available_megabytes(x, n, months)

    # Print the output
    print(available_megabytes)

if __name__ == '__main__':
    main()

