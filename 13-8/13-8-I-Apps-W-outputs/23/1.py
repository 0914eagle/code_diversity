
def get_final_squares(S):
    # Initialize the number of children on each square
    num_children = [0] * len(S)
    
    # Set the initial position of the children
    num_children[0] = 1
    num_children[-1] = 1
    
    # Iterate through each move
    for i in range(10**100):
        # Move the children
        for j in range(len(S)):
            if S[j] == "L":
                num_children[(j-1)%len(S)] += num_children[j]
            else:
                num_children[(j+1)%len(S)] += num_children[j]
        
        # Reset the number of children on the current square
        num_children[j] = 0
    
    return num_children

def main():
    S = input()
    print(*get_final_squares(S), sep=" ")

if __name__ == "__main__":
    main()

