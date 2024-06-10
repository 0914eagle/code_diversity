
def solve(S):
    # Initialize variables
    num_black, num_white = 0, 0
    # Iterate through the string S
    for i in range(len(S)):
        # If the current character is 'B', increment the number of black stones
        if S[i] == 'B':
            num_black += 1
        # If the current character is 'W', increment the number of white stones
        elif S[i] == 'W':
            num_white += 1
    # Return the minimum number of new stones needed to achieve Jiro's purpose
    return min(num_black, num_white)

def main():
    # Read a single line of input from stdin and convert it to an integer
    S = input().strip()
    # Print the minimum number of new stones needed to achieve Jiro's purpose
    print(solve(S))

if __name__ == '__main__':
    main()

