
def get_neighbors(student_id, neighbors):
    for neighbor in neighbors:
        if neighbor[0] == student_id:
            return neighbor[1]
    return 0

def restore_queue(n, neighbors):
    queue = []
    for i in range(n):
        student_id = i + 1
        neighbor_id = get_neighbors(student_id, neighbors)
        queue.append(neighbor_id)
    return queue

def main():
    n = int(input())
    neighbors = []
    for i in range(n):
        neighbors.append(list(map(int, input().split())))
    queue = restore_queue(n, neighbors)
    print(*queue, sep=' ')

if __name__ == '__main__':
    main()

