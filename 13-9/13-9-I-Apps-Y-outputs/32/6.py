
def get_min_stones(S):
    # Initialize variables
    min_stones = 0
    count_black = 0
    count_white = 0
    
    # Iterate through the string S
    for i in range(len(S)):
        # Check if the current stone is black
        if S[i] == "B":
            count_black += 1
        # Check if the current stone is white
        elif S[i] == "W":
            count_white += 1
    
    # Check if the board needs to be reversed
    if count_black > count_white:
        min_stones = count_black - count_white
    elif count_white > count_black:
        min_stones = count_white - count_black
    
    return min_stones

def main():
    S = input()
    print(get_min_stones(S))

if __name__ == '__main__':
    main()

