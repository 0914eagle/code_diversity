
def get_gift_pairs(d, k):
    n = len(d)
    pairs = []
    for i in range(n):
        for j in range(i+1, n):
            if (d[i] + d[j]) % k == 0:
                pairs.append((i, j))
    return pairs

def get_max_gifts(d, k):
    pairs = get_gift_pairs(d, k)
    return len(pairs)

if __name__ == '__main__':
    n, k = map(int, input().split())
    d = list(map(int, input().split()))
    print(get_max_gifts(d, k))

