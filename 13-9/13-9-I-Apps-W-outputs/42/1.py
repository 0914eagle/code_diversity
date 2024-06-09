
def solve(n):
    if n == 1:
        return "I hate it"
    else:
        return "I hate that I love that " + solve(n-1)

