
def has_palindromic_subsequence(a):
    n = len(a)
    for i in range(n - 2):
        for j in range(i + 1, n):
            if a[i] == a[j] and a[i + 1] == a[j - 1]:
                return True
    return False

def has_palindromic_subsequence_of_length_at_least_3(a):
    n = len(a)
    for i in range(n - 2):
        for j in range(i + 1, n):
            if a[i] == a[j] and a[i + 1] == a[j - 1] and j - i >= 2:
                return True
    return False

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        if has_palindromic_subsequence_of_length_at_least_3(a):
            print("YES")
        else:
            print("NO")

