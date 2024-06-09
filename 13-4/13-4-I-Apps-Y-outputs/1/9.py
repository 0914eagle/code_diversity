
def get_compatible_pairs(n, l, r):
    pairs = []
    for i in range(n):
        for j in range(i+1, n):
            if is_compatible(l[i], r[j]) and not (i in [a for a, b in pairs] and j in [b for a, b in pairs]):
                pairs.append((i, j))
    return pairs

def is_compatible(c1, c2):
    if c1 == c2:
        return True
    elif c1 == "?" or c2 == "?":
        return True
    else:
        return False

def main():
    n = int(input())
    l = input()
    r = input()
    pairs = get_compatible_pairs(n, l, r)
    print(len(pairs))
    for pair in pairs:
        print(pair[0], pair[1])

if __name__ == "__main__":
    main()

