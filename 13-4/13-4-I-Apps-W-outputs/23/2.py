
def f1(n, m, a, b, c, d):
    # Initialize a dictionary to store the values of the vertices
    values = {i: a[i-1] for i in range(1, n+1)}

    # Loop through each edge
    for i in range(m):
        # Get the vertices connected by the edge
        x, y = c[i]-1, d[i]-1

        # Check if the values of the vertices are different
        if values[x] != values[y]:
            # If the values are different, update the values of the vertices
            if values[x] > values[y]:
                values[x] -= 1
                values[y] += 1
            else:
                values[x] += 1
                values[y] -= 1

    # Check if all the values are equal
    return all(values[i] == b[i-1] for i in range(1, n+1))

def f2(n, m, a, b, c, d):
    # Initialize a dictionary to store the values of the vertices
    values = {i: a[i-1] for i in range(1, n+1)}

    # Loop through each edge
    for i in range(m):
        # Get the vertices connected by the edge
        x, y = c[i]-1, d[i]-1

        # Check if the values of the vertices are different
        if values[x] != values[y]:
            # If the values are different, update the values of the vertices
            if values[x] < values[y]:
                values[x] += 1
                values[y] -= 1
            else:
                values[x] -= 1
                values[y] += 1

    # Check if all the values are equal
    return all(values[i] == b[i-1] for i in range(1, n+1))

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [int(x) for x in input().split()]
    d = [int(x) for x in input().split()]

    if f1(n, m, a, b, c, d):
        print("Yes")
    elif f2(n, m, a, b, c, d):
        print("Yes")
    else:
        print("No")

