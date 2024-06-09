
def get_divisible_pairs(d, k):
    pairs = []
    for i in range(len(d)):
        for j in range(i+1, len(d)):
            if (d[i] + d[j]) % k == 0:
                pairs.append([i, j])
    return pairs

def get_maximum_gifts(n, k, d):
    pairs = get_divisible_pairs(d, k)
    gifts = []
    for pair in pairs:
        if pair not in gifts:
            gifts.append(pair)
    return len(gifts)

def main():
    n, k = map(int, input().split())
    d = list(map(int, input().split()))
    print(get_maximum_gifts(n, k, d))

if __name__ == '__main__':
    main()

