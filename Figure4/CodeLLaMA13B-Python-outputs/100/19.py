def make_a_pile(n):
    
    pile = []
    while n > 0:
        pile.append(n)
        if n % 2 == 0:
            n -= 1
        else:
            n -= 2
    return pile


