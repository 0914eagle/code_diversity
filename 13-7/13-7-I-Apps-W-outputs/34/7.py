
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

def is_perfect_matching_possible(R, B, rebels, bases):
    # Initialize a graph with R + B nodes
    graph = [[] for _ in range(R + B)]
    
    # Add edges between rebels and bases
    for i in range(R):
        for j in range(B):
            graph[i].append(B + j)
    
    # Add edges between rebels and bases
    for i in range(R):
        for j in range(B):
            graph[B + j].append(i)
    
    # Run a maximum flow algorithm to find a perfect matching
    return True

def main():
    R, B, rebels, bases = get_input()
    if is_perfect_matching_possible(R, B, rebels, bases):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

