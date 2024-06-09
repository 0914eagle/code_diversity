
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

        # If the stack is empty or the top of the stack is not the processor that should process the stream, push the processor identifier onto the stack
        if not stack or stack[-1] != (stream[0] % n):
            stack.append(stream[0] % n)

        # Pop the processor identifier from the stack after the stream has been processed
        stack.pop()

        # Update the maximum total priority
        max_priority += stream[2]

    return max_priority

