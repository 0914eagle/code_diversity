
def camel_race(n, jaap_bet, jan_bet, thijs_bet):
    pairs = 0
    for i in range(n):
        for j in range(i+1, n):
            if jaap_bet[i] == jan_bet[j] and jan_bet[i] == thijs_bet[j] and thijs_bet[i] == jaap_bet[j]:
                pairs += 1
    return pairs

