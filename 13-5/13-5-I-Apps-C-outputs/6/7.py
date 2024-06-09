
def get_free_desserts(price):
    # Initialize variables
    max_free_desserts = 0
    possible_bills = []

    # Iterate through all possible beverage prices
    for beverage_price in range(1, price):
        # Iterate through all possible main dish prices
        for main_dish_price in range(beverage_price + 1, price):
            # Check if the prices are mutually exclusive
            if all(digit not in str(beverage_price) for digit in str(main_dish_price)) and all(digit not in str(main_dish_price) for digit in str(beverage_price)):
                # Check if the total price is equal to the fixed price
                total_price = beverage_price + main_dish_price
                if total_price == price:
                    # Add the bill to the list of possible bills
                    possible_bills.append((beverage_price, main_dish_price))
                    max_free_desserts += 1

    # Return the maximum number of free desserts and the list of possible bills
    return max_free_desserts, possible_bills[:5000]

