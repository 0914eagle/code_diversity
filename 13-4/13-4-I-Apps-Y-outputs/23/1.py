
def get_total_cost(n):
    return 800 * n

def get_refund(n):
    return 200 if n % 15 == 0 else 0

def get_amount_paid(n):
    return get_total_cost(n) - get_refund(n)

def main():
    n = int(input())
    print(get_amount_paid(n))

if __name__ == '__main__':
    main()

