
def can_obtain_single_element(a):
    n = len(a)
    if n == 1:
        return True
    if n == 2:
        return a[0] == a[1]
    for i in range(n-1):
        for j in range(i+1, n):
            if abs(a[i] - a[j]) <= 1:
                return True
    return False

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print("YES" if can_obtain_single_element(a) else "NO")

if __name__ == '__main__':
    main()

