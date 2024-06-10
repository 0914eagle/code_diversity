
def get_pairs(n, k, a):
    pairs = 0
    for i in range(n):
        for j in range(i+1, n):
            x = a[i] * a[j]
            if x ** (1/k) % 1 == 0:
                pairs += 1
    return pairs

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(get_pairs(n, k, a))

if __name__ == '__main__':
    main()

