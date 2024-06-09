
def f1(n, distances):
    # Initialize the subsets A and B
    A = set()
    B = set()
    
    # Initialize the disparity of subsets A and B
    disparity_A = 0
    disparity_B = 0
    
    # Loop through each shipment
    for i in range(n):
        # Find the closest shipment in the other subset
        closest_subset = None
        closest_distance = float('inf')
        for subset in [A, B]:
            for shipment in subset:
                distance = distances[i][shipment]
                if distance < closest_distance:
                    closest_distance = distance
                    closest_subset = subset
        
        # Add the current shipment to the closest subset
        closest_subset.add(i)
        
        # Update the disparity of the closest subset
        if closest_subset == A:
            disparity_A += closest_distance
        else:
            disparity_B += closest_distance
    
    # Return the minimum possible sum of disparities
    return min(disparity_A, disparity_B)

def f2(...):
    # Implement f2 here
    pass

if __name__ == '__main__':
    n = int(input())
    distances = []
    for i in range(n - 1):
        distances.append(list(map(int, input().split())))
    print(f1(n, distances))

