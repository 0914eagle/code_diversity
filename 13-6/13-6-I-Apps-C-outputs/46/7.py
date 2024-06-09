
def get_counted_cards(cards):
    counted_cards = []
    for i, card in enumerate(cards):
        if i == 0 or card != cards[i - 1]:
            counted_cards.append(card)
    return counted_cards

def get_payout(counted_cards):
    if len(counted_cards) == 0:
        return 0.0
    return sum(counted_cards) / len(counted_cards)

def solve(cards):
    counted_cards = get_counted_cards(cards)
    return get_payout(counted_cards)

if __name__ == '__main__':
    num_cards = int(input())
    cards = list(map(int, input().split()))
    print(solve(cards))

