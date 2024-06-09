
def get_antipalindromic_permutation(s):
    n = len(s)
    if n % 2 == 1:
        return ""
    else:
        permutation = ""
        for i in range(n // 2):
            permutation += s[i]
        for i in range(n // 2, n):
            permutation += s[n - 1 - i]
        return permutation

def get_beauty(s, b):
    n = len(s)
    beauty = 0
    for i in range(n):
        beauty += b[i]
    return beauty

def main():
    n = int(input())
    s = input()
    b = list(map(int, input().split()))
    permutation = get_antipalindromic_permutation(s)
    beauty = get_beauty(permutation, b)
    print(beauty)

if __name__ == '__main__':
    main()

