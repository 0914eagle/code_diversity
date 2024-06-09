
def get_max_prettiness(a):
    n = len(a)
    a.sort(reverse=True)
    if n == 1:
        return a[0]
    if n == 2:
        return a[0] + a[1]
    if n == 3:
        return a[0] + a[1] + a[2]
    max_prettiness = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if a[i] % a[j] == 0 or a[j] % a[i] == 0:
                continue
            for k in range(j+1, n):
                if a[i] % a[k] == 0 or a[j] % a[k] == 0 or a[k] % a[i] == 0 or a[k] % a[j] == 0:
                    continue
                max_prettiness = max(max_prettiness, a[i] + a[j] + a[k])
    return max_prettiness

q = int(input())
for i in range(q):
    n = int(input())
    a = list(map(int, input().split()))
    print(get_max_prettiness(a))

