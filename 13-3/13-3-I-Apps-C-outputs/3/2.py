
def get_maximum_total_priority(streams):
    streams.sort(key=lambda x: x[0])
    priority_sum = 0
    max_priority_sum = 0
    for stream in streams:
        priority_sum += stream[2]
        max_priority_sum = max(max_priority_sum, priority_sum)
        priority_sum = max(priority_sum, 0)
    return max_priority_sum

