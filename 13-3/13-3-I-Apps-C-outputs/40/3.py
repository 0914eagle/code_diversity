
def f1(n, distances):
    # Initialize the subsets A and B
    A = set()
    B = set()
    
    # Initialize the disparities of A and B
    disparity_A = 0
    disparity_B = 0
    
    # Iterate through each shipment
    for i in range(n):
        # Find the closest shipment in the other subset
        closest_shipment = find_closest_shipment(i, A if i in B else B, distances)
        
        # Add the current shipment to the subset with the closest shipment
        if i in A:
            B.add(i)
            disparity_B += distances[i][closest_shipment]
        else:
            A.add(i)
            disparity_A += distances[i][closest_shipment]
    
    # Return the minimum possible sum of disparities
    return disparity_A + disparity_B

def find_closest_shipment(shipment, subset, distances):
    # Initialize the closest shipment and its distance
    closest_shipment = -1
    closest_distance = float('inf')
    
    # Iterate through each shipment in the subset
    for other_shipment in subset:
        # Find the distance between the current shipment and the other shipment
        distance = distances[shipment][other_shipment]
        
        # If the distance is less than the current closest distance, update the closest distance and shipment
        if distance < closest_distance:
            closest_distance = distance
            closest_shipment = other_shipment
    
    # Return the closest shipment
    return closest_shipment

def f2(...):
    # Implement function f2 here
    pass

if __name__ == '__main__':
    n = int(input())
    distances = []
    for i in range(n - 1):
        distances.append(list(map(int, input().split())))
    print(f1(n, distances))

