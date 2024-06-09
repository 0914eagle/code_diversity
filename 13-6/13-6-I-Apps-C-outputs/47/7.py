
def get_maximum_amount(n, m, coupons):
    # Initialize a dictionary to store the number of available coupons for each value
    available_coupons = {}
    for coupon in coupons:
        if coupon[0] not in available_coupons:
            available_coupons[coupon[0]] = 1
        else:
            available_coupons[coupon[0]] += 1
    
    # Initialize a list to store the values that have at least one available coupon
    available_values = []
    for value in available_coupons:
        if available_coupons[value] > 0:
            available_values.append(value)
    
    # Initialize a list to store the maximum amount of money that can be paid for each value
    maximum_amount = [0] * (n + 1)
    maximum_amount[0] = 0
    
    # Dynamic programming approach
    for i in range(1, n + 1):
        for value in available_values:
            if i - value >= 0 and maximum_amount[i - value] > 0:
                maximum_amount[i] = max(maximum_amount[i], maximum_amount[i - value] + value * available_coupons[value])
    
    return maximum_amount[n]

def main():
    n, m = map(int, input().split())
    coupons = []
    for i in range(m):
        q, w = map(int, input().split())
        coupons.append((q, w))
    print(get_maximum_amount(n, m, coupons))

if __name__ == '__main__':
    main()

