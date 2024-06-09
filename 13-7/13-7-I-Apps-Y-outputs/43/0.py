
def solve(x1, x2, x3, x4):
    # Initialize a list to store the possible values of a, b, and c
    abc = []
    
    # Iterate over all possible values of a
    for a in range(1, x1+1):
        # Iterate over all possible values of b
        for b in range(1, x2+1):
            # Iterate over all possible values of c
            for c in range(1, x3+1):
                # Check if a+b, a+c, b+c, and a+b+c are equal to the given numbers
                if a+b == x1 and a+c == x2 and b+c == x3 and a+b+c == x4:
                    # If they are equal, add the values of a, b, and c to the list
                    abc.append(a)
                    abc.append(b)
                    abc.append(c)
    
    # Return the list of possible values of a, b, and c
    return abc

