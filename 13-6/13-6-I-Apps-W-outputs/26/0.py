
def get_neighbors(n, a, b):
    neighbors = []
    for i in range(n):
        neighbors.append([a[i], b[i]])
    return neighbors

def restore_queue(neighbors):
    queue = []
    for neighbor in neighbors:
        if neighbor[0] != 0:
            queue.append(neighbor[0])
    for i in range(len(neighbors)):
        if neighbors[i][1] != 0 and neighbors[i][1] not in queue:
            queue.append(neighbors[i][1])
    return queue

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    neighbors = get_neighbors(n, a, b)
    queue = restore_queue(neighbors)
    print(*queue)

if __name__ == '__main__':
    main()

