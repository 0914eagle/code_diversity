
def solve(s):
    res = 0
    for init in range(1000001):
        cur = init
        ok = True
        for i in range(1, len(s) + 1):
            res += 1
            if s[i - 1] == '+':
                cur += 1
            else:
                cur -= 1
            if cur < 0:
                ok = False
                break
        if ok:
            break
    return res

def main():
    t = int(input())
    for _ in range(t):
        s = input()
        print(solve(s))

if __name__ == '__main__':
    main()

