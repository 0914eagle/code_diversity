
def f1(s):
    n = len(s)
    if n == 1:
        return 0
    else:
        count = 0
        for i in range(n-1):
            if s[i] != s[i+1]:
                count += 1
        return count

def f2(s):
    n = len(s)
    if n == 1:
        return 0
    else:
        count = 0
        for i in range(n-1):
            if s[i] == s[i+1]:
                count += 1
        return count

if __name__ == '__main__':
    s = input()
    print(f1(s))
    print(f2(s))

