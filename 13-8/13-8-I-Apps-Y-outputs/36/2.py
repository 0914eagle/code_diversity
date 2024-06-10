
def get_stopwatch_time(times):
    current_time = 0
    for time in times:
        current_time += 1
    return current_time

def main():
    n = int(input())
    times = []
    for i in range(n):
        times.append(int(input()))
    print(get_stopwatch_time(times))

if __name__ == '__main__':
    main()

