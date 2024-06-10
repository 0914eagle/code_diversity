
def get_intersection(A, B, n):
    # Function to find the intersection where Alice and Bob are different
    for i in range(n):
        if A == i:
            return B
        elif B == i:
            return A
    return -1

def get_path(A, B, n, edges):
    # Function to find the path from one intersection to the other
    path = []
    current = A
    while current != B:
        for i in range(n):
            if edges[current][i] == 1:
                path.append(i)
                current = i
                break
    return path

def get_turns(path, edges):
    # Function to find the number of turns in the path
    turns = 0
    for i in range(len(path) - 1):
        if edges[path[i]][path[i+1]] == 0:
            turns += 1
    return turns

def main():
    n, A, B = map(int, input().split())
    edges = [[0] * n for _ in range(n)]
    for i in range(n):
        l, r, t = map(int, input().split())
        edges[i][l] = 1
        edges[i][r] = 1
    intersection = get_intersection(A, B, n)
    if intersection == -1:
        print("indistinguishable")
    else:
        path = get_path(A, intersection, n, edges)
        turns = get_turns(path, edges)
        print(turns)

if __name__ == '__main__':
    main()

