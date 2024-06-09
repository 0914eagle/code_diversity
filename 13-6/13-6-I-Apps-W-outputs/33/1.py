
def is_adorable(s):
    n = len(s)
    if n % 2 == 1:
        return False
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            return False
    return True

def can_be_split(s):
    n = len(s)
    for i in range(1, n):
        if is_adorable(s[:i]) and is_adorable(s[i:]):
            return True
    return False

if __name__ == '__main__':
    s = input()
    print("Yes") if can_be_split(s) else print("No")

