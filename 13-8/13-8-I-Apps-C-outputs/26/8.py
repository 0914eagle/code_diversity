
def get_complete_codes(partial_code):
    # Initialize a set to store the complete codes
    complete_codes = set()
    
    # Iterate over the partial code
    for row in partial_code:
        # Initialize a set to store the digits in the current row
        row_digits = set()
        # Iterate over the digits in the current row
        for digit in row:
            # If the digit is not zero, add it to the set of row digits
            if digit != 0:
                row_digits.add(digit)
        # If the set of row digits is not empty, add it to the set of complete codes
        if row_digits:
            complete_codes.add(frozenset(row_digits))
    
    # Return the number of complete codes
    return len(complete_codes)

def main():
    # Read the input
    m, n = map(int, input().split())
    partial_code = []
    for _ in range(m):
        partial_code.append(list(map(int, input().split())))
    
    # Call the function to get the number of complete codes
    num_complete_codes = get_complete_codes(partial_code)
    
    # Print the number of complete codes
    print(num_complete_codes)

if __name__ == '__main__':
    main()

