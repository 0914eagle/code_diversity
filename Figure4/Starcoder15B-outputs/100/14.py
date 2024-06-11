def make_a_pile(n):
    
    pile = [n]
    i = 0
    while sum(pile) < 2 * n:
        i += 1
        if i % 2 == 0:
            pile.append(i + 2)
        else:
            pile.append(i + 1)
    return pile


