
def get_queue(n, records):
    queue = []
    for record in records:
        queue.append(record[0])
    return queue

def restore_queue(queue):
    n = len(queue)
    for i in range(n):
        if queue[i] == 0:
            queue[i] = queue[(i-1)%n]
    return queue

def main():
    n = int(input())
    records = []
    for i in range(n):
        records.append(list(map(int, input().split())))
    queue = get_queue(n, records)
    restored_queue = restore_queue(queue)
    print(*restored_queue)

if __name__ == '__main__':
    main()

