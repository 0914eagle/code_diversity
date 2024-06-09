
def f1(n, m, a, b, c, d):
    # Initialize a dictionary to store the values of the vertices
    values = {i: a[i-1] for i in range(1, n+1)}
    # Loop through each edge
    for i in range(m):
        # Get the vertices connected by the edge
        x, y = c[i]-1, d[i]-1
        # Check if the value of vertex x is less than the value of vertex y
        if values[x] < values[y]:
            # Decrease the value of vertex x by 1 and increase the value of vertex y by 1
            values[x] -= 1
            values[y] += 1
        # Check if the value of vertex x is greater than the value of vertex y
        elif values[x] > values[y]:
            # Increase the value of vertex x by 1 and decrease the value of vertex y by 1
            values[x] += 1
            values[y] -= 1
        # If the values are equal, return No
        else:
            return "No"
    # If all the values are equal to the desired values, return Yes
    if all(values[i] == b[i-1] for i in range(1, n+1)):
        return "Yes"
    # If not all the values are equal to the desired values, return No
    else:
        return "No"

def f2(n, m, a, b, c, d):
    # Initialize a dictionary to store the values of the vertices
    values = {i: a[i-1] for i in range(1, n+1)}
    # Loop through each edge
    for i in range(m):
        # Get the vertices connected by the edge
        x, y = c[i]-1, d[i]-1
        # Check if the value of vertex x is less than the value of vertex y
        if values[x] < values[y]:
            # Increase the value of vertex x by 1 and decrease the value of vertex y by 1
            values[x] += 1
            values[y] -= 1
        # Check if the value of vertex x is greater than the value of vertex y
        elif values[x] > values[y]:
            # Decrease the value of vertex x by 1 and increase the value of vertex y by 1
            values[x] -= 1
            values[y] += 1
        # If the values are equal, return No
        else:
            return "No"
    # If all the values are equal to the desired values, return Yes
    if all(values[i] == b[i-1] for i in range(1, n+1)):
        return "Yes"
    # If not all the values are equal to the desired values, return No
    else:
        return "No"

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = [0] + list(map(int, input().split()))
    d = [0] + list(map(int, input().split()))
    print(f1(n, m, a, b, c, d))
    print(f2(n, m, a, b, c, d))

