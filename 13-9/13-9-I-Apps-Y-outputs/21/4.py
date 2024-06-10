
def get_accommodation_fee(n, k, x, y):
    fee = 0
    for i in range(1, n+1):
        if i <= k:
            fee += x
        else:
            fee += y
    return fee

def main():
    n, k, x, y = map(int, input().split())
    print(get_accommodation_fee(n, k, x, y))

if __name__ == '__main__':
    main()

