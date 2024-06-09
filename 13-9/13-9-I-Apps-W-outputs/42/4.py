
def express_feeling(n):
    if n == 1:
        return "I hate it"
    else:
        return "I hate that I love " + express_feeling(n-1)

