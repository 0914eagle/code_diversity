def make_a_pile(n):
    
    pile = []
    for i in range(n):
        if i % 2 == 0:
            pile.append(i + 3)
        else:
            pile.append(i + 4)
    return pile


