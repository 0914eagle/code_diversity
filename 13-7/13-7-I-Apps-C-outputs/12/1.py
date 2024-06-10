
def get_happy_digits(a, k):
    happy_digits = []
    for i in range(k):
        if i % k == 0:
            happy_digits.append(i)
    return happy_digits

def get_tax_amount(a, k, n):
    tax_amount = 0
    for i in range(n):
        tax_amount += a[i]
    return tax_amount

def get_happy_tax_amounts(a, k, n):
    happy_tax_amounts = []
    tax_amount = get_tax_amount(a, k, n)
    happy_digits = get_happy_digits(a, k)
    for i in range(k):
        if str(tax_amount)[-1] == str(i):
            happy_tax_amounts.append(tax_amount)
            break
    return happy_tax_amounts

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    happy_tax_amounts = get_happy_tax_amounts(a, k, n)
    print(len(happy_tax_amounts))
    for i in happy_tax_amounts:
        print(i)

if __name__ == '__main__':
    main()

