
def solve(a):
    n = len(a)
    for i in range(n):
        for j in range(i+1, n):
            if a[i] + a[j] % 2 == 0:
                return [i+1, j+1]
    return -1

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(solve(a))

if __name__ == '__main__':
    main()

