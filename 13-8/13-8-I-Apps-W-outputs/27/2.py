
def get_min_animal_count(p, q, areas):
    # Find the shortest path between p and q
    visited = set()
    queue = [(p, 0)]
    while queue:
        current, count = queue.pop(0)
        if current == q:
            return count
        visited.add(current)
        for i in range(1, len(areas)):
            if i not in visited and areas[i] > 0:
                queue.append((i, count + 1))
    return -1

def get_average_min_animal_count(areas, roads):
    # Calculate the minimum animal count for all pairs of areas
    min_counts = []
    for i in range(len(areas)):
        for j in range(i + 1, len(areas)):
            min_counts.append(get_min_animal_count(i, j, areas))
    
    # Calculate the average minimum animal count
    return sum(min_counts) / (len(areas) * (len(areas) - 1))

def main():
    n, m = map(int, input().split())
    areas = list(map(int, input().split()))
    roads = []
    for _ in range(m):
        x, y = map(int, input().split())
        roads.append((x, y))
    print(get_average_min_animal_count(areas, roads))

if __name__ == '__main__':
    main()

