
def get_maximum_payment(n, m, coupons):
    # Initialize a dictionary to store the number of coupons available for each value
    coupon_count = {}
    for q, w in coupons:
        if q not in coupon_count:
            coupon_count[q] = 1
        else:
            coupon_count[q] += 1
    
    # Initialize a set to store the values that have been used
    used_values = set()
    
    # Initialize a variable to store the maximum payment
    maximum_payment = 0
    
    # Iterate through the values in the coupon_count dictionary
    for q, count in coupon_count.items():
        # If the value has not been used before, add it to the set of used values
        if q not in used_values:
            used_values.add(q)
            # Add the cost of the coupon to the maximum payment
            maximum_payment += count * q
    
    # If there are still coupons left, iterate through the values in the coupon_count dictionary again
    if len(coupon_count) > len(used_values):
        for q, count in coupon_count.items():
            # If the value has not been used before, add it to the set of used values
            if q not in used_values:
                used_values.add(q)
                # Add the cost of the coupon to the maximum payment
                maximum_payment += count * q
    
    # Return the maximum payment
    return maximum_payment

def main():
    n, m = map(int, input().split())
    coupons = []
    for _ in range(m):
        q, w = map(int, input().split())
        coupons.append((q, w))
    print(get_maximum_payment(n, m, coupons))

if __name__ == '__main__':
    main()

