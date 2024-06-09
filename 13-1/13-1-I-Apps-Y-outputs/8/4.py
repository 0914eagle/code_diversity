
def find_string(n, s, t):
    res = ""
    for i in range(n):
        if i % 3 == 0:
            res += "a"
        elif i % 3 == 1:
            res += "b"
        else:
            res += "c"
    if s in res or t in res:
        return "NO"
    return "YES\n" + res

if __name__ == '__main__':
    n = int(input())
    s = input()
    t = input()
    print(find_string(n, s, t))

