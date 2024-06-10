
def recycle(e, f, c):
    sodas = 0
    while e + f >= c:
        sodas += 1
        e += f
        f = 0
    return sodas

def drink_sodas(e, f, c, extra):
    sodas = recycle(e, f, c)
    sodas += extra
    return sodas

if __name__ == '__main__':
    e, f, c = map(int, input().split())
    extra = int(input())
    print(drink_sodas(e, f, c, extra))

