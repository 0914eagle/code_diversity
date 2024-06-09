
def f1(n):
    # Calculate the number of independent sets in the graph
    num_independent_sets = (1 << n) - 1
    return num_independent_sets

def f2(n, edges):
    # Initialize the answer and the number of independent sets
    answer = 0
    num_independent_sets = (1 << n) - 1

    # Iterate over all edges and calculate the number of independent sets in the subgraph
    for edge in edges:
        u, v = edge
        answer += num_independent_sets - (num_independent_sets >> (u - 1) & 1) - (num_independent_sets >> (v - 1) & 1) + (num_independent_sets >> (u - 1) & 1) * (num_independent_sets >> (v - 1) & 1)

    # Return the answer modulo 998244353
    return answer % 998244353

if __name__ == '__main__':
    n = int(input())
    edges = []
    for i in range(n - 1):
        u, v = map(int, input().split())
        edges.append((u, v))
    print(f2(n, edges))

