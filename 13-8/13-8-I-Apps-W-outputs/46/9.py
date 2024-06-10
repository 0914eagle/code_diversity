
def get_suitable_pairs(n, k, a):
    suitable_pairs = 0
    for i in range(n):
        for j in range(i+1, n):
            x = a[i] * a[j]
            if x ** (1/k) % 1 == 0:
                suitable_pairs += 1
    return suitable_pairs

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(get_suitable_pairs(n, k, a))

if __name__ == '__main__':
    main()

