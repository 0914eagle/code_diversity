
def f1(s, t):
    if len(s) == 0:
        return "NO"
    if s == t:
        return "YES"
    if len(s) == 1:
        return "NO"
    if s[0] == t[0]:
        return f1(s[1:], t[1:])
    if s[-1] == t[-1]:
        return f1(s[:-1], t[:-1])
    return "NO"

def f2(s, t):
    if len(s) == 0:
        return "NO"
    if s == t:
        return "YES"
    if len(s) == 1:
        return "NO"
    if s[0] == t[0]:
        return f2(s[1:], t[1:])
    if s[-1] == t[-1]:
        return f2(s[:-1], t[:-1])
    return "NO"

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        t = input()
        print(f1(s, t))
        print(f2(s, t))

