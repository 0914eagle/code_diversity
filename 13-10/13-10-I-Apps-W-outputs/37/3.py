
def solve(s):
    res = 0
    for i in range(len(s)):
        if s[i] == '+':
            res += 1
        else:
            res -= 1
    return res

def main():
    t = int(input())
    for i in range(t):
        s = input()
        print(solve(s))

if __name__ == '__main__':
    main()

