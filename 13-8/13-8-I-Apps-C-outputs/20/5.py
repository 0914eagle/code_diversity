
def get_maximum_amount_of_money(n, m, coupons):
    # Initialize a dictionary to store the number of coupons available for each value
    coupon_counts = {}
    for coupon in coupons:
        q, w = coupon
        if q not in coupon_counts:
            coupon_counts[q] = 1
        else:
            coupon_counts[q] += 1
    
    # Initialize a list to store the values that have been used
    used_values = []
    
    # Initialize a variable to store the maximum amount of money that can be paid
    maximum_amount = 0
    
    # Loop through the values in the array
    for i in range(n):
        # If the current value has not been used, try to use it
        if i not in used_values:
            # Get the current value and the number of coupons available for it
            current_value = i + 1
            current_coupon_count = coupon_counts[current_value] if current_value in coupon_counts else 0
            
            # If there are enough coupons available for the current value, use it and update the maximum amount of money that can be paid
            if current_coupon_count > 0:
                used_values.append(i)
                maximum_amount += current_value * current_coupon_count
    
    return maximum_amount

def main():
    n, m = map(int, input().split())
    coupons = []
    for i in range(m):
        q, w = map(int, input().split())
        coupons.append((q, w))
    print(get_maximum_amount_of_money(n, m, coupons))

if __name__ == '__main__':
    main()

