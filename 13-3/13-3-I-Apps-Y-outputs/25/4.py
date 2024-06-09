
def simplicity(string):
    return len(set(string))

def min_erase(string):
    simplicity_value = simplicity(string)
    if simplicity_value <= 2:
        return 0
    else:
        return simplicity_value - 2

