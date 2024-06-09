
def f1(n):
    # Calculate the area of the polygon
    area = n * (n - 3) / 2
    
    # Initialize the minimum weight to infinity
    min_weight = float('inf')
    
    # Iterate over all possible ways to cut the polygon into triangles
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                # Calculate the weight of the current triangle
                weight = i * j * k
                
                # If the weight is less than the minimum weight, update the minimum weight
                if weight < min_weight:
                    min_weight = weight
    
    # Return the minimum weight
    return min_weight

def f2(n):
    # Calculate the area of the polygon
    area = n * (n - 3) / 2
    
    # Initialize the minimum weight to infinity
    min_weight = float('inf')
    
    # Iterate over all possible ways to cut the polygon into triangles
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                # Calculate the weight of the current triangle
                weight = i * j * k
                
                # If the weight is less than the minimum weight, update the minimum weight
                if weight < min_weight:
                    min_weight = weight
    
    # Return the minimum weight
    return min_weight

if __name__ == '__main__':
    n = int(input())
    print(f1(n))

