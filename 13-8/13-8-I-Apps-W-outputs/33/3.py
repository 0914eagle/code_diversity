
def get_min_price(n, c1, c2, visitors):
    # Initialize variables
    min_price = float('inf')
    groups = []

    # Iterate over all possible groups
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            # Check if the group has at least one adult
            if sum(visitors[i - 1:j]) >= 1:
                # Calculate the price of the group
                price = c1 + c2 * (j - i + 1) ** 2

                # Check if the price is lower than the current minimum price
                if price < min_price:
                    min_price = price
                    groups = [i, j]

    return min_price, groups

def main():
    # Read the input
    n, c1, c2 = map(int, input().split())
    visitors = list(map(int, input()))

    # Calculate the minimum price and groups
    min_price, groups = get_min_price(n, c1, c2, visitors)

    # Print the result
    print(min_price)

if __name__ == '__main__':
    main()

