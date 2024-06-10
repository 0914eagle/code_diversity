
import itertools

def get_complete_codes(partial_code, m, n):
    # Initialize a list to store the complete codes
    complete_codes = []
    
    # Iterate over each row of the partial code
    for i in range(m):
        # Get the row of the partial code
        row = partial_code[i]
        
        # Get the indices of the unknown values in the row
        unknown_indices = [j for j, x in enumerate(row) if x == 0]
        
        # If there are no unknown values in the row, skip to the next row
        if not unknown_indices:
            continue
        
        # Get the values of the known digits in the row
        known_values = [x for x in row if x != 0]
        
        # Get the number of unknown values in the row
        num_unknown = len(unknown_indices)
        
        # Get the combinations of numbers that can be used to fill in the unknown values
        combinations = itertools.combinations(known_values, num_unknown)
        
        # Iterate over each combination of numbers
        for combination in combinations:
            # Create a copy of the partial code
            code = partial_code[:]
            
            # Fill in the unknown values in the row with the current combination of numbers
            for j, x in enumerate(combination):
                code[i][unknown_indices[j]] = x
            
            # If the code is complete, add it to the list of complete codes
            if all(code[i].count(x) == 1 for i in range(m) for x in range(1, 10) if x not in code[i]):
                complete_codes.append(code)
    
    # Return the list of complete codes
    return complete_codes

def get_num_complete_codes(partial_code, m, n):
    # Get the complete codes from the partial code
    complete_codes = get_complete_codes(partial_code, m, n)
    
    # Return the number of complete codes
    return len(complete_codes)

if __name__ == '__main__':
    m, n = map(int, input().split())
    partial_code = []
    for i in range(m):
        row = list(map(int, input().split()))
        partial_code.append(row)
    print(get_num_complete_codes(partial_code, m, n))

