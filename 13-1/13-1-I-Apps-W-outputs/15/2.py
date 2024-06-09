
def get_finish_time(queries, b):
    # Initialize variables
    queue = []
    current_time = 0
    finish_time = []
    
    # Iterate over the queries
    for query in queries:
        # If the server is free and the queue is empty, process the query immediately
        if not queue and not current_time:
            current_time = query[0]
            finish_time.append(current_time + query[1])
            current_time += query[1]
        
        # If the server is busy and the queue has less than b queries, add the query to the end of the queue
        elif queue and len(queue) < b:
            queue.append(query)
        
        # If the server is busy and the queue has b queries or more, reject the query
        else:
            finish_time.append(-1)
    
    # While there are queries in the queue, process them
    while queue:
        current_query = queue.pop(0)
        current_time += current_query[1]
        finish_time.append(current_time)
    
    return finish_time

