
def get_min_price(n, c_1, c_2, visitors):
    # Initialize variables
    min_price = float('inf')
    groups = []

    # Iterate over all possible group sizes
    for group_size in range(1, n + 1):
        # Initialize variables for this group size
        current_price = 0
        current_group = []

        # Iterate over all visitors
        for i in range(n):
            # If the visitor is part of the group
            if i < group_size:
                # Add the visitor to the group
                current_group.append(visitors[i])

                # Calculate the price for this group
                current_price += c_1 + c_2 * (group_size - 1) ** 2

        # If the group size is valid and the price is lower than the current minimum
        if len(current_group) == group_size and current_price < min_price:
            # Update the minimum price and groups
            min_price = current_price
            groups = [current_group]

    # Return the minimum price and groups
    return min_price, groups

def main():
    # Read the input
    n, c_1, c_2 = map(int, input().split())
    visitors = list(map(int, input()))

    # Get the minimum price and groups
    min_price, groups = get_min_price(n, c_1, c_2, visitors)

    # Print the minimum price
    print(min_price)

if __name__ == '__main__':
    main()

