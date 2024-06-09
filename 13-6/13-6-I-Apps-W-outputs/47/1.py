
def get_probability(n, m):
    total_cards = n * m
    successful_cases = 0

    for i in range(1, total_cards + 1):
        if i % n == 0:
            successful_cases += 1

    return successful_cases / total_cards

