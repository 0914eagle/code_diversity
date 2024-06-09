
def get_input():
    return int(input())

def calculate_total_cost(n):
    return 800 * n

def calculate_discount(n):
    return 200 if n % 15 == 0 else 0

def calculate_amount_paid(n):
    return calculate_total_cost(n) - calculate_discount(n)

def calculate_amount_received(n):
    return calculate_discount(n)

def calculate_balance(n):
    return calculate_amount_paid(n) - calculate_amount_received(n)

def main():
    n = get_input()
    print(calculate_balance(n))

if __name__ == '__main__':
    main()

