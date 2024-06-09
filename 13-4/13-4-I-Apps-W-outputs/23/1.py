
def read_input():
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    edges = []
    for _ in range(M):
        c, d = map(int, input().split())
        edges.append((c, d))
    return N, M, a, b, edges

def is_possible(N, M, a, b, edges):
    # Initialize the values of a and b
    a = a.copy()
    b = b.copy()
    
    # Loop through the edges and perform the operations
    for i in range(M):
        c, d = edges[i]
        if a[c-1] > a[d-1]:
            a[c-1] -= 1
            a[d-1] += 1
        elif a[c-1] < a[d-1]:
            a[c-1] += 1
            a[d-1] -= 1
        else:
            return False
    
    # Check if the final values of a and b are the same
    for i in range(N):
        if a[i] != b[i]:
            return False
    return True

def main():
    N, M, a, b, edges = read_input()
    if is_possible(N, M, a, b, edges):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

