
def f1(n, distances):
    # Initialize the subsets A and B
    A = set()
    B = set()
    
    # Initialize the disparity of both subsets to infinity
    disparity_A = float('inf')
    disparity_B = float('inf')
    
    # Iterate through each shipment
    for i in range(n):
        # Find the closest shipment in the other subset
        if i in A:
            closest_j = min(B, key=lambda x: distances[i][x])
        else:
            closest_j = min(A, key=lambda x: distances[i][x])
        
        # If the closest shipment is in subset A, move it to subset B
        if closest_j in A:
            A.remove(closest_j)
            B.add(closest_j)
        # If the closest shipment is in subset B, move it to subset A
        else:
            B.remove(closest_j)
            A.add(closest_j)
        
        # Update the disparity of both subsets
        disparity_A = min(disparity_A, max(distances[i][j] for j in A))
        disparity_B = min(disparity_B, max(distances[i][j] for j in B))
    
    # Return the minimum possible sum of disparities
    return disparity_A + disparity_B

def f2(...):
    # Implement f2 here
    pass

if __name__ == '__main__':
    n = int(input())
    distances = []
    for i in range(n - 1):
        distances.append(list(map(int, input().split())))
    print(f1(n, distances))

