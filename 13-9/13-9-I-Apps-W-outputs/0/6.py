
def get_grade(tree, k):
    # Initialize the minimum grade found so far
    min_grade = float('inf')
    # Initialize the maximum grade found so far
    max_grade = 0
    # Iterate over all possible root nodes
    for root in range(len(tree)):
        # Get the preorder traversal of the tree starting from the current root
        preorder = get_preorder(tree, root)
        # Get the minimum grade in the first k nodes of the preorder traversal
        min_grade_k = min(preorder[:k])
        # Update the minimum grade found so far
        min_grade = min(min_grade, min_grade_k)
        # Update the maximum grade found so far
        max_grade = max(max_grade, min_grade_k)
    # Return the maximum grade
    return max_grade

def get_preorder(tree, root):
    # Initialize the preorder traversal
    preorder = []
    # Recursively visit all nodes in the tree starting from the current root
    visit_node(tree, root, preorder)
    # Return the preorder traversal
    return preorder

def visit_node(tree, node, preorder):
    # Add the current node to the preorder traversal
    preorder.append(node)
    # Iterate over all neighbors of the current node
    for neighbor in tree[node]:
        # Recursively visit the neighbor if it has not been visited yet
        if neighbor not in preorder:
            visit_node(tree, neighbor, preorder)

def main():
    # Read the input data
    n, k = map(int, input().split())
    tree = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)
    # Get the maximum grade
    grade = get_grade(tree, k)
    # Print the maximum grade
    print(grade)

if __name__ == '__main__':
    main()

