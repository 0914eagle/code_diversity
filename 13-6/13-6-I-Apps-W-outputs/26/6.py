
def get_neighbors(student_id, neighbors):
    for neighbor in neighbors:
        if neighbor[0] == student_id:
            return neighbor[1]
    return 0

def restore_queue(n, neighbors):
    queue = []
    for i in range(n):
        front_id = get_neighbors(i, neighbors)
        queue.append(front_id)
    return queue

def main():
    n = int(input())
    neighbors = []
    for i in range(n):
        line = input().split()
        neighbors.append((int(line[0]), int(line[1])))
    queue = restore_queue(n, neighbors)
    print(*queue)

if __name__ == '__main__':
    main()

