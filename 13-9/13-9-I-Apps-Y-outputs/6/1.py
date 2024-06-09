
def solve(n):
    while True:
        if sum(int(i) for i in str(n)) == 0:
            return n
        n += 1

