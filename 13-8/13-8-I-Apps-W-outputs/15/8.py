
def is_relatively_prime(n, m):
    return all(gcd(n, m) == 1)

def find_relatively_prime_graph(n, m):
    if n < 1 or m < 1 or n > 10000 or m > 10000:
        return "Impossible"

    adjacency_matrix = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if is_relatively_prime(i, j):
                adjacency_matrix[i][j] = 1
                adjacency_matrix[j][i] = 1

    visited = [False] * (n + 1)
    stack = []
    stack.append(1)
    while stack:
        vertex = stack.pop()
        if not visited[vertex]:
            visited[vertex] = True
            for neighbor in range(1, n + 1):
                if adjacency_matrix[vertex][neighbor] == 1 and not visited[neighbor]:
                    stack.append(neighbor)

    if visited.count(True) == n:
        return "Possible"
    else:
        return "Impossible"

def main():
    n, m = map(int, input().split())
    print(find_relatively_prime_graph(n, m))

if __name__ == '__main__':
    main()

