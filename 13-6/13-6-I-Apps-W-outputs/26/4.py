
def get_queue(n, records):
    queue = []
    for i in range(n):
        queue.append(i+1)
    for record in records:
        if record[0] != 0:
            queue[record[0]-1] = record[1]
        if record[1] != 0:
            queue[record[1]-1] = record[0]
    return queue

def main():
    n = int(input())
    records = []
    for i in range(n):
        records.append(list(map(int, input().split())))
    queue = get_queue(n, records)
    print(*queue)

if __name__ == '__main__':
    main()

