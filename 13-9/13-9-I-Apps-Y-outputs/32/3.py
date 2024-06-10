
def solve(S):
    # Initialize variables
    num_black = 0
    num_white = 0
    same_color = True
    
    # Iterate through the string S
    for i in range(len(S)):
        # Check if the current stone is black
        if S[i] == "B":
            num_black += 1
        # Check if the current stone is white
        elif S[i] == "W":
            num_white += 1
        # Check if the current stone is not the same color as the previous stone
        if i > 0 and S[i] != S[i-1]:
            same_color = False
            break
    
    # Check if all stones are the same color
    if same_color:
        return 0
    
    # Check if the number of black stones is greater than the number of white stones
    if num_black > num_white:
        return num_black - num_white
    # Check if the number of white stones is greater than the number of black stones
    else:
        return num_white - num_black
    
def main():
    S = input()
    print(solve(S))
    
if __name__ == '__main__':
    main()

