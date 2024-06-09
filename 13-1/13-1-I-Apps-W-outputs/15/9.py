
def get_finish_time(queries, b):
    # Initialize variables
    queue = []
    current_time = 0
    finish_times = []
    
    # Iterate through the queries
    for query in queries:
        # If the server is free and the queue is empty, process the query immediately
        if not queue and not current_time:
            current_time = query[0]
            finish_times.append(current_time + query[1])
        # If the server is busy and the queue has less than b queries, add the query to the end of the queue
        elif len(queue) < b:
            queue.append(query)
        # If the server is busy and the queue has b queries or more, reject the query
        else:
            finish_times.append(-1)
    
    # While there are queries in the queue, process them
    while queue:
        current_time += 1
        for i in range(len(queue)):
            if queue[i][0] == current_time:
                finish_times.append(current_time + queue[i][1])
                queue.pop(i)
                break
    
    return finish_times

def main():
    n, b = map(int, input().split())
    queries = []
    for _ in range(n):
        queries.append(list(map(int, input().split())))
    finish_times = get_finish_time(queries, b)
    print(*finish_times, sep='\n')

if __name__ == '__main__':
    main()

