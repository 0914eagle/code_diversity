
def get_hulk_feeling(n):
    if n == 1:
        return "I hate it"
    else:
        return "I hate that " + get_hulk_feeling(n-1)

