
def get_minimum_price(n, c_1, c_2):
    # Initialize variables
    min_price = float('inf')
    groups = []

    # Iterate over all possible groups
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i + j == n:
                # Calculate the price of the current group
                price = c_1 + c_2 * (i - 1) ** 2

                # Check if the price is lower than the current minimum price
                if price < min_price:
                    min_price = price
                    groups = [(i, j)]
                elif price == min_price:
                    groups.append((i, j))

    return min_price

def main():
    # Read the input
    n, c_1, c_2 = map(int, input().split())
    visitors = list(map(int, input()))

    # Calculate the minimum price
    min_price = get_minimum_price(n, c_1, c_2)

    # Print the result
    print(min_price)

if __name__ == '__main__':
    main()

