
def calculate_average_distance(n, distances):
    total_distance = 0
    total_pairs = 0
    
    for i in range(n):
        for j in range(i+1, n):
            total_distance += distances[i][j-i-1]
            total_pairs += 1
    
    if total_pairs == 0:
        return "impossible"
    
    return total_distance / total_pairs

if __name__ == "__main__":
    n = int(input())
    distances = []
    for i in range(n-1):
        distances.append(list(map(int, input().split())))
    
    result = calculate_average_distance(n, distances)
    print(result)
