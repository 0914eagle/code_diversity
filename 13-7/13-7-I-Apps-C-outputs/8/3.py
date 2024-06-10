
def is_winning_move(n, k, cards):
    # Initialize variables
    num_color_sides_up = 0
    num_color_sides_down = 0
    consecutive_color_sides = 0
    consecutive_color_sides_up = 0
    consecutive_color_sides_down = 0
    
    # Loop through the cards
    for i in range(n):
        # Check if the current card has a color side up
        if cards[i] == "1":
            num_color_sides_up += 1
        else:
            num_color_sides_down += 1
        
        # Check if the current card is part of a consecutive run of color sides
        if i > 0 and cards[i] == cards[i-1]:
            consecutive_color_sides += 1
            if cards[i] == "1":
                consecutive_color_sides_up += 1
            else:
                consecutive_color_sides_down += 1
        else:
            consecutive_color_sides = 1
            if cards[i] == "1":
                consecutive_color_sides_up = 1
            else:
                consecutive_color_sides_down = 1
        
        # Check if the current move would result in all color sides facing the same direction
        if consecutive_color_sides == k and consecutive_color_sides_up > 0 and consecutive_color_sides_down > 0:
            return True
    
    # Check if the current move would result in all color sides facing the same direction
    if num_color_sides_up == k or num_color_sides_down == k:
        return True
    
    # If the current move would not result in all color sides facing the same direction, return False
    return False

def get_winner(n, k, cards):
    # Check if Tokitsukaze will win
    if is_winning_move(n, k, cards):
        return "tokitsukaze"
    
    # Check if Quailty will win
    if is_winning_move(n, k, list(reversed(cards))):
        return "quailty"
    
    # If neither Tokitsukaze nor Quailty will win, return "once again"
    return "once again"

def main():
    n, k = map(int, input().split())
    cards = list(input())
    print(get_winner(n, k, cards))

if __name__ == '__main__':
    main()

