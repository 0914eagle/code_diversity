
def count_almost_palindromic_substrings(s, l, r):
    count = 0
    for i in range(l-1, r):
        count += is_almost_palindromic(s[i:r])
    return count

def is_almost_palindromic(substring):
    return substring == substring[::-1] or can_be_palindrome(substring)

def can_be_palindrome(substring):
    return any(substring[:i] + substring[j] + substring[i+1:j] + substring[i] + substring[j+1:] == substring[::-1] for i in range(len(substring) - 1) for j in range(i+1, len(substring)))

if __name__ == '__main__':
    n, q = map(int, input().split())
    s = input().strip()
    for _ in range(q):
        l, r = map(int, input().split())
        print(count_almost_palindromic_substrings(s, l, r))
