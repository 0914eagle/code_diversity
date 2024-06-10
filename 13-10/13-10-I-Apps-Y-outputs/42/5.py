
def get_maximum_rent(a, b, m, sigma):
    # Initialize variables
    x = 1
    y = 1
    rent = a * x + b * y

    # Loop until the rent is maximized
    while True:
        # Calculate the current rent
        rent = a * x + b * y

        # Check if the current rent is maximized
        if rent >= m * sigma:
            return rent

        # Increase the number of smartbulbs
        y += 1

        # Check if the number of smartbulbs exceeds the maximum
        if y > m:
            break

    # Loop until the rent is maximized
    while True:
        # Calculate the current rent
        rent = a * x + b * y

        # Check if the current rent is maximized
        if rent >= m * sigma:
            return rent

        # Increase the square footage
        x += 1

        # Check if the square footage exceeds the maximum
        if x > m:
            break

    # If the rent is not maximized, return -1
    return -1

def main():
    a, b = map(int, input().split())
    m, sigma = map(int, input().split())
    print(get_maximum_rent(a, b, m, sigma))

if __name__ == '__main__':
    main()

