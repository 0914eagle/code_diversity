
def get_accommodation_fee(n, k, x, y):
    # Calculate the fee for the first k nights
    fee_1 = k * x
    
    # Calculate the fee for the remaining nights
    fee_2 = (n - k) * y
    
    # Return the total fee
    return fee_1 + fee_2

def main():
    # Read the input from stdin
    n, k, x, y = input().split()
    
    # Convert the input to integers
    n = int(n)
    k = int(k)
    x = int(x)
    y = int(y)
    
    # Calculate the total accommodation fee
    fee = get_accommodation_fee(n, k, x, y)
    
    # Print the result
    print(fee)

if __name__ == '__main__':
    main()

