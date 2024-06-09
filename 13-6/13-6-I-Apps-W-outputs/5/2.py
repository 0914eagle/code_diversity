
def get_triangulation_weight(n):
    # Calculate the weight of the triangulation
    weight = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if i < j < k:
                    weight += i * j * k
                elif i < k < j:
                    weight += i * j * k
                elif j < i < k:
                    weight += i * j * k
                elif j < k < i:
                    weight += i * j * k
                elif k < i < j:
                    weight += i * j * k
                elif k < j < i:
                    weight += i * j * k
    return weight

def get_minimum_weight_triangulation(n):
    # Initialize the minimum weight to a large value
    minimum_weight = float('inf')
    # Iterate over all possible triangulations
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if i < j < k:
                    weight = i * j * k
                elif i < k < j:
                    weight = i * j * k
                elif j < i < k:
                    weight = i * j * k
                elif j < k < i:
                    weight = i * j * k
                elif k < i < j:
                    weight = i * j * k
                elif k < j < i:
                    weight = i * j * k
                # Check if the current weight is less than the minimum weight
                if weight < minimum_weight:
                    minimum_weight = weight
    return minimum_weight

if __name__ == '__main__':
    n = int(input())
    print(get_minimum_weight_triangulation(n))

