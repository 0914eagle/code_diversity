
def get_maximum_total_priority(streams):
    streams.sort(key=lambda x: x[0])
    stack = []
    total_priority = 0
    for stream in streams:
        if stream[0] >= stack[-1][0] if stack else 0:
            stack.append(stream)
            total_priority += stream[2]
        else:
            while stack and stack[-1][0] < stream[0]:
                total_priority -= stack.pop()[2]
            stack.append(stream)
            total_priority += stream[2]
    return total_priority

