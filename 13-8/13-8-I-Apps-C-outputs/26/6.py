
def find_complete_codes(partial_code):
    # Initialize a set to store the complete codes
    complete_codes = set()
    
    # Iterate through each row of the partial code
    for i in range(len(partial_code)):
        # Get the current row of the partial code
        row = partial_code[i]
        
        # Initialize a set to store the digits in the current row
        digits = set()
        
        # Iterate through each digit in the current row
        for j in range(len(row)):
            # Get the current digit
            digit = row[j]
            
            # If the digit is not 0, add it to the set of digits
            if digit != 0:
                digits.add(digit)
        
        # If the set of digits is not empty, add it to the set of complete codes
        if digits:
            complete_codes.add(frozenset(digits))
    
    # Return the number of complete codes
    return len(complete_codes)

def main():
    # Read the input from stdin
    m, n = map(int, input().split())
    partial_code = []
    for _ in range(m):
        partial_code.append(list(map(int, input().split())))
    
    # Call the find_complete_codes function and print the result
    print(find_complete_codes(partial_code))

if __name__ == '__main__':
    main()

