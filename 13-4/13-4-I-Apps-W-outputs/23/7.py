
def f1(N, M, a, b, c, d):
    # Initialize a dictionary to store the values of the vertices
    values = {i: a[i-1] for i in range(1, N+1)}

    # Loop through each edge
    for i in range(M):
        # Get the vertices connected by the edge
        x, y = c[i]-1, d[i]-1

        # Check if the operation is possible
        if values[x] >= values[y]:
            return "No"

        # Perform the operation
        values[x] -= 1
        values[y] += 1

    # Check if the final values match the desired values
    for i in range(N):
        if values[i] != b[i]:
            return "No"

    return "Yes"

def f2(N, M, a, b, c, d):
    # Initialize a dictionary to store the values of the vertices
    values = {i: a[i-1] for i in range(1, N+1)}

    # Loop through each edge
    for i in range(M):
        # Get the vertices connected by the edge
        x, y = c[i]-1, d[i]-1

        # Check if the operation is possible
        if values[x] <= values[y]:
            return "No"

        # Perform the operation
        values[x] += 1
        values[y] -= 1

    # Check if the final values match the desired values
    for i in range(N):
        if values[i] != b[i]:
            return "No"

    return "Yes"

if __name__ == '__main__':
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [0] + list(map(int, input().split()))
    d = [0] + list(map(int, input().split()))
    print(f1(N, M, a, b, c, d))
    print(f2(N, M, a, b, c, d))

