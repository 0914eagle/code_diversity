def make_a_pile(n):
    
    pile = [n]
    while pile[-1] < 2 * n - 1:
        pile.append(pile[-1] + 2) if pile[-1] % 2 == 1 else pile.append(pile[-1] + 1)
    return pile


