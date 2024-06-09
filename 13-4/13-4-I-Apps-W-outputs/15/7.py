
def f1(s1, s2, t):
    n = len(s1)
    for i in range(n):
        if s1[i] != s2[i]:
            t -= 1
            if t == 0:
                return s1[:i] + "a" + s1[i+1:]
    return "-1"

def f2(s1, s2, t):
    n = len(s1)
    for i in range(n):
        if s1[i] != s2[i]:
            t -= 1
            if t == 0:
                return s2[:i] + "a" + s2[i+1:]
    return "-1"

if __name__ == '__main__':
    n, t = map(int, input().split())
    s1 = input()
    s2 = input()
    print(f1(s1, s2, t))
    print(f2(s1, s2, t))

