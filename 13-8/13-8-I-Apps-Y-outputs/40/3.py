
def is_periodic(s, k):
    if len(s) % k != 0:
        return False
    
    sub_str = s[:k]
    for i in range(len(s) // k - 1):
        if sub_str != s[i * k:(i + 1) * k]:
            return False
        sub_str = sub_str[1:] + s[i * k]
    return True

def solve(s):
    for k in range(1, len(s)):
        if is_periodic(s, k):
            return k
    return 0

if __name__ == '__main__':
    s = input()
    print(solve(s))

