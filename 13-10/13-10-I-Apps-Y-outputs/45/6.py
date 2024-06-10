
def get_discount(items):
    # Find the item with the highest price
    highest_price_item = max(items)

    # Get the index of the highest price item
    highest_price_index = items.index(highest_price_item)

    # Apply the discount to the highest price item
    discounted_price = highest_price_item // 2

    # Remove the highest price item from the list
    items.pop(highest_price_index)

    # Add the discounted price to the list
    items.append(discounted_price)

    # Return the total amount
    return sum(items)

def main():
    # Read the number of items and their prices from stdin
    num_items = int(input())
    prices = [int(input()) for _ in range(num_items)]

    # Get the discounted price
    discounted_price = get_discount(prices)

    # Print the total amount
    print(discounted_price)

if __name__ == '__main__':
    main()

