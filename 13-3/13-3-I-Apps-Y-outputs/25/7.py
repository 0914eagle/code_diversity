
def simplicity(string):
    return len(set(string))

def min_erase(string):
    simp = simplicity(string)
    if simp <= 2:
        return 0
    else:
        return simp - 2

