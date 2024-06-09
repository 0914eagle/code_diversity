
def give_cookies(A, B):
    if A + B < 3:
        return "Impossible"
    if A == B:
        return "Possible"
    if A > B:
        if A % 2 == 0:
            return "Possible"
        else:
            return "Impossible"
    else:
        if B % 2 == 0:
            return "Possible"
        else:
            return "Impossible"

