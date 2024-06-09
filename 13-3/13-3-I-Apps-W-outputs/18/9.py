
def f1(n):
    if n == 1:
        return -1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return 2
    return 1

def f2(n):
    if n == 1:
        return -1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return 1
    return -1

if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        n = int(input())
        print(f1(n))
        print(f2(n))

