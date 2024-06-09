
def get_maximum_total_priority(streams):
    
    # Sort the streams by their start time
    streams.sort(key=lambda x: x[0])
    
    # Initialize the stack with the identifier of the first processor
    stack = [1]
    
    # Initialize the total priority of the chosen streams to 0
    total_priority = 0
    
    # Iterate through the streams
    for stream in streams:
        # If the stream starts at the current time, push its processor identifier to the stack
        if stream[0] == stack[-1]:
            stack.append(stream[2])
        # If the stream starts after the current time, pop the processor identifier from the stack until the stack is not empty or the stream can be admitted
        else:
            while stack and stream[0] > stack[-1]:
                stack.pop()
            # If the stack is not empty, push the stream's processor identifier to the stack
            if stack:
                stack.append(stream[2])
    
        # Add the stream's priority to the total priority
        total_priority += stream[2]
    
    # Return the maximum total priority
    return total_priority

