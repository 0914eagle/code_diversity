
def is_easily_playable(s):
    # Check if the length of the string is between 1 and 100 (inclusive)
    if not 1 <= len(s) <= 100:
        return "No"
    
    # Check if all characters are L, R, U, or D
    if not all(c in ["L", "R", "U", "D"] for c in s):
        return "No"
    
    # Check if every character in an odd position is R, U, or D
    if not all(c in ["R", "U", "D"] for i, c in enumerate(s) if i % 2 == 1):
        return "No"
    
    # Check if every character in an even position is L, U, or D
    if not all(c in ["L", "U", "D"] for i, c in enumerate(s) if i % 2 == 0):
        return "No"
    
    return "Yes"

def main():
    s = input()
    print(is_easily_playable(s))

if __name__ == '__main__':
    main()

