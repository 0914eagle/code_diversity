
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

def get_min_weight_triangulation(n):
    # Initialize the minimum weight to a large value
    min_weight = float('inf')
    # Iterate over all possible triangulations
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if i < j < k:
                    weight = i * j * k
                elif j < i < k:
                    weight = j * i * k
                elif k < i < j:
                    weight = k * i * j
                # Check if the current triangulation has a smaller weight than the minimum weight so far
                if weight < min_weight:
                    min_weight = weight
    return min_weight

if __name__ == '__main__':
    n = int(input())
    print(get_min_weight_triangulation(n))

