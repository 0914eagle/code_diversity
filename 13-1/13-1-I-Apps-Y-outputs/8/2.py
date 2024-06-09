
def find_string(n, s, t):
    res = ""
    for i in range(n):
        if s[0] == "a" and t[0] == "a":
            res += "b"
        elif s[0] == "b" and t[0] == "b":
            res += "c"
        elif s[0] == "c" and t[0] == "c":
            res += "a"
        else:
            res += s[0]
    for i in range(n):
        if s[1] == "a" and t[1] == "a":
            res += "b"
        elif s[1] == "b" and t[1] == "b":
            res += "c"
        elif s[1] == "c" and t[1] == "c":
            res += "a"
        else:
            res += s[1]
    return res

def main():
    n = int(input())
    s = input()
    t = input()
    res = find_string(n, s, t)
    if len(res) == 3*n:
        print("YES")
        print(res)
    else:
        print("NO")

if __name__ == '__main__':
    main()

