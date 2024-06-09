
def get_min_weight(n):
    # Calculate the total area of the polygon
    total_area = n * (n - 3) / 2
    
    # Initialize the minimum weight to infinity
    min_weight = float('inf')
    
    # Iterate over all possible ways to cut the polygon into triangles
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                # Calculate the area of the current triangle
                area = get_triangle_area(i, j, k, n)
                
                # If the current triangle has non-zero area, calculate its weight and compare it to the minimum weight
                if area > 0:
                    weight = get_triangle_weight(i, j, k, n)
                    if weight < min_weight:
                        min_weight = weight
    
    # Return the minimum weight
    return min_weight

def get_triangle_area(i, j, k, n):
    # Calculate the area of the current triangle
    area = (n - 2) * (get_triangle_perimeter(i, j, k, n) / 2)
    
    # Return the area
    return area

def get_triangle_perimeter(i, j, k, n):
    # Calculate the perimeter of the current triangle
    perimeter = get_distance(i, j, n) + get_distance(j, k, n) + get_distance(k, i, n)
    
    # Return the perimeter
    return perimeter

def get_distance(i, j, n):
    # Calculate the distance between two vertices
    distance = abs(i - j)
    
    # If the distance is greater than the half of the number of vertices, return the distance modulo the number of vertices
    if distance > n / 2:
        distance = distance % n
    
    # Return the distance
    return distance

def get_triangle_weight(i, j, k, n):
    # Calculate the weight of the current triangle
    weight = i * j * k
    
    # Return the weight
    return weight

if __name__ == '__main__':
    n = int(input())
    print(get_min_weight(n))

