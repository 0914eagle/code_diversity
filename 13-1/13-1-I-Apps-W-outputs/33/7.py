
def get_min_capacity(log):
    # Initialize a dictionary to store the number of visitors in the room at each time
    visitors = {}

    # Iterate through the log and update the number of visitors in the room
    for event in log:
        if event.startswith("+"):
            visitors[event[1:]] = visitors.get(event[1:], 0) + 1
        else:
            visitors[event[1:]] -= 1

    # Find the minimum capacity of the reading room by finding the minimum number of visitors at any given time
    return min(visitors.values())

