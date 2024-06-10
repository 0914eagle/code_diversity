
import sys

def get_input():
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

def solve(R, B, rebels, bases):
    # create a graph with R rebels and B bases
    graph = {}
    for i in range(R):
        graph[i] = set()
    for i in range(B):
        graph[i + R] = set()
    
    # add edges between rebels and bases
    for i in range(R):
        for j in range(B):
            if (rebels[i][0] - bases[j][0]) * (rebels[i][1] - bases[j][1]) == 0:
                graph[i].add(j + R)
                graph[j + R].add(i)
    
    # find a perfect matching in the graph
    matching = []
    visited = set()
    while len(matching) < R:
        for i in range(R):
            if i not in visited and len(graph[i]) > 0:
                j = graph[i].pop()
                matching.append((i, j))
                visited.add(i)
                visited.add(j)
                break
    
    # check if the matching is perfect
    if len(matching) == R:
        return "Yes"
    else:
        return "No"

def main():
    R, B, rebels, bases = get_input()
    print(solve(R, B, rebels, bases))

if __name__ == '__main__':
    main()

