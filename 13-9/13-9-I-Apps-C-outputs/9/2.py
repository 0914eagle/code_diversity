
def get_number_of_pairs(n, jaap_bet, jan_bet, thijs_bet):
    pairs = 0
    for i in range(n):
        for j in range(i+1, n):
            if jaap_bet[i] == jan_bet[i] == thijs_bet[i] and jaap_bet[j] == jan_bet[j] == thijs_bet[j]:
                pairs += 1
    return pairs

