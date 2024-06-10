
import math

def get_probability_of_win(g, k, p):
    # Initialize variables
    n = len(g)
    m = len(k)
    prob_g_win = 0
    prob_k_win = 0
    
    # Calculate the probability of Gon winning on the first turn
    if g[0] == 'H':
        prob_g_win = p
    elif g[0] == 'T':
        prob_g_win = 1 - p
    else:
        raise ValueError("Invalid input")
    
    # Calculate the probability of Killua winning on the first turn
    if k[0] == 'H':
        prob_k_win = 1 - p
    elif k[0] == 'T':
        prob_k_win = p
    else:
        raise ValueError("Invalid input")
    
    # Calculate the probability of Gon winning on subsequent turns
    for i in range(1, n):
        prob_g_win *= p
        prob_g_win += (1 - p) * (prob_k_win ** (m - i))
    
    # Calculate the probability of Killua winning on subsequent turns
    for i in range(1, m):
        prob_k_win *= p
        prob_k_win += (1 - p) * (prob_g_win ** (n - i))
    
    return prob_g_win

def get_probability_of_draw(g, k, p):
    # Initialize variables
    n = len(g)
    m = len(k)
    prob_draw = 0
    
    # Calculate the probability of a draw on the first turn
    if g[0] == 'H' and k[0] == 'H':
        prob_draw = p ** 2
    elif g[0] == 'H' and k[0] == 'T':
        prob_draw = 2 * p * (1 - p)
    elif g[0] == 'T' and k[0] == 'H':
        prob_draw = 2 * p * (1 - p)
    elif g[0] == 'T' and k[0] == 'T':
        prob_draw = (1 - p) ** 2
    else:
        raise ValueError("Invalid input")
    
    # Calculate the probability of a draw on subsequent turns
    for i in range(1, n):
        prob_draw *= p
        prob_draw += (1 - p) * (prob_draw ** (m - i))
    
    return prob_draw

if __name__ == '__main__':
    g = input()
    k = input()
    p = float(input())
    prob_g_win = get_probability_of_win(g, k, p)
    prob_draw = get_probability_of_draw(g, k, p)
    print(prob_g_win)

