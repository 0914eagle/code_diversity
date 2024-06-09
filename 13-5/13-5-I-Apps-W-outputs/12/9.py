
def f1(s, t):
    if len(s) == 0:
        return False
    if s == t:
        return True
    for i in range(1, len(s)):
        if f1(s[i:], t):
            return True
    return False

def f2(s, t):
    if len(s) == 0:
        return False
    if s == t:
        return True
    for i in range(1, len(s)):
        if f2(s[:i], t):
            return True
    return False

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()
        t = input()
        if f1(s, t) or f2(s, t):
            print("YES")
        else:
            print("NO")

