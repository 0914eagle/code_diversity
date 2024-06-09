
def hulk_feeling(n):
    if n == 1:
        return "I hate it"
    else:
        return "I hate that I love " + hulk_feeling(n-1)

