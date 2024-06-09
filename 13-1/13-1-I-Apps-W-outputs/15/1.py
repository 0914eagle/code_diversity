
def get_finish_time(queries, b):
    
    queue = []
    finish_time = []
    for i, query in enumerate(queries):
        t, d = query
        if not queue and len(queue) < b:
            # Server is free and queue is empty, process query immediately
            finish_time.append(t + d)
        elif len(queue) < b:
            # Server is busy but queue is not full, add query to the end of the queue
            queue.append(query)
        else:
            # Server is busy and queue is full, reject query
            finish_time.append(-1)
    
    # Process queries in the queue
    while queue:
        query = queue.pop(0)
        t, d = query
        finish_time.append(t + d)
    
    return finish_time

def main():
    n, b = map(int, input().split())
    queries = []
    for i in range(n):
        t, d = map(int, input().split())
        queries.append((t, d))
    finish_time = get_finish_time(queries, b)
    print(*finish_time, sep='\n')

if __name__ == '__main__':
    main()

