
def solve(n, streams):
    # Sort the streams by their start time
    streams.sort(key=lambda x: x[0])

    # Initialize the stack and the maximum total priority
    stack = []
    max_priority = 0

    # Iterate through the streams
    for stream in streams:
        # If the stream starts at the current time, push its processor identifier to the stack
        if stream[0] == len(stack):
            stack.append(stream[2])
        # If the stream is already in the stack, skip it
        elif stream[2] in stack:
            continue
        # If the stream is not in the stack, pop processors from the stack until the stream can be processed
        else:
            while stack and stack[-1] < stream[2]:
                stack.pop()
            # If the stack is empty, the stream cannot be processed
            if not stack:
                continue
            # Add the stream's priority to the maximum total priority
            max_priority += stream[2]

    return max_priority

