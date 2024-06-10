
def get_max_payment(n, m, coupons):
    # Initialize a dictionary to store the number of occurrences of each coupon value
    coupon_counts = {}
    for coupon in coupons:
        if coupon[0] not in coupon_counts:
            coupon_counts[coupon[0]] = 0
        coupon_counts[coupon[0]] += 1

    # Initialize a dictionary to store the maximum payment for each coupon value
    max_payments = {}
    for coupon in coupons:
        max_payments[coupon[0]] = 0

    # Loop through the coupon values and calculate the maximum payment for each one
    for coupon in coupons:
        if coupon[0] in coupon_counts and coupon_counts[coupon[0]] > 0:
            max_payments[coupon[0]] = max(max_payments[coupon[0]], coupon[1] * coupon_counts[coupon[0]])

    # Calculate the maximum payment by summing up the maximum payments for each coupon value
    max_payment = sum(max_payments.values())

    return max_payment

def main():
    n, m = map(int, input().split())
    coupons = []
    for i in range(m):
        q, w = map(int, input().split())
        coupons.append([q, w])
    max_payment = get_max_payment(n, m, coupons)
    print(max_payment)

if __name__ == '__main__':
    main()

