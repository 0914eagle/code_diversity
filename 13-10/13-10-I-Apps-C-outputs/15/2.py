
def get_maximum_amount(n, m, coupons):
    # Initialize a dictionary to store the number of coupons used for each value
    coupons_used = {}
    for coupon in coupons:
        q, w = coupon
        if q not in coupons_used:
            coupons_used[q] = 0
        coupons_used[q] += 1

    # Initialize a list to store the maximum amount of money that can be paid for each value
    max_amount = [0] * (n + 1)
    for i in range(1, n + 1):
        if i in coupons_used:
            max_amount[i] = coupons_used[i] * i

    # Iterate through the values and calculate the maximum amount of money that can be paid
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            max_amount[j] = max(max_amount[j], max_amount[i] + (j - i))

    return max_amount[n]

def main():
    n, m = map(int, input().split())
    coupons = []
    for _ in range(m):
        q, w = map(int, input().split())
        coupons.append((q, w))
    print(get_maximum_amount(n, m, coupons))

if __name__ == '__main__':
    main()

