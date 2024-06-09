
def solve(n, k, videos):
    # Initialize a queue to store the videos that are waiting to be recompressed
    waiting_queue = []
    
    # Initialize a list to store the times when the videos stop being recompressed
    stop_times = [0] * n
    
    # Initialize the current time as the time when all the servers start working
    current_time = 0
    
    # Iterate through the videos
    for i, (s, m) in enumerate(videos):
        # If there are available servers, start recompressing the video immediately
        if len(waiting_queue) < k:
            waiting_queue.append((s, m, i))
            current_time = max(current_time, s)
        # Otherwise, add the video to the waiting queue
        else:
            waiting_queue.append((s, m, i))
    
    # While there are still videos waiting to be recompressed
    while waiting_queue:
        # Sort the waiting queue by the time the videos appear
        waiting_queue.sort(key=lambda x: x[0])
        
        # Pop the first video from the queue
        s, m, i = waiting_queue.pop(0)
        
        # Calculate the time it takes to recompress the video
        time_to_recompress = m * 60
        
        # Update the current time
        current_time += time_to_recompress
        
        # Add the time the video stops being recompressed to the list of stop times
        stop_times[i] = current_time
    
    return stop_times

