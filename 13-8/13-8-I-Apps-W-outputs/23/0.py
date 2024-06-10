
def get_moves(S):
    # Initialize the number of moves to 0
    num_moves = 0
    
    # Loop through each character in the string S
    for i in range(len(S)):
        # If the current character is L, move one square to the left
        if S[i] == 'L':
            num_moves -= 1
        # If the current character is R, move one square to the right
        else:
            num_moves += 1
    
    # Return the total number of moves
    return num_moves

def get_squares(S):
    # Initialize a list to store the number of children standing on each square
    num_children = [0] * len(S)
    
    # Loop through each character in the string S
    for i in range(len(S)):
        # If the current character is L, move one square to the left
        if S[i] == 'L':
            num_children[i-1] += 1
        # If the current character is R, move one square to the right
        else:
            num_children[i+1] += 1
    
    # Return the list of number of children standing on each square
    return num_children

if __name__ == '__main__':
    S = input()
    num_moves = get_moves(S)
    num_children = get_squares(S)
    print(*num_children)

