def make_a_pile(n):
    
    pile = [n]
    while n > 1:
        n = n - 2 if n % 2 == 0 else n - 1
        pile.append(n)
    return pile


