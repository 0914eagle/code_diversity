
def get_card_info(n):
    card_info = []
    for i in range(n):
        w, h, q = map(int, input().split())
        card_info.append((w, h, q))
    return card_info

def get_envelope_info(k):
    envelope_info = []
    for i in range(k):
        w, h = map(int, input().split())
        envelope_info.append((w, h))
    return envelope_info

def get_min_waste(card_info, envelope_info):
    # Initialize variables
    n = len(card_info)
    k = len(envelope_info)
    waste = 0

    # Sort the card info by area
    card_info.sort(key=lambda x: x[0] * x[1])

    # Loop through the cards and find the best envelope match
    for i in range(n):
        card = card_info[i]
        # Find the first envelope that is large enough
        for j in range(k):
            envelope = envelope_info[j]
            if card[0] <= envelope[0] and card[1] <= envelope[1]:
                break
        # Calculate the waste for this card
        waste += (envelope[0] * envelope[1]) - (card[0] * card[1])

    return waste

def main():
    n, k = map(int, input().split())
    card_info = get_card_info(n)
    envelope_info = get_envelope_info(k)
    waste = get_min_waste(card_info, envelope_info)
    print(waste)

if __name__ == '__main__':
    main()

