
def read_input():
    n = int(input())
    c = list(map(int, input().split()))
    return n, c

def build_tree(c):
    # Base case: if there are no nodes, return an empty tree
    if not c:
        return []

    # Find the largest value in the list
    largest = max(c)

    # Find the index of the largest value
    largest_index = c.index(largest)

    # Create a new tree with the largest value as the root
    tree = [largest]

    # Remove the largest value from the list
    c.pop(largest_index)

    # Recursively build the left and right subtrees
    tree.append(build_tree(c[:largest_index]))
    tree.append(build_tree(c[largest_index:]))

    return tree

def is_valid_tree(tree):
    # Base case: if the tree is empty, return True
    if not tree:
        return True

    # If the tree has only one node, return False
    if len(tree) == 1:
        return False

    # If the tree has at least two nodes, return True
    return True

def main():
    n, c = read_input()
    tree = build_tree(c)
    if is_valid_tree(tree):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()

