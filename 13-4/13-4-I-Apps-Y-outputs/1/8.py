
def get_compatible_pairs(l, r):
    n = len(l)
    pairs = []
    for i in range(n):
        for j in range(i+1, n):
            if l[i] == r[j] or l[i] == "?" or r[j] == "?":
                pairs.append([i, j])
    return pairs

def get_max_compatible_pairs(l, r):
    pairs = get_compatible_pairs(l, r)
    max_pairs = []
    for pair in pairs:
        if pair not in max_pairs:
            max_pairs.append(pair)
    return max_pairs

def main():
    n = int(input())
    l = input()
    r = input()
    pairs = get_max_compatible_pairs(l, r)
    print(len(pairs))
    for pair in pairs:
        print(pair[0], pair[1])

if __name__ == "__main__":
    main()

