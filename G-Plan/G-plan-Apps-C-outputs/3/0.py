
def count_almost_palindromic_substrings(s, l, r):
    count = 0
    for i in range(l-1, r):
        count += check_palindrome(s[i:r])
    return count

def check_palindrome(sub):
    if sub == sub[::-1]:
        return 1
    for i in range(len(sub)//2):
        if sub[i] != sub[-i-1]:
            return 1
    return 0

if __name__ == "__main__":
    n, q = map(int, input().split())
    string = input().strip()
    
    for _ in range(q):
        l, r = map(int, input().split())
        print(count_almost_palindromic_substrings(string, l, r))
