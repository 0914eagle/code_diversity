
def get_neighbors(n, records):
    neighbors = [[] for _ in range(n+1)]
    for record in records:
        neighbors[record[0]].append(record[1])
        neighbors[record[1]].append(record[0])
    return neighbors

def restore_queue(n, neighbors):
    queue = [0] * (n+1)
    queue[0] = 1
    for i in range(1, n+1):
        if neighbors[i]:
            queue[i] = neighbors[i][0]
        else:
            queue[i] = 0
    return queue

def main():
    n = int(input())
    records = []
    for _ in range(n):
        records.append(list(map(int, input().split())))
    neighbors = get_neighbors(n, records)
    queue = restore_queue(n, neighbors)
    print(*queue[1:])

if __name__ == '__main__':
    main()

