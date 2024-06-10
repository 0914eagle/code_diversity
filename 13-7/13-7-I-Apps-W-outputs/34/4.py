
def read_input():
    R, B = map(int, input().split())
    rebels = []
    for i in range(R):
        x, y = map(int, input().split())
        rebels.append((x, y))
    bases = []
    for i in range(B):
        x, y = map(int, input().split())
        bases.append((x, y))
    return R, B, rebels, bases

def find_matching(R, B, rebels, bases):
    # Initialize a graph with R + B nodes
    graph = [[] for _ in range(R + B)]
    
    # Add edges between rebels and bases
    for i in range(R):
        for j in range(B):
            if rebels[i] != bases[j]:
                graph[i].append(B + j)
    
    # Find a perfect matching using the Hopcroft-Karp algorithm
    matching = []
    for i in range(R):
        if not graph[i]:
            continue
        j = min(graph[i])
        matching.append((i, j))
        for k in graph[i]:
            graph[k].remove(j)
    
    # Check if the matching is perfect
    if len(matching) == R:
        return True
    else:
        return False

def main():
    R, B, rebels, bases = read_input()
    if find_matching(R, B, rebels, bases):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

