
def get_frequencies(n, edges):
    frequencies = [0] * (2 * n)
    for i in range(n):
        frequencies[i * 2] = i + 1
        frequencies[i * 2 + 1] = i + 1
    
    for edge in edges:
        i, j = edge
        if frequencies[i * 2] == frequencies[j * 2]:
            frequencies[j * 2 + 1] = frequencies[i * 2]
        elif frequencies[i * 2 + 1] == frequencies[j * 2]:
            frequencies[i * 2] = frequencies[j * 2 + 1]
        elif frequencies[i * 2] == frequencies[j * 2 + 1]:
            frequencies[j * 2] = frequencies[i * 2 + 1]
        elif frequencies[i * 2 + 1] == frequencies[j * 2 + 1]:
            frequencies[i * 2] = frequencies[j * 2]
    
    return frequencies

def main():
    n = int(input())
    edges = []
    for _ in range(n - 1):
        edges.append(list(map(int, input().split())))
    
    frequencies = get_frequencies(n, edges)
    for i in range(n):
        print(frequencies[i * 2], frequencies[i * 2 + 1])

if __name__ == '__main__':
    main()

