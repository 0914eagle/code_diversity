
def get_finish_time(queries, b):
    # Initialize variables
    queue = []
    current_time = 0
    finish_time = []
    
    # Iterate through the queries
    for query in queries:
        # If the server is free and the queue is empty, process the query immediately
        if not queue and not current_time:
            current_time = query[0]
            finish_time.append(current_time + query[1])
            continue
        
        # If the server is busy and the queue has less than b queries, add the query to the end of the queue
        if queue and len(queue) < b:
            queue.append(query)
            continue
        
        # If the server is busy and the queue has b queries or more, reject the query
        if queue and len(queue) >= b:
            finish_time.append(-1)
            continue
    
    # If the server is free and the queue has queries, process the query from the queue
    if not current_time and queue:
        current_time = queue[0][0]
        finish_time.append(current_time + queue[0][1])
        queue.pop(0)
    
    return finish_time

def main():
    n, b = map(int, input().split())
    queries = []
    for _ in range(n):
        queries.append(list(map(int, input().split())))
    finish_time = get_finish_time(queries, b)
    print(*finish_time, sep='\n')

if __name__ == '__main__':
    main()

