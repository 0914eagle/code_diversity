
def calculate_delivery_time(serving_times):
    serving_times.sort()
    delivery_times = [0] * 5
    current_time = 0

    for i in range(5):
        delivery_times[i] = current_time + serving_times[i]
        current_time = (delivery_times[i] + 9) // 10 * 10

    return delivery_times[-1]

if __name__ == "__main__":
    serving_times = [int(input()) for _ in range(5)]
    print(calculate_delivery_time(serving_times))
