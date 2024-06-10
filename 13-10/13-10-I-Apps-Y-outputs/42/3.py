
def get_maximum_rent(a, b, m, sigma):
    # Initialize variables
    x = 1
    y = 1
    rent = a * x + b * y

    # Loop until theConstraints are satisfied
    while x + y <= m and 2 * x + y >= sigma:
        # Update the variables
        x += 1
        y += 1

        # Calculate the new rent
        rent = a * x + b * y

    # Return the maximum rent
    return rent

def main():
    # Read the input
    a, b = map(int, input().split())
    m, sigma = map(int, input().split())

    # Calculate the maximum rent
    rent = get_maximum_rent(a, b, m, sigma)

    # Print the output
    print(rent)

if __name__ == '__main__':
    main()

