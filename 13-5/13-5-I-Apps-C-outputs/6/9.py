
def get_free_desserts(price):
    total_bills = 0
    possible_bills = []
    for beverage in range(1, price):
        for main_dish in range(beverage + 1, price):
            if beverage != main_dish and beverage % 10 != main_dish % 10 and beverage // 10 != main_dish // 10:
                total_bills += 1
                possible_bills.append([beverage, main_dish])
    return total_bills, possible_bills[:5000]

