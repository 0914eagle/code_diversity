
def get_triangle_weight(triangle):
    return triangle[0] * triangle[1] * triangle[2]

def get_min_weight_triangulation(polygon):
    n = len(polygon)
    if n == 3:
        return get_triangle_weight(polygon)
    
    min_weight = float('inf')
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if i != j and j != k and k != i:
                    triangle = [polygon[i], polygon[j], polygon[k]]
                    weight = get_triangle_weight(triangle)
                    if weight < min_weight:
                        min_weight = weight
    
    return min_weight

def main():
    n = int(input())
    polygon = list(range(1, n+1))
    print(get_min_weight_triangulation(polygon))

if __name__ == '__main__':
    main()

