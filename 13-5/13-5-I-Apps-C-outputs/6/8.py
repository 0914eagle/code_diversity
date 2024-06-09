
def get_free_desserts(price):
    # Initialize variables
    max_free_desserts = 0
    possible_bills = []

    # Iterate over all possible beverage prices
    for beverage_price in range(1, price):
        # Iterate over all possible main dish prices
        for main_dish_price in range(beverage_price + 1, price + 1):
            # Check if the prices are mutually different
            if all(str(beverage_price) != str(main_dish_price)[i] for i in range(len(str(main_dish_price)))):
                # Check if the bill is not identical to any of Quido's previous bills
                if (beverage_price, main_dish_price) not in possible_bills:
                    possible_bills.append((beverage_price, main_dish_price))
                    max_free_desserts += 1

    # Return the maximum number of free desserts and the possible bills
    return max_free_desserts, possible_bills[:5000]

