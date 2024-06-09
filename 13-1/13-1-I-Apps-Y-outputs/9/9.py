
def f1(a, b, c):
    return sorted([a, b, c])

def f2(a, b, c):
    return [a, c, b]

if __name__ == '__main__':
    a, b, c = map(int, input().split())
    print(*f1(a, b, c))

