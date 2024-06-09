
def is_possible(n, q, s, queues, sensors, windows):
    total_data = 0
    for window in windows:
        data_per_sensor = window[1:]
        total_data += sum(data_per_sensor)
        for i in range(s):
            queue = queues[sensors[i]]
            if queue[0] + data_per_sensor[i] > queue[1]:
                return "impossible"
    return "possible" if total_data <= n else "impossible"

