
def calculate_delivery_time(serving_times):
    serving_times.sort()
    time = 0
    for serving_time in serving_times:
        time = (time // 10 + 1) * 10
        time = max(time, serving_time)
        time += serving_time
    return time

if __name__ == "__main__":
    serving_times = [int(input()) for _ in range(5)]
    print(calculate_delivery_time(serving_times))
