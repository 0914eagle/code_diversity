
def find_winner(n, s):
    count_a = s.count('A')
    count_d = s.count('D')
    if count_a > count_d:
        return "Anton"
    elif count_d > count_a:
        return "Danik"
    else:
        return "Friendship"

