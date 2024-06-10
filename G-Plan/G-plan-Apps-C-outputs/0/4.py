
import itertools

def calculate_distance(port_distances, path):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += port_distances[path[i]][path[i + 1]]
    return total_distance

def calculate_average_distance(n, port_distances):
    total_pairs = 0
    total_distance = 0
    for path in itertools.permutations(range(n)):
        if path[0] != 0:
            continue
        total_pairs += 1
        total_distance += calculate_distance(port_distances, path)
    if total_pairs == 0:
        return "impossible"
    return total_distance / total_pairs

if __name__ == "__main__":
    n = int(input())
    port_distances = []
    for i in range(n - 1):
        port_distances.append(list(map(int, input().split())))
    
    result = calculate_average_distance(n, port_distances)
    print(result)
