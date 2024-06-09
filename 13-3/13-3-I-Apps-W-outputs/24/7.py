
def restore_queue(queue):
    n = len(queue)
    result = [0] * n
    for i in range(n):
        a, b = queue[i]
        if a != 0:
            result[i] = a
        if b != 0:
            result[n-i-1] = b
    return result

