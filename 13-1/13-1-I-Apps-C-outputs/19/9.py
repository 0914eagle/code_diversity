
def get_maximum_total_priority(streams):
    # Sort the streams by their start time
    streams = sorted(streams, key=lambda x: x[0])
    
    # Initialize the stack with the identifier of the first processor
    stack = [1]
    
    # Initialize the total priority of the chosen streams to 0
    total_priority = 0
    
    # Iterate through the streams
    for stream in streams:
        # If the stream starts at the current time, push its processor identifier to the stack
        if stream[0] == len(stack):
            stack.append(stream[2])
        
        # If the stream ends at the current time, pop its processor identifier from the stack
        if stream[0] + stream[1] == len(stack):
            stack.pop()
        
        # If the stack is not empty and the top processor identifier is the same as the stream's processor identifier, add the stream's priority to the total priority
        if stack and stack[-1] == stream[2]:
            total_priority += stream[2]
    
    return total_priority

