
def is_easily_playable(s):
    # Check if the length of the string is between 1 and 100, inclusive
    if not 1 <= len(s) <= 100:
        return "No"
    
    # Check if all characters are L, R, U, or D
    for i in s:
        if i not in ["L", "R", "U", "D"]:
            return "No"
    
    # Check if the characters in odd positions are R, U, or D
    for i in range(1, len(s), 2):
        if s[i] not in ["R", "U", "D"]:
            return "No"
    
    # Check if the characters in even positions are L, U, or D
    for i in range(2, len(s), 2):
        if s[i] not in ["L", "U", "D"]:
            return "No"
    
    # If all conditions are met, return "Yes"
    return "Yes"

def main():
    s = input()
    print(is_easily_playable(s))

if __name__ == '__main__':
    main()

