
def count_almost_palindromic_substrings(s, l, r):
    count = 0
    for i in range(l-1, r):
        count += is_almost_palindromic(s[i:r])
    return count

def is_almost_palindromic(sub):
    return sub == sub[::-1] or sub[:-2] == sub[:-2][::-1] or sub[1:] == sub[1:][::-1]

if __name__ == "__main__":
    n, q = map(int, input().split())
    s = input().strip()
    
    for _ in range(q):
        l, r = map(int, input().split())
        print(count_almost_palindromic_substrings(s, l, r))
