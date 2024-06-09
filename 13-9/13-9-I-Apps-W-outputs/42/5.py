
def express_feeling(n):
    if n == 1:
        return "I hate it"
    else:
        return "I hate that " + express_feeling(n-1)

