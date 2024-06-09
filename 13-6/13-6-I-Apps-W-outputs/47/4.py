
import math

def get_probability(n, m):
    total_cards = n * m
    success_cases = 0

    for i in range(1, n + 1):
        success_cases += math.comb(m, i) * math.comb(total_cards - m, n - i)

    return success_cases / math.pow(total_cards, n)

