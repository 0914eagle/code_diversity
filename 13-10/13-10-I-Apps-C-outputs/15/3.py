
def get_maximum_payment(n, m, coupons):
    # Initialize a dictionary to store the number of coupon uses for each value
    coupon_uses = {}
    for q, w in coupons:
        coupon_uses[q] = coupon_uses.get(q, 0) + 1

    # Initialize a list to store the values that have been used
    used_values = []

    # Loop through the coupon values and use the minimum number of coupon uses possible
    for i in range(n):
        min_coupon_use = float('inf')
        for q in coupon_uses:
            if q not in used_values and coupon_uses[q] < min_coupon_use:
                min_coupon_use = coupon_uses[q]
                value = q
        used_values.append(value)
        coupon_uses[value] -= 1

    # Calculate the maximum payment by summing the cost of the used coupons
    maximum_payment = 0
    for value in used_values:
        maximum_payment += coupons[value - 1][1]

    return maximum_payment

def main():
    n, m = map(int, input().split())
    coupons = []
    for i in range(m):
        q, w = map(int, input().split())
        coupons.append((q, w))
    print(get_maximum_payment(n, m, coupons))

if __name__ == '__main__':
    main()

