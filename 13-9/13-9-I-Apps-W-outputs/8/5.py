
import sys

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(a, b):
    root = Node(1)
    for i in range(1, len(a)):
        parent = root
        current = root
        while current:
            if current.val == a[i]:
                parent = current
                current = current.left
            elif current.val == b[i]:
                parent = current
                current = current.right
            else:
                break
        if parent.val == a[i]:
            parent.left = Node(b[i])
        else:
            parent.right = Node(b[i])
    return root

def find_subtree_vertices(root, p):
    vertices = []
    queue = [root]
    while queue:
        current = queue.pop(0)
        if current.val == p:
            vertices.append(current.val)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return vertices

def increment_counters(root, p, x):
    vertices = find_subtree_vertices(root, p)
    for vertex in vertices:
        root.val += x
    return root

def get_counters(root):
    queue = [root]
    counters = []
    while queue:
        current = queue.pop(0)
        counters.append(current.val)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return counters

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    p = list(map(int, input().split()))
    x = list(map(int, input().split()))
    root = build_tree(a, b)
    for i in range(q):
        root = increment_counters(root, p[i], x[i])
    counters = get_counters(root)
    print(*counters)

if __name__ == '__main__':
    main()

