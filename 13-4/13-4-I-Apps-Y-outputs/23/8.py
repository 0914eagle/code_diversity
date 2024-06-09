
def get_input():
    return int(input())

def calculate_total_cost(n):
    return n * 800

def calculate_discount(n):
    return n // 15 * 200

def calculate_amount_paid(n):
    return calculate_total_cost(n) - calculate_discount(n)

def calculate_amount_received(n):
    return calculate_discount(n)

def main():
    n = get_input()
    total_cost = calculate_total_cost(n)
    discount = calculate_discount(n)
    amount_paid = calculate_amount_paid(n)
    amount_received = calculate_amount_received(n)
    print(amount_paid - amount_received)

if __name__ == '__main__':
    main()

