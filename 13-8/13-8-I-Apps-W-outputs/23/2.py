
def move_children(S):
    # Initialize the number of children on each square
    num_children = [0] * len(S)
    num_children[0] = 1
    num_children[-1] = 1

    # Iterate through each character of S
    for i in range(1, len(S) - 1):
        # If the current character is L, move the child left
        if S[i] == "L":
            num_children[i - 1] += num_children[i]
        # If the current character is R, move the child right
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

