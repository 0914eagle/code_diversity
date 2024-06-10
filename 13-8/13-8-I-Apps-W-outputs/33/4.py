
def get_min_price(n, c_1, c_2):
    # Initialize variables
    price = 0
    group_size = 1
    group_cost = c_1

    # Iterate through the visitors
    for i in range(n):
        # If the current visitor is an adult, add them to the group
        if i % 2 == 0:
            group_size += 1
        # If the group size is full, calculate the cost of the group and add it to the total price
        elif group_size == 2:
            price += group_cost
            group_size = 1
            group_cost = c_1 + c_2 * (group_size - 1) ** 2
        # If the group size is not full, calculate the cost of the group and add it to the total price
        else:
            price += group_cost
            group_size += 1
            group_cost = c_1 + c_2 * (group_size - 1) ** 2

    # Add the cost of the last group
    price += group_cost

    return price

def main():
    n, c_1, c_2 = map(int, input().split())
    visitors = list(map(int, input()))
    price = get_min_price(n, c_1, c_2)
    print(price)

if __name__ == '__main__':
    main()

