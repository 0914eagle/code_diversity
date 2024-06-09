
def find_winner(n, s):
    a_count = s.count('A')
    d_count = s.count('D')
    if a_count > d_count:
        return "Anton"
    elif a_count < d_count:
        return "Danik"
    else:
        return "Friendship"

