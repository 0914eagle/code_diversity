
def f1(n, m, edges, q, queries):
    # Initialize a dictionary to store the colors and their frequencies
    colors = {}
    for edge in edges:
        color = edge[2]
        if color not in colors:
            colors[color] = 1
        else:
            colors[color] += 1

    # Initialize a dictionary to store the direct connections between vertices
    direct_connections = {}
    for edge in edges:
        u = edge[0]
        v = edge[1]
        if u not in direct_connections:
            direct_connections[u] = [v]
        else:
            direct_connections[u].append(v)
        if v not in direct_connections:
            direct_connections[v] = [u]
        else:
            direct_connections[v].append(u)

    # Initialize a dictionary to store the indirect connections between vertices
    indirect_connections = {}
    for u in direct_connections:
        for v in direct_connections[u]:
            if v not in indirect_connections:
                indirect_connections[v] = [u]
            else:
                indirect_connections[v].append(u)

    # Process the queries
    answers = []
    for query in queries:
        u = query[0]
        v = query[1]
        answer = 0
        if u in direct_connections and v in direct_connections:
            answer += 1
        if u in indirect_connections and v in indirect_connections:
            answer += 1
        answers.append(answer)

    return answers

def f2(...):
    ...

if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = []
    for i in range(m):
        a, b, c = map(int, input().split())
        edges.append((a, b, c))
    q = int(input())
    queries = []
    for i in range(q):
        u, v = map(int, input().split())
        queries.append((u, v))
    answers = f1(n, m, edges, q, queries)
    for answer in answers:
        print(answer)

