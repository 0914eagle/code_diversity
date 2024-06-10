
def get_maximum_amount(n, m, coupons):
    # Initialize a dictionary to store the number of coupons available for each value
    coupon_count = {}
    for q, w in coupons:
        if q not in coupon_count:
            coupon_count[q] = 0
        coupon_count[q] += 1

    # Initialize a list to store the values that have at least one coupon available
    available_values = []
    for q, w in coupons:
        if coupon_count[q] > 0:
            available_values.append(q)

    # Initialize a list to store the maximum amount of money that can be paid for each value
    max_amount = [0] * (n + 1)
    max_amount[0] = 0

    # Dynamic programming approach
    for i in range(1, n + 1):
        for value in available_values:
            if value <= i:
                max_amount[i] = max(max_amount[i], max_amount[i - value] + value * coupon_count[value])

    return max_amount[n]

def main():
    n, m = map(int, input().split())
    coupons = []
    for i in range(m):
        q, w = map(int, input().split())
        coupons.append((q, w))
    print(get_maximum_amount(n, m, coupons))

if __name__ == '__main__':
    main()

