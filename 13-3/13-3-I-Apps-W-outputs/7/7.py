
def find_winner(n, s):
    anton_wins = s.count("A")
    danik_wins = s.count("D")
    if anton_wins > danik_wins:
        return "Anton"
    elif danik_wins > anton_wins:
        return "Danik"
    else:
        return "Friendship"

