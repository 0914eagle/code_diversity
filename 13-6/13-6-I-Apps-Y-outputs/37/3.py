
def has_palindrome_subsequence(a):
    n = len(a)
    for i in range(n):
        for j in range(i+2, n+1):
            if a[i] == a[j-1] and a[i+1] == a[j-2]:
                return True
    return False

def has_palindrome_subsequence_optimized(a):
    n = len(a)
    for i in range(n):
        if a[i] == a[n-i-1]:
            return True
    return False

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print("YES") if has_palindrome_subsequence_optimized(a) else print("NO")

