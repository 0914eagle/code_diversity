
def solve(N):
    # Initialize variables
    operations = 0
    currencies = [1, 6, 9]

    # Loop through the currencies and check if they can be used to withdraw N yen
    for currency in currencies:
        while N >= currency:
            N -= currency
            operations += 1

    return operations

