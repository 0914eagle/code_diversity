
import sys

def get_monotonic_renumberings(a):
    n = len(a)
    renum = [0] * n
    for i in range(n):
        if i == 0:
            renum[i] = 0
        else:
            if a[i] == a[i-1]:
                renum[i] = renum[i-1]
            else:
                renum[i] = renum[i-1] + 1
    return renum

def count_monotonic_renumberings(a):
    n = len(a)
    renum = get_monotonic_renumberings(a)
    count = 1
    for i in range(n-1):
        if renum[i] == renum[i+1]:
            count *= 2
        else:
            count *= 2 - 1
    return count % 998244353

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(count_monotonic_renumberings(a))

if __name__ == '__main__':
    main()

