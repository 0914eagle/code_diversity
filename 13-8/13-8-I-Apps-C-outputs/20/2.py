
def max_amount_of_money(n, m, coupons):
    # Initialize a dictionary to store the number of coupons for each value
    num_coupons = {}
    for q, w in coupons:
        if q not in num_coupons:
            num_coupons[q] = 1
        else:
            num_coupons[q] += 1
    
    # Initialize a list to store the values that are not used in the array
    unused_values = set(num_coupons.keys())
    
    # Initialize a variable to store the maximum amount of money that can be paid
    max_amount = 0
    
    # Loop through each value in the range [1, n]
    for i in range(1, n + 1):
        # If the current value is not used in the array, continue to the next value
        if i not in unused_values:
            continue
        
        # If the current value is used in the array, remove it from the unused values list
        unused_values.remove(i)
        
        # If the current value has a coupon, pay the cost of the coupon and add the value to the list of unused values
        if i in num_coupons:
            max_amount += num_coupons[i]
            unused_values.add(i + 1)
    
    # Return the maximum amount of money that can be paid
    return max_amount

def main():
    n, m = map(int, input().split())
    coupons = []
    for i in range(m):
        q, w = map(int, input().split())
        coupons.append((q, w))
    print(max_amount_of_money(n, m, coupons))

if __name__ == '__main__':
    main()

