
def get_palindromic_strings(s):
    n = len(s)
    palindromic_strings = 0
    for i in range(n):
        for j in range(i+1, n+1):
            substring = s[i:j]
            if substring == substring[::-1]:
                palindromic_strings += 1
    return palindromic_strings

def get_subsequence_count(s, n):
    count = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substring = s[i:j]
            if len(substring) == n:
                count += 1
    return count

def get_answer(s):
    n = len(s)
    palindromic_strings = get_palindromic_strings(s)
    subsequence_count = get_subsequence_count(s, 2*n)
    return (palindromic_strings * subsequence_count) % (10**9 + 7)

if __name__ == '__main__':
    n = int(input())
    s = input()
    print(get_answer(s))

