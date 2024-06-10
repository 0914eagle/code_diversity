
def get_winner(n, k, deck):
    # Initialize the variables
    total_moves = 0
    card_flips = []
    card_color = []
    
    # Get the initial card color
    for i in range(n):
        if deck[i] == "1":
            card_color.append(1)
        else:
            card_color.append(0)
    
    # Loop until the game ends
    while True:
        # Tokitsukaze's move
        card_flips.append(k)
        total_moves += 1
        if total_moves > 10**9:
            return "once again"
        
        # Quailty's move
        card_flips.append(k)
        total_moves += 1
        if total_moves > 10**9:
            return "once again"
        
        # Check if the game ends
        if all(card_color) or not any(card_color):
            if any(card_color):
                return "tokitsukaze"
            else:
                return "quailty"
        
        # Update the card color
        for i in range(n):
            if card_flips[i] == 0:
                continue
            if card_color[i] == 0:
                card_color[i] = 1
            else:
                card_color[i] = 0
    
    # If the game doesn't end, it's a draw
    return "once again"

def main():
    n, k = map(int, input().split())
    deck = input()
    print(get_winner(n, k, deck))

if __name__ == '__main__':
    main()

