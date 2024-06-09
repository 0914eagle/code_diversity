
def solve(n, m):
    total_cards = n * m
    success_cases = 0

    for i in range(1, n + 1):
        success_cases += (i * (m - 1))

    return success_cases / total_cards

