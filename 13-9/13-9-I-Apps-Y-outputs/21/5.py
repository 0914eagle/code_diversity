
def get_accommodation_fee(n, k, x, y):
    total_fee = 0
    for i in range(n):
        if i < k:
            total_fee += x
        else:
            total_fee += y
    return total_fee

def main():
    n, k, x, y = map(int, input().split())
    total_fee = get_accommodation_fee(n, k, x, y)
    print(total_fee)

if __name__ == '__main__':
    main()

