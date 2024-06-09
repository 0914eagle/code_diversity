
def get_max_prettiness(a):
    n = len(a)
    a.sort(reverse=True)
    max_prettiness = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if a[i] % a[j] == 0 or a[i] % a[k] == 0 or a[j] % a[k] == 0:
                    continue
                max_prettiness = max(max_prettiness, a[i] + a[j] + a[k])
    return max_prettiness

q = int(input())
for i in range(q):
    n = int(input())
    a = list(map(int, input().split()))
    print(get_max_prettiness(a))

