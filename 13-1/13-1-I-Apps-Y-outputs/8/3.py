
def find_string(n, s, t):
    res = ""
    for i in range(n):
        if s[0] == "a" and t[0] == "a":
            res += "b"
        elif s[0] == "b" and t[0] == "b":
            res += "c"
        else:
            res += "a"
    for i in range(n):
        if s[1] == "a" and t[1] == "a":
            res += "b"
        elif s[1] == "b" and t[1] == "b":
            res += "c"
        else:
            res += "a"
    return res

def main():
    n = int(input())
    s = input()
    t = input()
    res = find_string(n, s, t)
    if res == "":
        print("NO")
    else:
        print("YES")
        print(res)

if __name__ == '__main__':
    main()

