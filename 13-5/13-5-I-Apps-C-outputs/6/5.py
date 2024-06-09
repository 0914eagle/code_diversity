
def get_free_desserts(price):
    # Initialize a list to store the possible bills
    bills = []
    
    # Iterate over the possible prices of the beverage
    for beverage_price in range(1, price):
        # Get the possible prices of the main dish
        main_dish_prices = [price - beverage_price, price - beverage_price - 1]
        
        # Iterate over the possible prices of the main dish
        for main_dish_price in main_dish_prices:
            # Check if the prices of the beverage and main dish are different
            if beverage_price != main_dish_price:
                # Check if the prices of the beverage and main dish do not share any digits
                if len(set(str(beverage_price)) & set(str(main_dish_price))) == 0:
                    # Add the bill to the list of possible bills
                    bills.append((beverage_price, main_dish_price))
    
    # Return the list of possible bills
    return bills

