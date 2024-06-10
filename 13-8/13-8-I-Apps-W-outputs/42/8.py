
def get_tree_height(n, parent):
    height = 0
    while n != 1:
        n = parent[n]
        height += 1
    return height

def get_swap_pairs(n, a, parent):
    height = get_tree_height(n, parent)
    pairs = set()
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if parent[i] != parent[j] and a[i] != 0 and a[j] != 0 and abs(height[i] - height[j]) % 2 == 1:
                pairs.add((i, j))
    return pairs

def main():
    n = int(input())
    a = list(map(int, input().split()))
    parent = list(map(int, input().split()))
    pairs = get_swap_pairs(n, a, parent)
    print(len(pairs))

if __name__ == '__main__':
    main()

