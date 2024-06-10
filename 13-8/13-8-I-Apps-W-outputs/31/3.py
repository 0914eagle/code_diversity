
def get_standing_dominoes(n, s):
    # Initialize variables
    standing_dominoes = 0
    left_dominoes = 0
    right_dominoes = 0
    
    # Iterate through the dominoes
    for i in range(n):
        # Check if the domino is standing vertically
        if s[i] == ".":
            standing_dominoes += 1
        # Check if the domino is falling to the left
        elif s[i] == "L":
            left_dominoes += 1
        # Check if the domino is falling to the right
        elif s[i] == "R":
            right_dominoes += 1
    
    # Return the number of standing dominoes
    return standing_dominoes

def main():
    # Read the input
    n = int(input())
    s = input()
    
    # Call the function to get the number of standing dominoes
    standing_dominoes = get_standing_dominoes(n, s)
    
    # Print the output
    print(standing_dominoes)

if __name__ == '__main__':
    main()

