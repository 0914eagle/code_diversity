
def get_maximum_payment(n, m, coupons):
    # Initialize a dictionary to store the number of available coupons for each value
    available_coupons = {}
    for coupon in coupons:
        if coupon[0] not in available_coupons:
            available_coupons[coupon[0]] = 1
        else:
            available_coupons[coupon[0]] += 1
    
    # Initialize a list to store the values that can be used to build the array
    available_values = []
    for value in available_coupons:
        available_values.append(value)
    
    # Sort the available values in descending order
    available_values.sort(reverse=True)
    
    # Initialize a variable to store the maximum payment that can be made
    maximum_payment = 0
    
    # Iterate through the available values and check if they can be used to build a beautiful array
    for value in available_values:
        # Check if the value occurs in the array
        if value in available_coupons:
            # Calculate the number of coupons that can be used for the current value
            num_coupons = available_coupons[value]
            
            # Calculate the maximum payment that can be made using the current value
            maximum_payment += num_coupons * value
            
            # Update the available coupons for the current value
            available_coupons[value] = 0
    
    return maximum_payment

def main():
    n, m = map(int, input().split())
    coupons = []
    for i in range(m):
        q, w = map(int, input().split())
        coupons.append([q, w])
    print(get_maximum_payment(n, m, coupons))

if __name__ == '__main__':
    main()

