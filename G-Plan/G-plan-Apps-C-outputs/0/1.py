
def calculate_distance(port_distances, i, j):
    distance = 0
    for k in range(i, j):
        distance += port_distances[k]
    return distance

def calculate_average_distance(n, port_distances):
    total_distance = 0
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            distance = calculate_distance(port_distances[i], i, j)
            total_distance += distance
            count += 1
    if count == 0:
        return "impossible"
    return total_distance / count

if __name__ == "__main__":
    n = int(input())
    port_distances = []
    for i in range(n-1):
        port_distances.append(list(map(int, input().split())))
    
    result = calculate_average_distance(n, port_distances)
    print(result)
