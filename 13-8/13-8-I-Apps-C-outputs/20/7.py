
def get_maximum_amount(n, m, coupons):
    # Initialize a dictionary to store the number of coupons used for each number
    num_coupon_dict = {}
    for coupon in coupons:
        num_coupon_dict[coupon[0]] = num_coupon_dict.get(coupon[0], 0) + 1
    
    # Initialize a list to store the maximum amount of money that can be paid for each number
    max_amount_list = [0] * (n + 1)
    for i in range(1, n + 1):
        if i in num_coupon_dict:
            max_amount_list[i] = num_coupon_dict[i] * coupons[i - 1][1]
    
    # Dynamic programming to find the maximum amount of money that can be paid
    for i in range(2, n + 1):
        for j in range(1, i):
            if max_amount_list[i] < max_amount_list[j] + max_amount_list[i - j]:
                max_amount_list[i] = max_amount_list[j] + max_amount_list[i - j]
    
    return max_amount_list[n]

def main():
    n, m = map(int, input().split())
    coupons = []
    for i in range(m):
        q, w = map(int, input().split())
        coupons.append((q, w))
    print(get_maximum_amount(n, m, coupons))

if __name__ == '__main__':
    main()

