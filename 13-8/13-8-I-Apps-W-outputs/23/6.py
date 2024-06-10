
def move_children(S):
    # Initialize the number of children on each square
    num_children = [0] * len(S)
    
    # Set the first and last children to 1
    num_children[0] = 1
    num_children[-1] = 1
    
    # Loop through each character of the string
    for i in range(1, len(S) - 1):
        # If the character is L, move the child to the left
        if S[i] == 'L':
            num_children[i - 1] += num_children[i]
        # If the character is R, move the child to the right
        else:
            num_children[i + 1] += num_children[i]
    
    # Return the number of children on each square
    return num_children

def main():
    S = input()
    num_children = move_children(S)
    print(*num_children)

if __name__ == '__main__':
    main()

