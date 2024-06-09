
def anton_and_danik(n, s):
    anton_wins = 0
    danik_wins = 0
    for game in s:
        if game == "A":
            anton_wins += 1
        else:
            danik_wins += 1
    
    if anton_wins > danik_wins:
        return "Anton"
    elif danik_wins > anton_wins:
        return "Danik"
    else:
        return "Friendship"

