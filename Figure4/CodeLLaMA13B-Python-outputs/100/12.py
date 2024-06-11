def make_a_pile(n):
    
    pile = []
    while n > 0:
        pile.append(n)
        if n % 2 == 0:
            n = n - 1
        else:
            n = n + 1
    return pile


