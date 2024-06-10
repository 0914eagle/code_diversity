
def check_winner(n, k, cards):
    # Initialize variables
    num_moves = 0
    flipped_cards = []
    same_side = True
    
    # Loop through the cards
    for i in range(n):
        # Check if the card is already flipped
        if cards[i] == "1":
            continue
        
        # Check if the card is flippable
        if i + k - 1 < n and cards[i + k - 1] == "1":
            flipped_cards.append(i)
            num_moves += 1
            continue
        
        # Check if the card is on the edge
        if i < k or i + k - 1 == n:
            continue
        
        # Check if the card is facing the same side as the previous card
        if cards[i] == cards[i - 1]:
            continue
        
        # Check if the card is facing the same side as the next card
        if cards[i] == cards[i + 1]:
            continue
        
        # The card is not flippable, not on the edge, and not facing the same side as the previous or next card
        return "once again"
    
    # Check if Tokitsukaze can win
    if len(flipped_cards) > 0 and len(flipped_cards) % 2 == 0:
        return "tokitsukaze"
    
    # Check if Quailty can win
    if len(flipped_cards) > 0 and len(flipped_cards) % 2 == 1:
        return "quailty"
    
    # Check if the game can end in a draw
    if num_moves > 1000000000:
        return "once again"
    
    # No winner or draw
    return "tokitsukaze"

def main():
    n, k = map(int, input().split())
    cards = input()
    print(check_winner(n, k, cards))

if __name__ == '__main__':
    main()

