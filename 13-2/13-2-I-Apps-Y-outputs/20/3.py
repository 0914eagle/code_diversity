
def get_max_prettiness(a):
    
    n = len(a)
    a.sort(reverse=True)
    if n == 1:
        return a[0]
    if n == 2:
        return a[0] + a[1]
    if n == 3:
        return max(a[0] + a[1], a[1] + a[2], a[0] + a[2])
    # If n > 3, find the maximum possible cumulative prettiness by considering all possible combinations of three problems.
    max_prettiness = 0
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if a[i] % a[j] == 0 or a[i] % a[k] == 0 or a[j] % a[k] == 0:
                    continue
                prettiness = a[i] + a[j] + a[k]
                max_prettiness = max(max_prettiness, prettiness)
    return max_prettiness

def main():
    q = int(input())
    for _ in range(q):
        n = int(input())
        a = list(map(int, input().split()))
        print(get_max_prettiness(a))

if __name__ == '__main__':
    main()

