
def get_free_desserts(price):
    max_free_desserts = 0
    possible_bills = []
    for beverage_price in range(1, price):
        for main_dish_price in range(beverage_price + 1, price + 1):
            if beverage_price != main_dish_price and beverage_price % 10 != main_dish_price % 10 and beverage_price // 10 != main_dish_price // 10:
                possible_bills.append((beverage_price, main_dish_price))
                max_free_desserts += 1
                if max_free_desserts == 5000:
                    return max_free_desserts, possible_bills
    return max_free_desserts, possible_bills

