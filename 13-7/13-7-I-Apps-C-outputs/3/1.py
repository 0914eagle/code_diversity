
def solve(s):
    if len(s) <= 3:
        return "First"
    
    # Takahashi goes first, so we start with his move
    takahashi_move = True
    while True:
        if takahashi_move:
            # Takahashi removes a character from the middle of the string
            mid = len(s) // 2
            s = s[:mid] + s[mid+1:]
        else:
            # Aoki removes a character from the end of the string
            s = s[:-1]
        
        # Check if the string is now empty
        if not s:
            return "First"
        
        # Check if the string has two neighboring equal characters
        if len(s) > 1 and s[0] == s[1]:
            return "Second"
        
        # Switch players
        takahashi_move = not takahashi_move

def main():
    s = input()
    print(solve(s))

if __name__ == '__main__':
    main()

