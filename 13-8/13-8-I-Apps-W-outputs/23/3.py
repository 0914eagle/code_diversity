
def get_moves(S):
    # Initialize the number of children on each square
    num_children = [0] * len(S)
    
    # Set the initial number of children on the first and last squares
    num_children[0] = 1
    num_children[-1] = 1
    
    # Loop through each character of the string
    for i in range(1, len(S) - 1):
        # If the character is L, move the child to the left
        if S[i] == "L":
            num_children[i - 1] += num_children[i]
        # If the character is R, move the child to the right
        else:
            num_children[i + 1] += num_children[i]
    
    return num_children

def get_final_positions(S):
    # Get the number of children on each square after each child moves
    num_children = get_moves(S)
    
    # Get the final number of children on each square
    final_positions = [0] * len(S)
    for i in range(len(S)):
        final_positions[i] = num_children[i]
    
    return final_positions

if __name__ == '__main__':
    S = input()
    print(*get_final_positions(S), sep=' ')

