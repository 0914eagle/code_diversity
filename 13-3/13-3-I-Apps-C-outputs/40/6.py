
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
        closest_subset = A if i in B else B
        closest_distance = float('inf')
        for j in closest_subset:
            distance = distances[i][j]
            if distance < closest_distance:
                closest_distance = distance
        
        # Add the shipment to the subset with the closest distance
        if closest_distance == disparity_A:
            A.add(i)
        else:
            B.add(i)
        
        # Update the disparity of both subsets
        disparity_A = min(disparity_A, closest_distance)
        disparity_B = min(disparity_B, closest_distance)
    
    # Return the minimum possible sum of disparities
    return disparity_A + disparity_B

def f2(...):
    # Implement f2 here
    pass

if __name__ == '__main__':
    n = int(input())
    distances = []
    for i in range(n):
        distances.append([int(x) for x in input().split()])
    print(f1(n, distances))

