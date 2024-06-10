
def get_bracket_sequences(n):
    sequences = []
    for i in range(1, n+1):
        sequences.extend(get_bracket_sequences_helper(i, n))
    return sequences

def get_bracket_sequences_helper(i, n):
    if i == 0:
        return [""]
    sequences = []
    for j in range(1, n+1):
        for seq in get_bracket_sequences_helper(i-1, n):
            sequences.append("(" + seq + ")")
            sequences.append(")" + seq + "(")
    return sequences

def get_maximum_matching(n):
    sequences = get_bracket_sequences(n)
    graph = {}
    for seq in sequences:
        for i in range(len(seq)):
            if seq[i] == "(":
                graph[i] = []
            else:
                graph[i] = [i-1]
    matching = []
    for i in range(len(graph)):
        if i not in matching:
            dfs(graph, i, matching)
    return len(matching)

def dfs(graph, i, matching):
    if i in matching:
        return
    matching.append(i)
    for j in graph[i]:
        dfs(graph, j, matching)

if __name__ == '__main__':
    n = int(input())
    print(get_maximum_matching(n) % 1000000007)

