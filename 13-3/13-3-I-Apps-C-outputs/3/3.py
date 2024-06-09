
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

        # If the stream ends at the current time, pop its processor identifier from the stack
        if stream[0] + stream[1] == len(stack):
            stack.pop()

        # If the stack is not empty and the top processor identifier is the same as the current stream's processor identifier, add the stream's priority to the maximum total priority
        if stack and stack[-1] == stream[2]:
            max_priority += stream[2]

    return max_priority

