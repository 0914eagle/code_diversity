
def calculate_distance(town1, town2, roads):
    # Calculate the distance between two towns using roads
    # Assume all roads have the same length (1)
    return roads[(town1, town2)]

def max_sum_distances(n, k, universities, roads):
    universities.sort()
    distances = []
    for i in range(0, len(universities), 2):
        distances.append(calculate_distance(universities[i], universities[i+1], roads))
    distances.sort(reverse=True)
    return sum(distances[:k])

if __name__ == "__main__":
    n, k = map(int, input().split())
    universities = list(map(int, input().split()))
    roads = {}
    for _ in range(n-1):
        x, y = map(int, input().split())
        roads[(x, y)] = 1  # Assume all roads have the same length (1)

    result = max_sum_distances(n, k, universities, roads)
    print(result)
