
def f1(n, k):
    if n % 2 == 0:
        return f2(n, k, 0)
    else:
        return f2(n, k, 1)

def f2(n, k, parity):
    if k == 1:
        return [n]
    else:
        for i in range(1, n + 1):
            if i % 2 == parity:
                result = f2(n - i, k - 1, parity)
                if result != -1:
                    return [i] + result
        return -1

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        result = f1(n, k)
        if result == -1:
            print("NO")
        else:
            print("YES")
            print(" ".join(map(str, result)))

