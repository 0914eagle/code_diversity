
def is_valid_code(code):
    # Check if the code has no repeated digits in any row
    for row in code:
        if len(set(row)) != len(row):
            return False
    
    # Check if the code has the correct property for each non-zero digit
    for i in range(len(code)):
        for j in range(len(code[0])):
            if code[i][j] != 0:
                if i > 0 and code[i-1][j] != 0:
                    if code[i-1][j] % code[i][j] != 0 and code[i-1][j] + code[i][j] != 0 and code[i-1][j] - code[i][j] != 0 and code[i-1][j] * code[i][j] != 0:
                        return False
                if j < len(code[0])-1 and code[i][j+1] != 0:
                    if code[i][j+1] % code[i][j] != 0 and code[i][j+1] + code[i][j] != 0 and code[i][j+1] - code[i][j] != 0 and code[i][j+1] * code[i][j] != 0:
                        return False
    
    return True

def find_complete_codes(code):
    # Find the number of unknown values in the code
    num_unknown = 0
    for row in code:
        for elem in row:
            if elem == 0:
                num_unknown += 1
    
    # Initialize a list to store all possible complete codes
    complete_codes = []
    
    # Iterate through all possible combinations of values for the unknown digits
    for i in range(10**num_unknown):
        # Convert the current combination to a list of digits
        combination = [int(digit) for digit in str(i)]
        
        # Check if the current combination forms a valid code
        if is_valid_code(code):
            # Add the current combination to the list of complete codes
            complete_codes.append(code)
    
    return len(complete_codes)

if __name__ == '__main__':
    m, n = map(int, input().split())
    code = []
    for i in range(m):
        code.append(list(map(int, input().split())))
    print(find_complete_codes(code))

