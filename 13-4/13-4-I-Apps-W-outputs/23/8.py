
def f1(N, M, a, b, c, d):
    # Initialize a dictionary to store the values of the vertices
    values = {i: a[i-1] for i in range(1, N+1)}

    # Loop through each edge
    for i in range(M):
        # Get the vertices connected by the edge
        x = c[i]
        y = d[i]

        # Check if the values of the vertices are equal
        if values[x] == values[y]:
            # If they are equal, decrease the value of one of the vertices by 1
            values[x] -= 1
        else:
            # If they are not equal, increase the value of one of the vertices by 1
            values[x] += 1

    # Check if the final values of the vertices are equal to the desired values
    return all(values[i] == b[i-1] for i in range(1, N+1))

def f2(...):
    ...

if __name__ == '__main__':
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    d = list(map(int, input().split()))
    print("Yes") if f1(N, M, a, b, c, d) else print("No")

