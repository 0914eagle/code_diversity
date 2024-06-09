
def solve(S):
    # Initialize a list to store the number of children on each square
    children = [0] * len(S)
    
    # Set the first and last children to 1
    children[0] = 1
    children[-1] = 1
    
    # Iterate through each character of S
    for i in range(1, len(S) - 1):
        # If the current character is L, move the child left
        if S[i] == "L":
            children[i - 1] += 1
        # If the current character is R, move the child right
        else:
            children[i + 1] += 1
    
    # Return the number of children on each square
    return children

