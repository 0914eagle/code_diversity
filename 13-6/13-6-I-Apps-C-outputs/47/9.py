
def get_maximum_amount(n, m, coupons):
    # Initialize a dictionary to store the number of coupons for each number
    number_to_coupon_count = {}
    for q, w in coupons:
        if q not in number_to_coupon_count:
            number_to_coupon_count[q] = 0
        number_to_coupon_count[q] += w
    
    # Initialize a list to store the numbers that have been used
    used_numbers = []
    
    # Initialize a variable to store the maximum amount that can be paid
    maximum_amount = 0
    
    # Loop through each number from 1 to n
    for i in range(1, n+1):
        # If the number has at least one coupon
        if i in number_to_coupon_count:
            # Add the number to the list of used numbers
            used_numbers.append(i)
            # Subtract the cost of the coupon from the maximum amount that can be paid
            maximum_amount -= number_to_coupon_count[i]
        # If the number does not have any coupon
        else:
            # Loop through the used numbers
            for j in used_numbers:
                # If the number is adjacent to the used number
                if abs(i-j) == 1:
                    # Add the number to the list of used numbers
                    used_numbers.append(i)
                    # Break the loop
                    break
    
    # Return the maximum amount that can be paid
    return maximum_amount

def main():
    n, m = map(int, input().split())
    coupons = []
    for i in range(m):
        q, w = map(int, input().split())
        coupons.append((q, w))
    print(get_maximum_amount(n, m, coupons))

if __name__ == '__main__':
    main()

