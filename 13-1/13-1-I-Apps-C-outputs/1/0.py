
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
        closest_shipment = find_closest_shipment(i, A if i in B else B, distances)
        
        # Add the current shipment to the subset with the closest shipment
        if closest_shipment in A:
            B.add(i)
            disparity_B += distances[i][closest_shipment]
        else:
            A.add(i)
            disparity_A += distances[i][closest_shipment]
    
    # Return the minimum possible sum of disparities
    return disparity_A + disparity_B

def find_closest_shipment(shipment, subset, distances):
    # Find the closest shipment in the subset
    closest_shipment = None
    min_distance = float('inf')
    for other_shipment in subset:
        distance = distances[shipment][other_shipment]
        if distance < min_distance:
            min_distance = distance
            closest_shipment = other_shipment
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

