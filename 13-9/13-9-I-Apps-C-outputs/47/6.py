
def coin_flip(p):
    import random
    return random.choices(['H', 'T'], weights=[p, 1-p], k=1)[0]

def game_probability(g, k, p):
    import itertools
    import numpy as np
    
    def get_substrings(s):
        return [''.join(s[i:j+1]) for i in range(len(s)) for j in range(i, len(s))]
    
    def get_probability(g, k, p, n):
        probability = 0
        for i in range(n):
            s = ''.join(coin_flip(p) for _ in range(i+1))
            substrings = get_substrings(s)
            if g in substrings and k not in substrings:
                probability += 1/(2**i)
            elif k in substrings and g not in substrings:
                probability -= 1/(2**i)
        return probability
    
    n = 10**100
    g_probability = get_probability(g, k, p, n)
    k_probability = get_probability(k, g, p, n)
    return g_probability/(g_probability + k_probability)

def main():
    g = input()
    k = input()
    p = float(input())
    print(game_probability(g, k, p))

if __name__ == '__main__':
    main()

