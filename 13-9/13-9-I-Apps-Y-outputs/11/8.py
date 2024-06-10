
import sys

def get_monotonic_renumeration_count(a):
    n = len(a)
    count = 0
    for i in range(n):
        count += 1
        for j in range(i+1, n):
            if a[i] == a[j]:
                count -= 1
    return count % 998244353

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(get_monotonic_renumeration_count(a))

if __name__ == '__main__':
    main()

