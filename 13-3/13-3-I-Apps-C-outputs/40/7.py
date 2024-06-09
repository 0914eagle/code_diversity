
def f1(n, distances):
    # Initialize the subsets A and B
    A = set()
    B = set()
    
    # Initialize the minimum sum of disparities
    min_sum = float('inf')
    
    # Iterate over all possible subsets of shipments
    for i in range(1 << n):
        # Convert the binary representation of i to a subset of shipments
        subset = set(j for j in range(n) if i & (1 << j))
        
        # Calculate the disparity of the subset
        disparity = calculate_disparity(subset, distances)
        
        # If the disparity is less than the minimum sum of disparities, update the minimum sum of disparities and the corresponding subsets A and B
        if disparity < min_sum:
            min_sum = disparity
            A = subset
            B = set(j for j in range(n) if j not in A)
    
    # Return the minimum sum of disparities and the corresponding subsets A and B
    return min_sum, A, B

def f2(n, distances):
    # Initialize the subsets A and B
    A = set()
    B = set()
    
    # Initialize the minimum sum of disparities
    min_sum = float('inf')
    
    # Iterate over all possible subsets of shipments
    for i in range(1 << n):
        # Convert the binary representation of i to a subset of shipments
        subset = set(j for j in range(n) if i & (1 << j))
        
        # Calculate the disparity of the subset
        disparity = calculate_disparity(subset, distances)
        
        # If the disparity is less than the minimum sum of disparities, update the minimum sum of disparities and the corresponding subsets A and B
        if disparity < min_sum:
            min_sum = disparity
            A = subset
            B = set(j for j in range(n) if j not in A)
    
    # Return the minimum sum of disparities and the corresponding subsets A and B
    return min_sum, A, B

def calculate_disparity(subset, distances):
    # Initialize the disparity
    disparity = 0
    
    # Iterate over all pairs of shipments in the subset
    for i in subset:
        for j in subset:
            # If i is not equal to j, calculate the distance between the two shipments and update the disparity
            if i != j:
                disparity = max(disparity, distances[i][j])
    
    # Return the disparity
    return disparity

if __name__ == '__main__':
    n = int(input())
    distances = []
    for i in range(n - 1):
        distances.append(list(map(int, input().split())))
    min_sum, A, B = f1(n, distances)
    print(min_sum)
    print(A)
    print(B)

