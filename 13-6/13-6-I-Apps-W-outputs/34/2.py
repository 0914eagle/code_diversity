
def get_antipalindromic_permutation(s):
    n = len(s)
    if n % 2 == 1:
        return ""
    else:
        s = list(s)
        for i in range(n // 2):
            s[i], s[n - i - 1] = s[n - i - 1], s[i]
        return "".join(s)

def get_beauty(s, b):
    n = len(s)
    beauty = 0
    for i in range(n):
        if s[i] == s[n - i - 1]:
            beauty += b[i]
    return beauty

def get_maximum_beauty(s, b):
    n = len(s)
    max_beauty = 0
    for i in range(n):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                continue
            else:
                s_temp = s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:]
                beauty = get_beauty(s_temp, b)
                if beauty > max_beauty:
                    max_beauty = beauty
    return max_beauty

def main():
    n = int(input())
    s = input()
    b = list(map(int, input().split()))
    antipalindromic_permutation = get_antipalindromic_permutation(s)
    maximum_beauty = get_maximum_beauty(antipalindromic_permutation, b)
    print(maximum_beauty)

if __name__ == '__main__':
    main()

