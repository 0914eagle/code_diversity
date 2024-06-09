
def get_triangulation_weight(n):
    # Calculate the weight of the triangulation
    weight = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if i < j < k:
                    weight += i * j * k
                elif j < i < k:
                    weight += j * i * k
                elif k < i < j:
                    weight += k * i * j
    return weight

def get_minimum_weight_triangulation(n):
    # Calculate the minimum weight among all triangulations of the polygon
    minimum_weight = float('inf')
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if i < j < k:
                    weight = i * j * k
                elif j < i < k:
                    weight = j * i * k
                elif k < i < j:
                    weight = k * i * j
                if weight < minimum_weight:
                    minimum_weight = weight
    return minimum_weight

if __name__ == '__main__':
    n = int(input())
    print(get_minimum_weight_triangulation(n))

