
def get_compatible_pairs(n, l, r):
    compatible_pairs = []
    for i in range(n):
        for j in range(i+1, n):
            if is_compatible(l[i], r[j]) and is_compatible(r[j], l[i]):
                compatible_pairs.append((i, j))
    return compatible_pairs

def is_compatible(c1, c2):
    if c1 == c2:
        return True
    if c1 == "?" or c2 == "?":
        return True
    return False

def main():
    n = int(input())
    l = input()
    r = input()
    compatible_pairs = get_compatible_pairs(n, l, r)
    print(len(compatible_pairs))
    for pair in compatible_pairs:
        print(pair[0], pair[1])

if __name__ == "__main__":
    main()

