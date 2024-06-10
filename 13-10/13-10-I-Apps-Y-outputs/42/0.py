
def get_max_rent(a, b, m, sigma):
    # Initialize variables
    x = 1
    y = 1
    rent = a + b

    # Loop until the constraints are met
    while x + y <= m and 2 * x + y >= sigma:
        # Calculate the current rent
        current_rent = a * x + b * y

        # Check if the current rent is greater than the previous rent
        if current_rent > rent:
            rent = current_rent

        # Increment x and y
        x += 1
        y += 1

    # Return the maximum rent
    return rent

def main():
    # Read input
    a, b = map(int, input().split())
    m, sigma = map(int, input().split())

    # Call the get_max_rent function
    max_rent = get_max_rent(a, b, m, sigma)

    # Print the maximum rent
    print(max_rent)

if __name__ == '__main__':
    main()

