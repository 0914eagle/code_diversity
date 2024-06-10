
def get_min_price(n, c_1, c_2):
    # Initialize variables
    min_price = float('inf')
    group_size = 0

    # Iterate through all possible group sizes
    for i in range(1, n + 1):
        # Calculate the price of the ticket for the current group size
        price = c_1 + c_2 * (i - 1) ** 2

        # Check if the price is less than the current minimum price
        if price < min_price:
            min_price = price
            group_size = i

    return min_price

def get_groups(n, group_size):
    # Initialize variables
    groups = []
    current_group = []

    # Iterate through all visitors
    for i in range(n):
        # If the current visitor is an adult, add them to the current group
        if i % 2 == 0:
            current_group.append(i)

        # If the current group is full or it is the last visitor, add the current group to the list of groups and start a new group
        if len(current_group) == group_size or i == n - 1:
            groups.append(current_group)
            current_group = []

    return groups

def get_total_price(groups, c_1, c_2):
    # Initialize variables
    total_price = 0

    # Iterate through all groups
    for group in groups:
        # Calculate the price of the ticket for the current group
        price = c_1 + c_2 * (len(group) - 1) ** 2
        total_price += price

    return total_price

def main():
    # Read input
    n, c_1, c_2 = map(int, input().split())
    visitors = list(map(int, input()))

    # Find the minimum price and the corresponding group size
    min_price = get_min_price(n, c_1, c_2)
    group_size = min_price // (c_1 + c_2)

    # Create the list of groups
    groups = get_groups(n, group_size)

    # Calculate the total price
    total_price = get_total_price(groups, c_1, c_2)

    # Print the minimum price
    print(total_price)

if __name__ == '__main__':
    main()

