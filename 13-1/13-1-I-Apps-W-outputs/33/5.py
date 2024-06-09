
def get_min_capacity(log):
    # Initialize a dictionary to store the number of visitors in the room
    visitors = {}
    
    # Iterate through the log and update the number of visitors in the room
    for event in log:
        if event.startswith("+"):
            visitor_id = int(event[1:])
            visitors[visitor_id] = visitors.get(visitor_id, 0) + 1
        else:
            visitor_id = int(event[1:])
            visitors[visitor_id] = visitors.get(visitor_id, 0) - 1
            if visitors[visitor_id] == 0:
                del visitors[visitor_id]
    
    # Return the minimum capacity of the reading room
    return min(visitors.values()) if visitors else 0

