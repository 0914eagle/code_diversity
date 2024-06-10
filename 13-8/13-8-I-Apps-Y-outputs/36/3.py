
def get_stopwatch_time(times):
    current_time = 0
    for time in times:
        current_time += 1
        if current_time == time:
            current_time += 1
    return current_time

def main():
    num_times = int(input())
    times = []
    for i in range(num_times):
        times.append(int(input()))
    print(get_stopwatch_time(times))

if __name__ == '__main__':
    main()

