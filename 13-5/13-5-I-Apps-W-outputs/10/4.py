
def f1(a, b):
    if a == 0 and b == 0:
        return 0
    if a == 0 and b != 0:
        return "infinity"
    if a != 0 and b == 0:
        return 1
    if a != 0 and b != 0:
        return "infinity"

def f2(a, b):
    if a == 0 and b == 0:
        return 0
    if a == 0 and b != 0:
        return "infinity"
    if a != 0 and b == 0:
        return 1
    if a != 0 and b != 0:
        return "infinity"

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(f1(a, b))
    print(f2(a, b))

