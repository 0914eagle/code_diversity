
def get_winner(s):
    if len(s) == 3:
        return "First"
    
    # Initialize variables
    takahashi_moves = 0
    aoki_moves = 0
    i = 1
    
    # Loop through the string
    while i < len(s) - 1:
        # Takahashi's move
        if s[i] != s[i - 1] and s[i] != s[i + 1]:
            takahashi_moves += 1
            i += 1
        # Aoki's move
        else:
            aoki_moves += 1
            i += 1
    
    # Check if Takahashi or Aoki has more moves
    if takahashi_moves > aoki_moves:
        return "First"
    elif takahashi_moves < aoki_moves:
        return "Second"
    else:
        return "Draw"

def main():
    s = input()
    print(get_winner(s))

if __name__ == '__main__':
    main()

