
def solve(s):
    n = len(s)
    if n == 1:
        return 1
    
    # Initialize the board with the given string
    board = [0] * n
    for i in range(n):
        if s[i] == "B":
            board[i] = 1
        else:
            board[i] = -1
    
    # Count the number of stones of each color
    num_black = sum(board)
    num_white = n - num_black
    
    # If the number of stones of each color is not equal, return -1
    if abs(num_black - num_white) > 1:
        return -1
    
    # If the number of stones of each color is equal, return the minimum number of new stones needed
    if num_black > num_white:
        return num_black - num_white
    else:
        return num_white - num_black
    
def main():
    s = input()
    print(solve(s))
    
if __name__ == '__main__':
    main()

