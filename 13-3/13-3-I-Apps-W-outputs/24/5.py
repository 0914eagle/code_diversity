
def restore_queue(queue):
    n = len(queue)
    result = [0] * n
    for i in range(n):
        front, back = queue[i]
        if front != 0:
            result[front - 1] = i + 1
        if back != 0:
            result[i] = back
    return result

