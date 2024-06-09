
def get_max_triangles(n, a):
    # Sort the array in descending order
    a.sort(reverse=True)
    
    # Initialize the number of triangles to 0
    triangles = 0
    
    # Loop through the array and count the number of triangles that can be formed
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if a[i] + a[j] > a[k]:
                    triangles += 1
    
    return triangles

