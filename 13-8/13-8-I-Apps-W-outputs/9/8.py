
def get_correct_bracket_sequences(n):
    sequences = []
    for i in range(n):
        sequences.append('()')
    for i in range(n):
        for j in range(n):
            sequences.append('(' + sequences[i] + sequences[j] + ')')
    return sequences

def get_maximum_matching(sequences):
    graph = {}
    for sequence in sequences:
        for i in range(len(sequence)):
            if sequence[i] == '(':
                graph[i] = []
            elif sequence[i] == ')':
                graph[i] = []
                for j in range(i):
                    if sequence[j] == '(':
                        graph[i].append(j)
    matching = []
    for i in range(len(graph)):
        if i not in matching and graph[i]:
            matching.append(i)
            for j in graph[i]:
                if j not in matching:
                    matching.append(j)
    return len(matching)

def main():
    n = int(input())
    sequences = get_correct_bracket_sequences(n)
    print(get_maximum_matching(sequences) % (10**9 + 7))

if __name__ == '__main__':
    main()

