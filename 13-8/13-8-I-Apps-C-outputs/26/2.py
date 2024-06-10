
def get_complete_codes(m, n, partial_code):
    # Initialize a list to store the complete codes
    complete_codes = []
    
    # Iterate over each row of the partial code
    for i in range(m):
        # Get the current row of the partial code
        current_row = partial_code[i]
        
        # If the current row has no zeros, it is a complete code
        if current_row.count(0) == 0:
            complete_codes.append(current_row)
            continue
        
        # If the current row has zeros, we need to find the possible values for the zeros
        possible_values = get_possible_values(current_row)
        
        # Iterate over each possible value for the zeros
        for possible_value in possible_values:
            # Replace the zeros with the possible value in the current row
            current_row = [possible_value if x == 0 else x for x in current_row]
            
            # If the current row is a complete code, add it to the list of complete codes
            if current_row.count(0) == 0:
                complete_codes.append(current_row)
    
    # Return the list of complete codes
    return complete_codes

def get_possible_values(row):
    # Initialize a set to store the possible values for the zeros
    possible_values = set()
    
    # Iterate over each pair of non-zero digits in the row
    for i in range(len(row)):
        for j in range(i+1, len(row)):
            # If the two digits are not zero and they have the property described in the problem, add their product, sum, difference, or quotient to the set of possible values
            if row[i] != 0 and row[j] != 0 and (row[i] * row[j] in row or row[i] + row[j] in row or row[i] - row[j] in row or row[i] // row[j] in row):
                possible_values.add(row[i] * row[j])
                possible_values.add(row[i] + row[j])
                possible_values.add(row[i] - row[j])
                possible_values.add(row[i] // row[j])
    
    # Return the set of possible values
    return possible_values

if __name__ == '__main__':
    m, n = map(int, input().split())
    partial_code = []
    for i in range(m):
        partial_code.append(list(map(int, input().split())))
    print(len(get_complete_codes(m, n, partial_code)))

