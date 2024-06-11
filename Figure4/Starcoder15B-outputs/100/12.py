def make_a_pile(n):
    
    pile = [n]
    while pile[-1] < 2 * n:
        pile.append(pile[-1] + 2 - (pile[-1] % 2))
    return pile


