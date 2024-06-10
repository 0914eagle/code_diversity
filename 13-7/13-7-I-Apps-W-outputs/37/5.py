
def get_pleasantness(gift_id, tree):
    
    total_pleasantness = 0
    current_gift = tree[gift_id]
    while current_gift != 1:
        total_pleasantness += current_gift[0]
        current_gift = tree[current_gift[1]]
    return total_pleasantness

def find_max_pleasantness(tree):
    
    max_pleasantness = 0
    for i in range(1, len(tree)):
        for j in range(i + 1, len(tree)):
            if not set(tree[i][2]) & set(tree[j][2]):
                pleasantness_i = get_pleasantness(i, tree)
                pleasantness_j = get_pleasantness(j, tree)
                max_pleasantness = max(max_pleasantness, pleasantness_i + pleasantness_j)
    return max_pleasantness

def main():
    n = int(input())
    tree = [[] for _ in range(n + 1)]
    tree[1] = [0, 1, []]
    for i in range(2, n + 1):
        tree[i] = [int(x) for x in input().split()]
        tree[i].append(tree[tree[i][1]][2] + [i])
    print(find_max_pleasantness(tree))

if __name__ == '__main__':
    main()

