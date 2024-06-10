
def is_easily_playable(S):
    # Check if the length of the string is between 1 and 100 (inclusive)
    if not 1 <= len(S) <= 100:
        return "No"
    
    # Check if all characters are L, R, U, or D
    for c in S:
        if c not in "LURD":
            return "No"
    
    # Check if every character in an odd position is R, U, or D
    for i in range(1, len(S), 2):
        if S[i] not in "RUD":
            return "No"
    
    # Check if every character in an even position is L, U, or D
    for i in range(2, len(S), 2):
        if S[i] not in "LUD":
            return "No"
    
    # If all checks pass, return "Yes"
    return "Yes"

def main():
    S = input()
    print(is_easily_playable(S))

if __name__ == '__main__':
    main()

