
def get_input():
    return int(input())

def calculate_total_cost(meals_ordered):
    total_cost = meals_ordered * 800
    return total_cost

def calculate_discount(meals_ordered):
    discount = meals_ordered // 15 * 200
    return discount

def calculate_amount_paid(meals_ordered):
    total_cost = calculate_total_cost(meals_ordered)
    discount = calculate_discount(meals_ordered)
    amount_paid = total_cost - discount
    return amount_paid

def calculate_amount_received(meals_ordered):
    discount = calculate_discount(meals_ordered)
    amount_received = discount
    return amount_received

def main():
    meals_ordered = get_input()
    amount_paid = calculate_amount_paid(meals_ordered)
    amount_received = calculate_amount_received(meals_ordered)
    print(amount_paid - amount_received)

if __name__ == '__main__':
    main()

