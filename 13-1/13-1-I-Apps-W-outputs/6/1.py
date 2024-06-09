
def is_valid(a, b):
    n = len(a)
    for i in range(1, int(n/2)+1):
        if a[:i] == b[n-i:] and a[i:] == b[:n-i]:
            return True
    return False

t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if is_valid(a, b):
        print("Yes")
    else:
        print("No")

