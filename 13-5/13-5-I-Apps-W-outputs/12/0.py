
def f1(s, t):
    if len(s) < len(t):
        return "NO"
    if s == t:
        return "YES"
    for i in range(1, len(s)):
        if s[:i] + s[i+1:] == t:
            return "YES"
    return "NO"

def f2(s, t):
    if len(s) < len(t):
        return "NO"
    if s == t:
        return "YES"
    for i in range(1, len(s)):
        for j in range(i+1, len(s)):
            if s[:i] + s[j:] == t:
                return "YES"
    return "NO"

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        t = input()
        print(f1(s, t))
        print(f2(s, t))

