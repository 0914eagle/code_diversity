
def get_complete_codes(m, n, partial_code):
    # Initialize a set to store the complete codes
    complete_codes = set()
    
    # Iterate over the partial code
    for i in range(m):
        for j in range(n):
            # If the current cell is not filled, skip it
            if partial_code[i][j] == 0:
                continue
            
            # Get the values of the cells above, below, left, and right of the current cell
            above = partial_code[i-1][j] if i > 0 else 0
            below = partial_code[i+1][j] if i < m-1 else 0
            left = partial_code[i][j-1] if j > 0 else 0
            right = partial_code[i][j+1] if j < n-1 else 0
            
            # Check if the current cell satisfies the property
            if above == 0 or below == 0 or left == 0 or right == 0:
                continue
            
            # Check if the current cell is the product, sum, difference, or quotient of the cells above, below, left, and right
            if partial_code[i][j] == above * right or partial_code[i][j] == above + right or partial_code[i][j] == above - right or partial_code[i][j] == above // right:
                complete_codes.add(tuple(map(tuple, partial_code)))
                break
    
    # Return the number of complete codes
    return len(complete_codes)

def main():
    m, n = map(int, input().split())
    partial_code = []
    for i in range(m):
        partial_code.append(list(map(int, input().split())))
    print(get_complete_codes(m, n, partial_code))

if __name__ == '__main__':
    main()

