
def is_win(s):
    if len(s) == 3:
        return "First"
    
    # Check if the string is already in the required format
    if s[0] != s[1] and s[-1] != s[-2]:
        return "First"
    
    # Check if the string can be transformed into the required format
    for i in range(1, len(s) - 1):
        if s[i] == s[i - 1] or s[i] == s[i + 1]:
            return "Second"
    
    return "First"

def main():
    s = input()
    print(is_win(s))

if __name__ == '__main__':
    main()

