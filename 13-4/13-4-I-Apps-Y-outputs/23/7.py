
def get_total_cost(n):
    return 800 * n

def get_discount(n):
    return 200 * (n // 15)

def get_amount_paid(n):
    return get_total_cost(n) - get_discount(n)

def get_amount_received(n):
    return get_discount(n)

if __name__ == '__main__':
    n = int(input())
    print(get_amount_paid(n))

