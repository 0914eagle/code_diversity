
def get_tree_height(n, p):
    height = 0
    parent = 1
    while parent != n:
        height += 1
        parent = p[parent]
    return height

def get_leaf_nodes(n, p):
    leaf_nodes = []
    for i in range(1, n+1):
        if p[i] == 0:
            leaf_nodes.append(i)
    return leaf_nodes

def get_move_count(n, a, p):
    height = get_tree_height(n, p)
    leaf_nodes = get_leaf_nodes(n, p)
    move_count = 0
    for i in leaf_nodes:
        move_count += a[i]
    return move_count

def get_swap_count(n, a, p):
    height = get_tree_height(n, p)
    leaf_nodes = get_leaf_nodes(n, p)
    swap_count = 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if i != j and a[i] != a[j]:
                swap_count += 1
    return swap_count

def get_winning_swap_count(n, a, p):
    move_count = get_move_count(n, a, p)
    swap_count = get_swap_count(n, a, p)
    winning_swap_count = 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if i != j and a[i] != a[j]:
                temp_a = a.copy()
                temp_a[i], temp_a[j] = temp_a[j], temp_a[i]
                temp_move_count = get_move_count(n, temp_a, p)
                if temp_move_count < move_count:
                    winning_swap_count += 1
    return winning_swap_count

def main():
    n = int(input())
    a = list(map(int, input().split()))
    p = list(map(int, input().split()))
    print(get_winning_swap_count(n, a, p))

if __name__ == '__main__':
    main()

