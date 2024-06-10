
def get_g_k_strings():
    g = input()
    k = input()
    return g, k

def get_p_coin_flip():
    p = float(input())
    return p

def get_probability_gon_wins(g, k, p):
    g_len = len(g)
    k_len = len(k)
    probability_g_wins = 0
    probability_k_wins = 0
    probability_draw = 0
    for i in range(100):
        probability_g_wins += (g_len / (g_len + k_len)) * (1 - p) ** i
        probability_k_wins += (k_len / (g_len + k_len)) * p ** i
        probability_draw += (1 - p) ** i * (1 - (g_len / (g_len + k_len)) * (1 - p) ** i)
    return probability_g_wins, probability_k_wins, probability_draw

def main():
    g, k = get_g_k_strings()
    p = get_p_coin_flip()
    probability_g_wins, probability_k_wins, probability_draw = get_probability_gon_wins(g, k, p)
    print(probability_g_wins)

if __name__ == '__main__':
    main()

