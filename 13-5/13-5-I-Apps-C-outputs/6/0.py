
def get_free_desserts(price):
    # Initialize variables
    total_bills = 0
    possible_bills = []

    # Iterate through all possible beverage prices
    for beverage_price in range(1, price + 1):
        # Iterate through all possible main dish prices
        for main_dish_price in range(beverage_price + 1, price + 1):
            # Check if the prices are mutually distinct
            if all(str(beverage_price) != str(main_dish_price)[i] for i in range(len(str(main_dish_price)))):
                total_bills += 1
                possible_bills.append((beverage_price, main_dish_price))

    # Sort the possible bills in ascending order
    possible_bills.sort()

    # Return the total number of possible bills and the first 5000 possible bills
    return total_bills, possible_bills[:5000]

