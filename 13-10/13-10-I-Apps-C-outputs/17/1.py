
def solve(n, k, cards):
    # Initialize the number of moves to 0
    moves = 0
    # Initialize the number of moves for each player to 0
    tokit_moves = 0
    quail_moves = 0
    # Initialize the number of moves for each player to win to 0
    tokit_wins = 0
    quail_wins = 0
    # Initialize the status of the cards to the input status
    card_status = cards
    # Loop until all cards have the same status
    while card_status.count('1') != card_status.count('0'):
        # Check if Tokitsukaze can make a move
        if tokit_moves < k:
            # Find the first card with color side facing down
            down_card = card_status.index('0')
            # Flip the card and the k-1 cards after it
            card_status = card_status[:down_card] + '1' + '0' * (k - 1) + card_status[down_card + k:]
            # Increment the number of moves for Tokitsukaze
            tokit_moves += 1
            # Increment the total number of moves
            moves += 1
        # Check if Quailty can make a move
        if quail_moves < k:
            # Find the first card with color side facing up
            up_card = card_status.index('1')
            # Flip the card and the k-1 cards before it
            card_status = card_status[:up_card] + '0' + '1' * (k - 1) + card_status[up_card + k:]
            # Increment the number of moves for Quailty
            quail_moves += 1
            # Increment the total number of moves
            moves += 1
        # Check if Tokitsukaze has won
        if card_status.count('1') == card_status.count('0'):
            tokit_wins += 1
        # Check if Quailty has won
        if card_status.count('1') == card_status.count('0'):
            quail_wins += 1
        # Check if the total number of moves exceeds 10^9
        if moves > 10**9:
            return "once again"
    # Return the winner
    if tokit_wins > quail_wins:
        return "tokitsukaze"
    elif quail_wins > tokit_wins:
        return "quailty"
    else:
        return "once again"

def main():
    n, k = map(int, input().split())
    cards = list(input())
    print(solve(n, k, cards))

if __name__ == '__main__':
    main()

