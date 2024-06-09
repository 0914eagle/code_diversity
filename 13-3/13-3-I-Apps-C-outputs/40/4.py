
def f1(n, distances):
    # Initialize the subsets A and B
    A = set()
    B = set()
    
    # Initialize the disparities of A and B
    disparity_A = 0
    disparity_B = 0
    
    # Loop through each shipment
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
            disparity_A += closest_distance
        else:
            B.add(i)
            disparity_B += closest_distance
    
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

