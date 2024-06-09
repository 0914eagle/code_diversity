
def get_antipalindromic_permutation(s):
    n = len(s)
    if n % 2 == 1:
        return ""
    s = list(s)
    for i in range(n // 2):
        s[i], s[n - i - 1] = s[n - i - 1], s[i]
    return "".join(s)

def get_max_beauty(s, b):
    n = len(s)
    if n % 2 == 1:
        return 0
    antipalindromic_permutation = get_antipalindromic_permutation(s)
    beauty = 0
    for i in range(n):
        if s[i] == antipalindromic_permutation[i]:
            beauty += b[i]
    return beauty

if __name__ == '__main__':
    n = int(input())
    s = input()
    b = list(map(int, input().split()))
    print(get_max_beauty(s, b))

