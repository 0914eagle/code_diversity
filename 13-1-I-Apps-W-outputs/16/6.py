
def possible_matches(n, a, b):
    total_players = sum(a)
    total_umpires = sum(b)
    return total_players * (total_players - 1) // 2 * total_umpires

