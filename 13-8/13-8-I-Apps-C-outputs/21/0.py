
def get_node_network(n):
    network = {}
    for i in range(2, n+1):
        network[i] = []
    for i in range(2, n+1):
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                network[i].append(int(i/j))
    return network

def get_distance(network, fragments):
    distance = 0
    for fragment in fragments:
        distance += len(network[fragment])
    return distance

def get_min_distance(network, fragments):
    min_distance = float('inf')
    for node in network:
        distance = get_distance(network, fragments + [node])
        if distance < min_distance:
            min_distance = distance
    return min_distance

def solve(n, fragments):
    network = get_node_network(n)
    return get_min_distance(network, fragments)

if __name__ == '__main__':
    n = int(input())
    fragments = list(map(int, input().split()))
    print(solve(n, fragments))

