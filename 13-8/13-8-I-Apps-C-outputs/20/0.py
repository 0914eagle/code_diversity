
def get_maximum_amount(n, m, coupons):
    # Initialize a dictionary to store the number of coupons available for each number
    num_coupon_dict = {}
    for q, w in coupons:
        if q not in num_coupon_dict:
            num_coupon_dict[q] = w
        else:
            num_coupon_dict[q] += w
    
    # Initialize a list to store the numbers that have been used
    used_nums = []
    
    # Initialize a variable to store the maximum amount of money that can be paid
    max_amount = 0
    
    # Loop through each number from 1 to n
    for i in range(1, n+1):
        # If the number has a coupon available
        if i in num_coupon_dict:
            # Add the number to the list of used numbers
            used_nums.append(i)
            # Update the maximum amount of money that can be paid
            max_amount += num_coupon_dict[i]
            # Remove the coupon from the dictionary
            del num_coupon_dict[i]
    
    # If there are any remaining coupons
    if num_coupon_dict:
        # Loop through the remaining coupons
        for q, w in num_coupon_dict.items():
            # If the number has not been used yet
            if q not in used_nums:
                # Add the number to the list of used numbers
                used_nums.append(q)
                # Update the maximum amount of money that can be paid
                max_amount += w
    
    return max_amount

def main():
    n, m = map(int, input().split())
    coupons = []
    for i in range(m):
        q, w = map(int, input().split())
        coupons.append((q, w))
    print(get_maximum_amount(n, m, coupons))

if __name__ == '__main__':
    main()

