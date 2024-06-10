
def count_children(S):
    # Initialize a list to store the number of children on each square
    children = [0] * len(S)
    
    # Set the first and last squares to have one child each
    children[0] = 1
    children[-1] = 1
    
    # Iterate through each character of the string
    for i in range(1, len(S) - 1):
        # If the current character is L, move one square to the left
        if S[i] == "L":
            children[i - 1] += 1
        # If the current character is R, move one square to the right
        else:
            children[i + 1] += 1
    
    # Return the number of children on each square
    return children

def main():
    # Read a string from standard input
    S = input()
    
    # Call the count_children function and print the result
    print(" ".join(map(str, count_children(S))))

if __name__ == '__main__':
    main()

