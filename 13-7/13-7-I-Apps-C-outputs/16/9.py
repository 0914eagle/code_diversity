
def get_cards_sequence(oranges, apples):
    # Check if the input is valid
    if oranges <= 0 or apples <= 0 or oranges > 10**18 or apples > 10**18 or oranges * apples == 0:
        return "Impossible"
    
    # Initialize the variables
    cards = []
    oranges_alice, apples_alice = oranges, apples
    oranges_bob, apples_bob = 0, 0
    
    # Play the game
    while oranges_alice > 0 and apples_alice > 0:
        # Alice's turn
        if oranges_alice % 2 == 0:
            cards.append("A")
            oranges_bob += oranges_alice // 2
            apples_bob += apples_alice // 2
            oranges_alice = oranges_alice // 2
            apples_alice = apples_alice // 2
        else:
            cards.append("B")
            oranges_alice -= 1
            apples_alice -= 1
            oranges_bob += 1
            apples_bob += 1
        
        # Bob's turn
        if oranges_bob % 2 == 0:
            cards.append("B")
            oranges_alice += oranges_bob // 2
            apples_alice += apples_bob // 2
            oranges_bob = oranges_bob // 2
            apples_bob = apples_bob // 2
        else:
            cards.append("A")
            oranges_bob -= 1
            apples_bob -= 1
            oranges_alice += 1
            apples_alice += 1
    
    # Compress the sequence of cards
    compressed_cards = []
    count = 1
    for i in range(len(cards) - 1):
        if cards[i] == cards[i + 1]:
            count += 1
        else:
            compressed_cards.append(str(count))
            compressed_cards.append(cards[i])
            count = 1
    compressed_cards.append(str(count))
    compressed_cards.append(cards[-1])
    
    return "".join(compressed_cards)

