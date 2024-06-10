
def get_tree_nodes(n):
    nodes = []
    for i in range(1, n+1):
        nodes.append(i)
    return nodes

def get_tree_edges(n, parent):
    edges = []
    for i in range(1, n+1):
        edges.append(parent[i])
    return edges

def get_tree_apples(n, apples):
    nodes = get_tree_nodes(n)
    edges = get_tree_edges(n, parent)
    tree = {}
    for i in range(1, n+1):
        tree[i] = {}
        tree[i]['apples'] = apples[i-1]
        tree[i]['children'] = []
    for i in range(1, n+1):
        if edges[i-1] != 0:
            tree[edges[i-1]]['children'].append(i)
    return tree

def get_leaf_nodes(tree):
    leaf_nodes = []
    for node in tree:
        if len(tree[node]['children']) == 0:
            leaf_nodes.append(node)
    return leaf_nodes

def get_moves(tree, current_node, moves):
    if current_node in moves:
        return moves
    moves.append(current_node)
    if len(tree[current_node]['children']) == 0:
        return moves
    for child in tree[current_node]['children']:
        moves = get_moves(tree, child, moves)
    return moves

def get_swap_moves(tree, leaf_nodes, moves, swap_moves):
    for leaf in leaf_nodes:
        for move in moves:
            if leaf != move:
                swap_moves.append((leaf, move))
    return swap_moves

def get_swap_moves_after_swap(tree, leaf_nodes, swap_moves, moves):
    swap_moves_after_swap = []
    for swap_move in swap_moves:
        new_leaf_nodes = get_leaf_nodes(tree)
        for leaf in new_leaf_nodes:
            if leaf not in leaf_nodes:
                swap_moves_after_swap.append(swap_move)
    return swap_moves_after_swap

def get_swap_moves_after_swap_with_winner(tree, swap_moves_after_swap, moves):
    swap_moves_after_swap_with_winner = []
    for swap_move in swap_moves_after_swap:
        new_moves = get_moves(tree, swap_move[0], [])
        if len(new_moves) == 0:
            swap_moves_after_swap_with_winner.append(swap_move)
    return swap_moves_after_swap_with_winner

def count_swap_moves(n, apples, parent):
    tree = get_tree_apples(n, apples)
    leaf_nodes = get_leaf_nodes(tree)
    moves = get_moves(tree, 1, [])
    swap_moves = get_swap_moves(tree, leaf_nodes, moves, [])
    swap_moves_after_swap = get_swap_moves_after_swap(tree, leaf_nodes, swap_moves, [])
    swap_moves_after_swap_with_winner = get_swap_moves_after_swap_with_winner(tree, swap_moves_after_swap, moves)
    return len(swap_moves_after_swap_with_winner)

def main():
    n = int(input())
    apples = list(map(int, input().split()))
    parent = list(map(int, input().split()))
    print(count_swap_moves(n, apples, parent))

if __name__ == '__main__':
    main()

