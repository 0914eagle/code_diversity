
def get_card_dimensions(n):
    card_dimensions = []
    for i in range(n):
        w, h, q = map(int, input().split())
        card_dimensions.append((w, h, q))
    return card_dimensions

def get_envelope_dimensions(k):
    envelope_dimensions = []
    for i in range(k):
        w, h = map(int, input().split())
        envelope_dimensions.append((w, h))
    return envelope_dimensions

def get_wasted_paper(card_dimensions, envelope_dimensions):
    wasted_paper = 0
    for card in card_dimensions:
        for envelope in envelope_dimensions:
            if card[0] <= envelope[0] and card[1] <= envelope[1]:
                wasted_paper += (envelope[0] * envelope[1]) - (card[0] * card[1])
                break
    return wasted_paper

def main():
    n, k = map(int, input().split())
    card_dimensions = get_card_dimensions(n)
    envelope_dimensions = get_envelope_dimensions(k)
    wasted_paper = get_wasted_paper(card_dimensions, envelope_dimensions)
    print(wasted_paper)

if __name__ == '__main__':
    main()

