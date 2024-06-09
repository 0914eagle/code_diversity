
def get_pairs(n, a):
    pairs = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if a[i] & a[j] >= a[i] ^ a[j]:
                pairs += 1
    return pairs

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(get_pairs(n, a))

if __name__ == '__main__':
    main()

