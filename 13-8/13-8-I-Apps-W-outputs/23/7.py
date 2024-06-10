
def get_moves(S):
    # Initialize the number of children on each square
    num_children = [0] * len(S)
    
    # Set the first and last children
    num_children[0] = 1
    num_children[-1] = 1
    
    # Iterate through the moves
    for i in range(100):
        for j in range(len(S)):
            if S[j] == "L":
                num_children[j-1] += num_children[j]
            else:
                num_children[j+1] += num_children[j]
    
    return num_children

def main():
    S = input()
    num_children = get_moves(S)
    print(" ".join(map(str, num_children)))

if __name__ == '__main__':
    main()

