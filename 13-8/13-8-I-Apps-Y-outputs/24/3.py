
def is_easily_playable(s):
    # Check if the length of the string is between 1 and 100
    if not 1 <= len(s) <= 100:
        return "No"
    
    # Check if the string contains only L, R, U, and D
    if not all(c in "LRUD" for c in s):
        return "No"
    
    # Check if the characters in odd positions are R, U, or D
    if not all(s[i] in "RUD" for i in range(1, len(s), 2)):
        return "No"
    
    # Check if the characters in even positions are L, U, or D
    if not all(s[i] in "LUD" for i in range(2, len(s), 2)):
        return "No"
    
    # If all conditions are met, return "Yes"
    return "Yes"

def main():
    s = input("Enter a string: ")
    print(is_easily_playable(s))

if __name__ == "__main__":
    main()

