
def solve(x):
    while x > 9:
        x = sum(int(i) for i in str(x) if i != '0')
    return x

