
def is_easily_playable(S):
    # Check if the length of S is between 1 and 100 (inclusive)
    if not 1 <= len(S) <= 100:
        return "No"
    
    # Check if S contains only L, R, U, and D
    if not all(c in ["L", "R", "U", "D"] for c in S):
        return "No"
    
    # Check if every character in an odd position is R, U, or D
    for i in range(1, len(S), 2):
        if S[i] not in ["R", "U", "D"]:
            return "No"
    
    # Check if every character in an even position is L, U, or D
    for i in range(2, len(S), 2):
        if S[i] not in ["L", "U", "D"]:
            return "No"
    
    # If all conditions are met, return "Yes"
    return "Yes"

def main():
    S = input()
    print(is_easily_playable(S))

if __name__ == '__main__':
    main()

