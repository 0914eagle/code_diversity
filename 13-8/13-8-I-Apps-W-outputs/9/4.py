
def get_correct_bracket_sequences(n):
    def helper(n, s):
        if n == 0:
            return [""]
        sequences = []
        for seq in helper(n-1, s):
            sequences.append("(" + seq + ")")
            sequences.append(seq + ")")
        return sequences
    return helper(n, "")

def get_maximum_matching(n):
    sequences = get_correct_bracket_sequences(n)
    graph = {}
    for seq in sequences:
        for i in range(len(seq)):
            if seq[i] == "(":
                if i+1 < len(seq) and seq[i+1] == ")":
                    if i not in graph:
                        graph[i] = []
                    graph[i].append(i+1)
    matching = []
    visited = set()
    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor)
        matching.append(node)
    for node in graph:
        dfs(node)
    return len(matching) % (10**9 + 7)

if __name__ == '__main__':
    n = int(input())
    print(get_maximum_matching(n))

