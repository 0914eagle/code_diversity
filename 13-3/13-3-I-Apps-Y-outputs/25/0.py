
def simplify_string(s):
    return len(set(s))

def min_erase_count(s):
    simplicity = simplify_string(s)
    if simplicity <= 2:
        return 0
    else:
        return simplicity - 2

