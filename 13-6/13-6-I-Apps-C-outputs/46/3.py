
def f1(N, cards):
    # Initialize variables
    stop_counting = -1
    start_counting = -1
    counted_cards = []
    total = 0

    # Iterate through the cards
    for i, card in enumerate(cards):
        # If the card is counted, add it to the total
        if i > stop_counting and (i < start_counting or start_counting == -1):
            total += card
            counted_cards.append(card)

        # If the card is the last card, calculate the average
        if i == N - 1:
            if len(counted_cards) == 0:
                return 0
            else:
                return total / len(counted_cards)

        # If the card is the first card, set the stop_counting index
        if i == 0:
            stop_counting = i

        # If the card is the last card, set the start_counting index
        if i == N - 1:
            start_counting = i

    # If the loop completes and no average was calculated, return 0
    return 0

def f2(N, cards):
    # Initialize variables
    stop_counting = -1
    start_counting = -1
    counted_cards = []
    total = 0

    # Iterate through the cards
    for i, card in enumerate(cards):
        # If the card is counted, add it to the total
        if i > stop_counting and (i < start_counting or start_counting == -1):
            total += card
            counted_cards.append(card)

        # If the card is the last card, calculate the average
        if i == N - 1:
            if len(counted_cards) == 0:
                return 0
            else:
                return total / len(counted_cards)

        # If the card is the first card, set the stop_counting index
        if i == 0:
            stop_counting = i

        # If the card is the last card, set the start_counting index
        if i == N - 1:
            start_counting = i

    # If the loop completes and no average was calculated, return 0
    return 0

if __name__ == '__main__':
    N = int(input())
    cards = list(map(int, input().split()))
    print(f1(N, cards))
    print(f2(N, cards))

