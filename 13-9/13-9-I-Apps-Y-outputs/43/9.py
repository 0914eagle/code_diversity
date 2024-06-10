
def solve_test_case(n, gangs):
    # Initialize a graph with n nodes and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges between nodes belonging to different gangs
    for i in range(n):
        for j in range(i+1, n):
            if gangs[i] != gangs[j]:
                graph[i].append(j)
                graph[j].append(i)

    # BFS to find a Hamiltonian cycle
    queue = [0]
    visited = [False] * n
    visited[0] = True
    while queue:
        node = queue.pop(0)
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                if neighbor == 0:
                    break
    else:
        return "NO"

    # Return the Hamiltonian cycle as a list of edges
    cycle = []
    node = 0
    while node != 0:
        cycle.append(node)
        node = graph[node][0]
    return "YES\n" + "\n".join(f"{node+1} {cycle[i]+1}" for i in range(1, len(cycle)))

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        gangs = list(map(int, input().split()))
        print(solve_test_case(n, gangs))

if __name__ == '__main__':
    main()

