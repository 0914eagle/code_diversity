
def get_kth_digit(k):
    # Calculate the position of the digit in the sequence
    position = k
    
    # Initialize the digit to 1
    digit = 1
    
    # Iterate until we reach the desired position
    while position > 1:
        # Calculate the next digit in the sequence
        digit = (digit * 10) % 9
        
        # Decrement the position
        position -= 1
    
    # Return the digit
    return digit

def main():
    # Read the input k
    k = int(input())
    
    # Calculate the k-th digit of the sequence
    digit = get_kth_digit(k)
    
    # Print the result
    print(digit)

if __name__ == '__main__':
    main()

