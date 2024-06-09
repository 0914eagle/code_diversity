
def solve(m, n, p, q):
    if m < n or n < 1 or p < 1 or q < 1:
        return "IMPOSSIBLE"
    
    # Initialize the possible digits for the first n digits
    possible_digits = set(range(1, 10))
    
    # Iterate through the possible digits for the first n digits
    for i in range(n):
        # If the current digit is not possible, remove it from the set of possible digits
        if i not in possible_digits:
            continue
        
        # Check if the remaining digits form a valid number
        remaining_digits = possible_digits - {i}
        if len(remaining_digits) < m - n:
            continue
        
        # Check if the product of the remaining digits and q is equal to the original number
        product = 1
        for j in remaining_digits:
            product *= j
        if product % q == 0 and product // q == p:
            return str(i) + "".join(str(j) for j in sorted(remaining_digits))
    
    return "IMPOSSIBLE"

