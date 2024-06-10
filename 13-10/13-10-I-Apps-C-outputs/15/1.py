
def get_maximum_amount(n, m, coupons):
    # Initialize a dictionary to store the number of available coupons for each value
    available_coupons = {}
    for q, w in coupons:
        if q not in available_coupons:
            available_coupons[q] = 1
        else:
            available_coupons[q] += 1
    
    # Initialize a list to store the maximum amount of money that can be paid for each position in the array
    max_amount = [0] * (n + 1)
    max_amount[0] = 0
    
    # Iterate over the positions in the array
    for i in range(1, n + 1):
        # Iterate over the values that can be used at this position
        for q in range(1, i + 1):
            # Check if there are enough coupons available for this value
            if q in available_coupons and available_coupons[q] > 0:
                # Calculate the maximum amount of money that can be paid for this position
                max_amount[i] = max(max_amount[i], max_amount[i - q] + q * coupons[q - 1][1])
        
        # Update the maximum amount of money that can be paid for this position
        max_amount[i] = max(max_amount[i], max_amount[i - 1])
    
    # Return the maximum amount of money that can be paid
    return max_amount[n]

def main():
    n, m = map(int, input().split())
    coupons = []
    for _ in range(m):
        q, w = map(int, input().split())
        coupons.append((q, w))
    print(get_maximum_amount(n, m, coupons))

if __name__ == '__main__':
    main()

