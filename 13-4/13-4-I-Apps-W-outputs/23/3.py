
def f1(N, M, a, b, c, d):
    # Initialize a dictionary to store the values of the vertices
    values = {i: a[i-1] for i in range(1, N+1)}

    # Iterate through the edges
    for i in range(M):
        # Get the vertices connected by the edge
        x, y = c[i]-1, d[i]-1

        # Check if the value of vertex x is less than the value of vertex y
        if values[x] < values[y]:
            # Increase the value of vertex x by 1 and decrease the value of vertex y by 1
            values[x] += 1
            values[y] -= 1
        else:
            # Decrease the value of vertex x by 1 and increase the value of vertex y by 1
            values[x] -= 1
            values[y] += 1

    # Check if the values of all vertices are equal to the desired values
    return all(values[i] == b[i-1] for i in range(1, N+1))

def f2(...):
    ...

if __name__ == '__main__':
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [list(map(int, input().split())) for _ in range(M)]
    d = [list(map(int, input().split())) for _ in range(M)]
    print("Yes") if f1(N, M, a, b, c, d) else print("No")

