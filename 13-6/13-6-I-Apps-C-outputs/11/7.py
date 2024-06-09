
def get_input():
    return int(input())

def get_preorder_traversal(root, traversal):
    if root == -1:
        return
    traversal.append(root)
    get_preorder_traversal(root*2, traversal)
    get_preorder_traversal(root*2+1, traversal)
    return traversal

def solve(n):
    traversal = []
    get_preorder_traversal(1, traversal)
    return ' '.join(str(x) for x in traversal)

if __name__ == '__main__':
    n = get_input()
    print(solve(n))

