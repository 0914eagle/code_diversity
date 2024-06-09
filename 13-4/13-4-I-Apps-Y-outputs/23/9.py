
def calculate_total_cost(num_meals):
    total_cost = 800 * num_meals
    return total_cost

def calculate_refund(num_meals):
    refund = 200 * (num_meals // 15)
    return refund

def calculate_balance(num_meals):
    total_cost = calculate_total_cost(num_meals)
    refund = calculate_refund(num_meals)
    balance = total_cost - refund
    return balance

if __name__ == '__main__':
    num_meals = int(input())
    balance = calculate_balance(num_meals)
    print(balance)

