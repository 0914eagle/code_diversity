
def get_accommodation_fee(n, k, x, y):
    fee = 0
    for i in range(n):
        if i < k:
            fee += x
        else:
            fee += y
    return fee

def main():
    n, k, x, y = map(int, input().split())
    fee = get_accommodation_fee(n, k, x, y)
    print(fee)

if __name__ == '__main__':
    main()

