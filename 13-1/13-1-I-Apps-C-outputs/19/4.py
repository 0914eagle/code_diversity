
def solve(n, streams):
    # Sort the streams by their start time
    streams.sort(key=lambda x: x[0])

    # Initialize the stack and the maximum total priority
    stack = []
    max_priority = 0

    # Iterate through the streams
    for stream in streams:
        # If the stream is not active, skip it
        if stream[0] + stream[1] <= 0:
            continue

        # If the stack is empty, push the processor identifier onto the stack
        if not stack:
            stack.append(stream[2])

        # If the stack is not empty, check if the processor identifier is already on the stack
        else:
            # If the processor identifier is already on the stack, skip the stream
            if stream[2] in stack:
                continue

            # If the processor identifier is not on the stack, push it onto the stack
            stack.append(stream[2])

        # Update the maximum total priority
        max_priority += stream[2]

    return max_priority

