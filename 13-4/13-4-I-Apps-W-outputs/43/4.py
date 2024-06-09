
def get_unique_promo_code(promo_codes):
    # Initialize a dictionary to store the number of errors for each promo code
    errors = {}
    
    # Loop through each promo code
    for promo_code in promo_codes:
        # Get the number of errors for this promo code
        num_errors = get_num_errors(promo_code)
        
        # If the promo code has not been seen before, add it to the dictionary with the number of errors
        if promo_code not in errors:
            errors[promo_code] = num_errors
        # If the promo code has been seen before and the number of errors is less than the current number of errors, update the number of errors
        elif num_errors < errors[promo_code]:
            errors[promo_code] = num_errors
    
    # Return the maximum number of errors that allows each promo code to be uniquely identified
    return max(errors.values())

def get_num_errors(promo_code):
    # Initialize a variable to store the number of errors
    num_errors = 0
    
    # Loop through each digit in the promo code
    for i in range(len(promo_code)):
        # If the digit is not a 0 or 9, increment the number of errors
        if promo_code[i] not in ["0", "9"]:
            num_errors += 1
    
    # Return the number of errors
    return num_errors

def main():
    # Read the number of promo codes
    n = int(input())
    
    # Read the promo codes
    promo_codes = []
    for _ in range(n):
        promo_codes.append(input())
    
    # Call the function to get the maximum number of errors
    max_errors = get_unique_promo_code(promo_codes)
    
    # Print the result
    print(max_errors)

if __name__ == '__main__':
    main()

