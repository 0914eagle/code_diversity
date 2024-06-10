
def check_win(n, k, cards):
    # Initialize the number of moves to 0
    moves = 0
    
    # Loop through each card
    for i in range(n):
        # If the card is with a color side facing up
        if cards[i] == 1:
            # Check if the next k-1 cards also have color sides facing up
            for j in range(i+1, i+k):
                if j < n and cards[j] == 1:
                    moves += 1
                else:
                    break
        # If the card is with a color side facing down
        else:
            # Check if the previous k-1 cards also have color sides facing down
            for j in range(i-1, i-k-1, -1):
                if j >= 0 and cards[j] == 0:
                    moves += 1
                else:
                    break
    
    # If the total number of moves is greater than 10^9, return "once again"
    if moves > 10**9:
        return "once again"
    
    # If Tokitsukaze has more moves than Quailty, return "tokitsukaze"
    if moves % 2 == 1:
        return "tokitsukaze"
    # Otherwise, return "quailty"
    else:
        return "quailty"

def main():
    n, k = map(int, input().split())
    cards = list(map(int, input()))
    print(check_win(n, k, cards))

if __name__ == '__main__':
    main()

