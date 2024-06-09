
def solve(n, m):
    total_cards = n * m
    success_cases = 0

    for i in range(1, total_cards + 1):
        if i % n == 0:
            success_cases += 1

    return success_cases / total_cards

