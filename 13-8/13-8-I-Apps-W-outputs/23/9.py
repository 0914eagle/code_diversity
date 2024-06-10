
def get_moves(S):
    # Initialize the number of children on each square
    num_children = [0] * len(S)
    
    # Set the first and last children
    num_children[0] = 1
    num_children[-1] = 1
    
    # Iterate through the moves
    for i in range(10**100):
        for j in range(len(S)):
            if S[j] == "L":
                num_children[j-1] += num_children[j]
            else:
                num_children[j+1] += num_children[j]
    
    return num_children

def main():
    S = input()
    print(*get_moves(S), sep=" ")

if __name__ == '__main__':
    main()

