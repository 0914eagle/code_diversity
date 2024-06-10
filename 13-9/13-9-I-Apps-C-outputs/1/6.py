
def get_card_size(cards):
    
    return set(map(tuple, cards))

def get_envelope_size(envelopes, card_size):
    
    return min(envelopes, key=lambda x: abs(x[0] * x[1] - card_size[0] * card_size[1]))

def get_wasted_paper(envelopes, cards):
    
    card_sizes = get_card_size(cards)
    total_wasted_paper = 0
    for card_size in card_sizes:
        envelope_size = get_envelope_size(envelopes, card_size)
        total_wasted_paper += (envelope_size[0] * envelope_size[1] - card_size[0] * card_size[1])
    return total_wasted_paper

def main():
    num_cards, num_envelopes = map(int, input().split())
    cards = []
    for _ in range(num_cards):
        cards.append(list(map(int, input().split())))
    wasted_paper = get_wasted_paper(range(1, num_envelopes + 1), cards)
    print(wasted_paper)

if __name__ == '__main__':
    main()

