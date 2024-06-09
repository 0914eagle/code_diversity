
def is_palindrome(s):
    return s == s[::-1]

def cut_into_palindromes(s):
    n = len(s)
    dp = [[False] * (n+1) for _ in range(n+1)]
    palindromes = []
    for i in range(n+1):
        for j in range(i+1):
            if i == j:
                dp[i][j] = True
            elif i == j+1:
                dp[i][j] = is_palindrome(s[j:i])
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j+1] and s[j] == s[i-1]
            if dp[i][j] and i-j == j-i:
                palindromes.append(s[j:i])
    return len(palindromes), " ".join(palindromes)

def main():
    n = int(input())
    s = input()
    print(cut_into_palindromes(s))

if __name__ == '__main__':
    main()

