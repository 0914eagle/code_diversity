
def f1(s, a, b):
    if len(s) < a:
        return "NO"
    if len(s) < b:
        return "YES"
    if s[:b].count("X") == b:
        return "NO"
    if s[a-b:a].count("X") == b:
        return "YES"
    return "NO"

def f2(s, a, b):
    if len(s) < a:
        return "NO"
    if len(s) < b:
        return "YES"
    if s[:b].count("X") == b:
        return "NO"
    if s[a-b:a].count("X") == b:
        return "YES"
    return "NO"

if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        a, b = map(int, input().split())
        s = input()
        print(f1(s, a, b))
        print(f2(s, a, b))

