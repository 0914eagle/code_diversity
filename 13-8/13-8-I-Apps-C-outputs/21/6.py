
def get_prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors

def get_emotion_samples_node(n_fragments, fragments_locations):
    # Initialize the graph with all nodes and edges
    graph = {}
    for i in range(1, n_fragments + 1):
        graph[i] = []
    for i in range(1, n_fragments + 1):
        for j in range(1, n_fragments + 1):
            if i != j:
                graph[i].append(j)

    # Find the shortest path from each fragment to the emotion samples node
    emotion_samples_node = 1
    for i in range(1, n_fragments + 1):
        distance = float('inf')
        for j in range(1, n_fragments + 1):
            if i != j:
                current_distance = get_path_length(graph, i, j, emotion_samples_node)
                if current_distance < distance:
                    distance = current_distance
        emotion_samples_node += distance

    return emotion_samples_node

def get_path_length(graph, start, end, emotion_samples_node):
    visited = set()
    queue = [(start, 0)]
    while queue:
        current_node, current_distance = queue.pop(0)
        if current_node == end:
            return current_distance
        if current_node not in visited:
            visited.add(current_node)
            for neighbor in graph[current_node]:
                if neighbor != emotion_samples_node:
                    queue.append((neighbor, current_distance + 1))
    return float('inf')

def main():
    n_fragments = int(input())
    fragments_locations = [int(i) for i in input().split()]
    emotion_samples_node = get_emotion_samples_node(n_fragments, fragments_locations)
    print(emotion_samples_node)

if __name__ == '__main__':
    main()

