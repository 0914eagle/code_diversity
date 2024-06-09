
def is_palindrome(s):
    return s == s[::-1]

def cut_into_palindromes(s):
    n = len(s)
    if n == 1:
        return 1, [s]

    for i in range(1, n):
        if is_palindrome(s[:i]):
            j = n - i
            if is_palindrome(s[i:j]):
                return 2, [s[:i], s[i:j]]

    return 1, [s]

def main():
    n = int(input())
    s = input()
    k, palindromes = cut_into_palindromes(s)
    print(k)
    print(" ".join(palindromes))

if __name__ == '__main__':
    main()

