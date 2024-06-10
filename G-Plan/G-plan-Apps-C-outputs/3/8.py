
def count_almost_palindromic_substrings(s, l, r):
    count = 0
    for i in range(l-1, r):
        count += check_almost_palindromic(s[i:r])
    return count

def check_almost_palindromic(sub):
    if sub == sub[::-1]:
        return len(sub)
    for i in range(len(sub)):
        for j in range(i+1, len(sub)):
            if sub[:i] + sub[j] + sub[i+1:j] + sub[i] + sub[j+1:] == sub[:j+1]:
                return j - i + 1
    return 0

if __name__ == "__main__":
    n, q = map(int, input().split())
    s = input().strip()
    for _ in range(q):
        l, r = map(int, input().split())
        print(count_almost_palindromic_substrings(s, l, r))
