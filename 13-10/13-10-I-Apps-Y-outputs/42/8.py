
def get_maximum_rent(a, b, m, sigma):
    # Initialize variables
    x = 1
    y = 1
    R = a + b

    # Loop until the constraints are met
    while x + y <= m and 2 * x + y >= sigma:
        # Calculate the current rent
        current_rent = a * x + b * y

        # If the current rent is greater than the previous rent, update the variables
        if current_rent > R:
            R = current_rent
            x += 1
            y += 1

    # Return the maximum rent
    return R

def main():
    # Read the input
    a, b = map(int, input().split())
    m, sigma = map(int, input().split())

    # Call the function and print the result
    print(get_maximum_rent(a, b, m, sigma))

if __name__ == '__main__':
    main()

