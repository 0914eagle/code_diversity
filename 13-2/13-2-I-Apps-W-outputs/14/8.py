
def f1(s, a, b):
    if len(s) < a:
        return "NO"
    if len(s) < b:
        return "YES"
    if s[0] == "X":
        return "NO"
    if s[a-1] == "X":
        return "YES"
    return "NO"

def f2(s, a, b):
    if len(s) < a:
        return "NO"
    if len(s) < b:
        return "YES"
    if s[0] == "X":
        return "NO"
    if s[a-1] == "X":
        return "YES"
    return "NO"

if __name__ == '__main__':
    q = int(input())
    for i in range(q):
        a, b = map(int, input().split())
        s = input()
        print(f1(s, a, b))
        print(f2(s, a, b))

