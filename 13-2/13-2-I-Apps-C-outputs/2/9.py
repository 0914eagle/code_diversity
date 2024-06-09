
def is_possible(n, q, s, queues, sensors, windows):
    total_data = 0
    for window in windows:
        data_per_sensor = window[1:]
        total_data += sum(data_per_sensor)
        for i in range(s):
            queue = queues[sensors[i] - 1]
            if queue - data_per_sensor[i] < 0:
                return "impossible"
            queue -= data_per_sensor[i]
    if total_data > n:
        return "impossible"
    return "possible"

if __name__ == '__main__':
    n, q, s = map(int, input().split())
    queues = list(map(int, input().split()))
    sensors = list(map(int, input().split()))
    windows = [list(map(int, input().split())) for _ in range(n)]
    print(is_possible(n, q, s, queues, sensors, windows))

