
def get_max_money(n, m, coupons):
    # Initialize a dictionary to store the number of coupons available for each value
    num_coupons = {}
    for q, w in coupons:
        if q not in num_coupons:
            num_coupons[q] = 1
        else:
            num_coupons[q] += 1
    
    # Initialize a list to store the maximum amount of money that can be paid for each value
    max_money = [0] * (n + 1)
    max_money[0] = 0
    
    # Iterate through the values in the array
    for i in range(1, n + 1):
        # If the current value is not covered by any coupon, the maximum amount of money that can be paid is 0
        if i not in num_coupons:
            max_money[i] = 0
        # Otherwise, find the maximum amount of money that can be paid by combining the coupons for the current value with the maximum amount of money that can be paid for the previous values
        else:
            max_money[i] = max(max_money[i - 1], num_coupons[i] * w)
    
    return max_money[n]

def main():
    n, m = map(int, input().split())
    coupons = []
    for _ in range(m):
        q, w = map(int, input().split())
        coupons.append((q, w))
    print(get_max_money(n, m, coupons))

if __name__ == '__main__':
    main()

