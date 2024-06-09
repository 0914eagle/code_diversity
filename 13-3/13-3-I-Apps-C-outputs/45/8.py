
def f1(n, p, x, y):
    # Calculate the number of ways to choose two suspects
    # such that at least p coders agree with the choice
    count = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j and (i in x or i in y) and (j in x or j in y):
                count += 1
    return count

def f2(n, p, x, y):
    # Calculate the number of ways to choose two suspects
    # such that at least p coders agree with the choice
    count = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j and (i in x or i in y) and (j in x or j in y):
                count += 1
    return count

if __name__ == '__main__':
    n, p = map(int, input().split())
    x = set()
    y = set()
    for i in range(n):
        xi, yi = map(int, input().split())
        x.add(xi)
        y.add(yi)
    print(f1(n, p, x, y))
    print(f2(n, p, x, y))

