
import sys

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.counter = 0

def build_tree(a, b):
    root = TreeNode(1)
    for i in range(1, len(a)):
        parent = root.find(a[i])
        child = TreeNode(b[i])
        parent.add_child(child)
    return root

def find_root(node):
    if node.parent is None:
        return node
    else:
        return find_root(node.parent)

def update_counters(root, node, increment):
    if node is None:
        return
    node.counter += increment
    update_counters(root, node.left, increment)
    update_counters(root, node.right, increment)

def run_operations(root, operations):
    for operation in operations:
        node = root.find(operation[0])
        update_counters(root, node, operation[1])

def get_counters(root):
    counters = []
    for i in range(1, root.value + 1):
        counters.append(root.find(i).counter)
    return counters

def main():
    input_lines = sys.stdin.readlines()
    n, q = map(int, input_lines[0].split())
    a = list(map(int, input_lines[1].split()))
    b = list(map(int, input_lines[2].split()))
    operations = [[int(x) for x in input_lines[i].split()] for i in range(3, 3 + q)]
    root = build_tree(a, b)
    run_operations(root, operations)
    counters = get_counters(root)
    print(' '.join(map(str, counters)))

if __name__ == '__main__':
    main()

