
def solve(n):
    if n % 2 == 1:
        return "Weird"
    elif n % 2 == 0 and 2 <= n <= 5:
        return "Not Weird"
    elif n % 2 == 0 and 6 <= n <= 20:
        return "Weird"
    else:
        return "Not Weird"

