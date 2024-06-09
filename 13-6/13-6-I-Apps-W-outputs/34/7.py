
def get_antipalindromic_permutation(s):
    n = len(s)
    if n % 2 == 1:
        return ""
    else:
        s = list(s)
        for i in range(n // 2):
            s[i], s[n - i - 1] = s[n - i - 1], s[i]
        return "".join(s)

def get_maximum_beauty(s, b):
    n = len(s)
    if n % 2 == 1:
        return 0
    else:
        s = list(s)
        for i in range(n // 2):
            s[i], s[n - i - 1] = s[n - i - 1], s[i]
        return sum(b)

if __name__ == '__main__':
    n = int(input())
    s = input()
    b = list(map(int, input().split()))
    print(get_maximum_beauty(s, b))

