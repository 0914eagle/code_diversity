
def solve(S):
    # Initialize the number of new stones needed
    new_stones = 0

    # Iterate through the string S
    for i in range(len(S)):
        # If the current character is 'B' and the previous character is 'W', we need to place a new black stone
        if S[i] == 'B' and (i == 0 or S[i-1] == 'W'):
            new_stones += 1
        # If the current character is 'W' and the next character is 'B', we need to place a new white stone
        elif S[i] == 'W' and (i == len(S)-1 or S[i+1] == 'B'):
            new_stones += 1

    return new_stones

def main():
    S = input()
    print(solve(S))

if __name__ == '__main__':
    main()

