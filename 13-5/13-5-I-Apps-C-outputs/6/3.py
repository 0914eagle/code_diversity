
def get_free_desserts(price):
    # Initialize variables
    max_free_desserts = 0
    possible_bills = []

    # Iterate through all possible beverage prices
    for beverage_price in range(1, price):
        # Iterate through all possible main dish prices
        for main_dish_price in range(beverage_price + 1, price):
            # Check if the bill is not identical to any of Quido's previous bills
            if (beverage_price, main_dish_price) not in possible_bills:
                # Check if the price of the beverage is less than the price of the main dish
                if beverage_price < main_dish_price:
                    # Check if the prices listed on the bill cannot mutually use the same digit
                    if len(set(str(beverage_price) + str(main_dish_price))) == 2:
                        max_free_desserts += 1
                        possible_bills.append((beverage_price, main_dish_price))

    # Print the maximum number of free desserts and the possible bills
    print(max_free_desserts)
    for beverage_price, main_dish_price in possible_bills[:5000]:
        print(beverage_price, main_dish_price)

