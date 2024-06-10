
def get_wasted_paper(cards, envelopes):
    # Calculate the total wasted paper for each card type
    wasted_paper = [envelopes[0] - card[0] * card[1] for card in cards]
    
    # Calculate the total wasted paper for all card types
    total_wasted_paper = sum(wasted_paper)
    
    return total_wasted_paper

def get_envelope_sizes(cards, k):
    # Sort the cards by their area in decreasing order
    cards.sort(key=lambda x: x[0] * x[1], reverse=True)
    
    # Initialize the envelope sizes
    envelope_sizes = [0] * k
    
    # Fill the envelopes with the largest cards first
    for i in range(k):
        envelope_sizes[i] = cards[i][0]
    
    return envelope_sizes

def get_min_wasted_paper(cards, k):
    # Get the envelope sizes
    envelope_sizes = get_envelope_sizes(cards, k)
    
    # Calculate the wasted paper for each card type
    wasted_paper = [envelope_sizes[0] - card[0] * card[1] for card in cards]
    
    # Calculate the total wasted paper
    total_wasted_paper = sum(wasted_paper)
    
    return total_wasted_paper

if __name__ == '__main__':
    n, k = map(int, input().split())
    cards = []
    for _ in range(n):
        w, h, q = map(int, input().split())
        cards.append((w, h, q))
    
    print(get_min_wasted_paper(cards, k))

