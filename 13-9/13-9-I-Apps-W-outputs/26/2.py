
def solve(s):
    total = 0
    for i in range(0, len(s), 2):
        name = s[i]
        price = s[i+1]
        total += float(price)
    return format(total, '.2f')

