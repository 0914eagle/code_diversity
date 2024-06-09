
def get_finish_time(queries, b):
    
    queue = []
    finish_time = []
    for i, query in enumerate(queries):
        t, d = query
        if not queue and len(queue) < b:
            # Server is free and queue is empty, start processing the query
            queue.append(query)
            finish_time.append(t + d)
        elif len(queue) < b:
            # Server is busy but queue is not full, add the query to the end of the queue
            queue.append(query)
        else:
            # Server is busy and queue is full, reject the query
            finish_time.append(-1)
    return finish_time

def main():
    n, b = map(int, input().split())
    queries = []
    for i in range(n):
        queries.append(tuple(map(int, input().split())))
    finish_time = get_finish_time(queries, b)
    print(*finish_time, sep='\n')

if __name__ == '__main__':
    main()

