
def get_probability(n, m):
    total_cards = n * m
    success_cases = 0

    # Case 1: Alex takes two cards with the same value from two different decks
    success_cases += m * (m - 1) / 2

    # Case 2: Alex takes two different cards
    success_cases += total_cards * (total_cards - 1) / 2

    return success_cases / (total_cards * (total_cards - 1))

