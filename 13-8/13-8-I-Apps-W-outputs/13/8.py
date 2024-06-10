
def is_good(s):
    count_zero = 0
    count_one = 0
    for c in s:
        if c == '0':
            count_zero += 1
        else:
            count_one += 1
    return count_zero != count_one

def solve(s):
    if len(s) == 1:
        return 1, s
    
    for i in range(1, len(s)):
        if is_good(s[:i]):
            k, ss = solve(s[i:])
            return k + 1, s[:i] + ' ' + ss
    
    return 1, s

def main():
    n = int(input())
    s = input()
    k, ss = solve(s)
    print(k)
    print(ss)

if __name__ == '__main__':
    main()

