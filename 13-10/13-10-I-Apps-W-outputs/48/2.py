
def get_order(n):
    order = []
    visited = [False] * n
    def dfs(node):
        if visited[node]:
            return False
        visited[node] = True
        if node == 0:
            order.append(node)
            return True
        if dfs((2 * node) % n) or dfs((2 * node + 1) % n):
            order.append(node)
            return True
        return False
    if dfs(0):
        return order
    return -1

def main():
    n = int(input())
    print(get_order(n))

if __name__ == '__main__':
    main()

