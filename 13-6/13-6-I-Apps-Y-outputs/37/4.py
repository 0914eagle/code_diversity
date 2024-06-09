
def has_palindrome_subsequence(a):
    # Your code here
    pass

def get_palindrome_subsequence(a):
    # Your code here
    pass

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        if has_palindrome_subsequence(a):
            print("YES")
        else:
            print("NO")

