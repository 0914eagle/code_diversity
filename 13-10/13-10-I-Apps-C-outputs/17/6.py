
def check_moves(n, k, cards):
    # Initialize variables
    tokens = ["tokitsukaze", "quailty"]
    token_index = 0
    moves = 0
    
    # Loop through each card
    for i in range(n):
        # Check if card is face up
        if cards[i] == "1":
            # Check if there are consecutive cards with the same color
            for j in range(i+1, min(i+k, n)):
                if cards[j] == cards[i]:
                    # Flip all consecutive cards with the same color
                    for k in range(i, j+1):
                        cards[k] = "1" if cards[k] == "0" else "0"
                    token_index = 1 - token_index
                    moves += 1
                    break
    
    # Check if the game can end in a draw
    if moves > 10**9:
        return "once again"
    
    # Check if Tokitsukaze will win
    if token_index == 0:
        return tokens[0]
    
    # Check if Quailty will win
    if token_index == 1:
        return tokens[1]
    
    # If neither of them will win, the game will end in a draw
    return "once again"

def main():
    n, k = map(int, input().split())
    cards = list(input())
    print(check_moves(n, k, cards))

if __name__ == '__main__':
    main()

