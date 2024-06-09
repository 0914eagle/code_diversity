
def get_max_triangles(n, arr):
    # Sort the array in descending order
    arr.sort(reverse=True)
    
    # Initialize variables to keep track of triangles made
    triangles_made = 0
    
    # Loop through the array and check if a triangle can be made with the current stick and the next two sticks
    for i in range(len(arr)-2):
        if arr[i] > arr[i+1] + arr[i+2]:
            triangles_made += 1
    
    return triangles_made

