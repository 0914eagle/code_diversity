def make_a_pile(n):
    
    pile = [n]
    while pile[-1] < 2 * n - 1:
        if pile[-1] % 2 == 0:
            pile.append(pile[-1] + 2)
        else:
            pile.append(pile[-1] + 1)
    return pile


