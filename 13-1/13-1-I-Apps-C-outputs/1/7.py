
def f1(n, distances):
    # Initialize the subsets A and B
    A = set()
    B = set()
    
    # Initialize the disparity of both subsets to infinity
    disparity_A = float('inf')
    disparity_B = float('inf')
    
    # Loop through each shipment
    for i in range(n):
        # Find the closest shipment in the other subset
        if i in A:
            closest_j = min(B, key=lambda x: distances[i][x])
        else:
            closest_j = min(A, key=lambda x: distances[i][x])
        
        # If the closest shipment is in subset A, move it to subset B
        if closest_j in A:
            B.add(i)
            A.remove(closest_j)
            disparity_B = max(disparity_B, distances[i][closest_j])
            disparity_A = max(disparity_A, distances[closest_j][i])
        # If the closest shipment is in subset B, move it to subset A
        else:
            A.add(i)
            B.remove(closest_j)
            disparity_A = max(disparity_A, distances[i][closest_j])
            disparity_B = max(disparity_B, distances[closest_j][i])
    
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

