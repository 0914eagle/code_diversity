
import sys

def get_correct_fields(s):
    n = len(s)
    if n == 0:
        return 0
    
    # Initialize the dp table with all 0s
    dp = [0] * (n + 1)
    dp[0] = 1
    
    # Iterate over the characters of the input string
    for i in range(n):
        # If the current character is '?', then we have 3 options:
        # 1. The current cell is empty and there are no bombs in the adjacent cells
        # 2. The current cell is empty and there is 1 bomb in the adjacent cells
        # 3. The current cell is empty and there are 2 bombs in the adjacent cells
        if s[i] == '?':
            dp[i + 1] = (dp[i] * 3) % 1000000007
        # If the current character is '*', then we have 0 options, since we cannot place a bomb in this cell
        elif s[i] == '*':
            dp[i + 1] = 0
        # If the current character is a digit, then we have 1 option, since we can place the corresponding number in this cell
        else:
            dp[i + 1] = dp[i]
    
    return dp[n]

def main():
    s = input()
    print(get_correct_fields(s))

if __name__ == '__main__':
    main()

