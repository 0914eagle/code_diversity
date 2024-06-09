
def get_free_desserts(price):
    # Initialize a list to store the possible bills
    bills = []
    
    # Loop through all possible beverage prices
    for beverage_price in range(1, price):
        # Loop through all possible main dish prices
        for main_dish_price in range(beverage_price + 1, price):
            # Check if the prices are mutually distinct
            if all(str(beverage_price) != str(main_dish_price)[i] for i in range(len(str(main_dish_price)))):
                # Add the bill to the list
                bills.append((beverage_price, main_dish_price))
    
    # Return the list of possible bills
    return bills

