
def hulk_feelings(n):
    if n == 1:
        return "I hate it"
    else:
        return "I hate that " + hulk_feelings(n-1)

