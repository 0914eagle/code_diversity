
def get_tea_time(n, l, r):
    tea_time = [0] * n
    queue = []
    for i in range(n):
        queue.append((l[i], r[i], i))
    queue.sort()
    for i in range(n):
        if queue[0][0] == queue[i][0]:
            tea_time[queue[i][2]] = queue[i][1]
            queue.pop(0)
        else:
            tea_time[queue[i][2]] = 0
            queue.pop(0)
    return tea_time

