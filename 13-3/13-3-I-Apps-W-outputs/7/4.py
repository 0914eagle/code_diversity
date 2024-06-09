
def solve(n, k, videos):
    # Initialize a queue to store the videos that are waiting to be recompressed
    waiting_queue = []
    
    # Initialize a list to store the times when each video stops being recompressed
    end_times = [0] * n
    
    # Initialize the current time as the time when all servers start working
    current_time = 0
    
    # Iterate through the videos
    for i, (s, m) in enumerate(videos):
        # If there are available servers, start recompressing the video immediately
        if len(waiting_queue) < k:
            waiting_queue.append(i)
            current_time += m * 60
            end_times[i] = current_time
        # Otherwise, add the video to the waiting queue
        else:
            waiting_queue.append(i)
    
    # While there are still videos in the waiting queue
    while waiting_queue:
        # Dequeue a video and start recompressing it
        video_index = waiting_queue.pop(0)
        s, m = videos[video_index]
        current_time += m * 60
        end_times[video_index] = current_time
    
    return end_times

