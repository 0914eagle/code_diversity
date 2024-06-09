
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

        # If the stack is empty, push the stream's processor identifier onto the stack
        if not stack:
            stack.append(stream[2])

        # If the stack is not empty, check if the stream's processor identifier is the same as the top of the stack
        else:
            # If the stream's processor identifier is the same as the top of the stack, push it onto the stack
            if stream[2] == stack[-1]:
                stack.append(stream[2])

            # If the stream's processor identifier is not the same as the top of the stack, reject the stream
            else:
                continue

        # Update the maximum total priority
        max_priority += stream[2]

    # Return the maximum total priority
    return max_priority

