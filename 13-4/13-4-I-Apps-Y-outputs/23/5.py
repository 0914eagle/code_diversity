
def get_amount_paid(n):
    return 800 * n

def get_amount_paid_back(n):
    return 200 * (n // 15)

def get_amount_owed(n):
    return get_amount_paid(n) - get_amount_paid_back(n)

if __name__ == '__main__':
    n = int(input())
    print(get_amount_owed(n))

