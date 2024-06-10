
def get_divine_digits(a, k):
    divine_digits = []
    for i in range(k):
        if i % k == a % k:
            divine_digits.append(i)
    return divine_digits

def get_divine_amounts(a, k, n):
    divine_amounts = []
    for i in range(n):
        amount = a[i]
        for j in range(i, n):
            amount += a[j]
            if amount % k == 0:
                divine_amounts.append(amount)
    return divine_amounts

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    divine_digits = get_divine_digits(a, k)
    divine_amounts = get_divine_amounts(a, k, n)
    print(len(divine_digits))
    print(*divine_amounts)

if __name__ == '__main__':
    main()

