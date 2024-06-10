
def get_total_accommodation_fee(n, k, x, y):
    total = 0
    for i in range(1, n+1):
        if i <= k:
            total += x
        else:
            total += y
    return total

def main():
    n, k, x, y = map(int, input().split())
    print(get_total_accommodation_fee(n, k, x, y))

if __name__ == '__main__':
    main()

