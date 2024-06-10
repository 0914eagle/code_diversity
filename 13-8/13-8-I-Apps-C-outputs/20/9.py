
def get_maximum_amount(n, m, coupons):
    # Initialize a dictionary to store the number of coupons used for each number
    num_coupon_used = {}
    for i in range(m):
        q, w = coupons[i]
        num_coupon_used[q] = num_coupon_used.get(q, 0) + 1
    
    # Initialize a list to store the numbers that can be used to construct the array
    available_nums = []
    for i in range(1, n+1):
        if i not in num_coupon_used or num_coupon_used[i] > 0:
            available_nums.append(i)
    
    # Initialize a list to store the maximum amount of money that can be paid for each number
    max_amount = [0] * (n+1)
    max_amount[0] = 0
    for i in range(1, n+1):
        if i in num_coupon_used:
            max_amount[i] = max_amount[i-1] + num_coupon_used[i] * coupons[i-1][1]
        else:
            max_amount[i] = max_amount[i-1]
    
    # Initialize a list to store the maximum amount of money that can be paid for each combination of numbers
    dp = [0] * (n+1)
    dp[0] = 0
    for i in range(1, n+1):
        for j in range(i, n+1):
            if i in num_coupon_used and j in num_coupon_used and num_coupon_used[i] > 0 and num_coupon_used[j] > 0:
                dp[j] = max(dp[j], dp[i-1] + max_amount[j])
            else:
                dp[j] = max(dp[j], dp[i-1] + max_amount[j])
    
    return dp[n]

def main():
    n, m = map(int, input().split())
    coupons = []
    for i in range(m):
        q, w = map(int, input().split())
        coupons.append((q, w))
    print(get_maximum_amount(n, m, coupons))

if __name__ == '__main__':
    main()

