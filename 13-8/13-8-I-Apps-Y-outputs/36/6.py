
def get_pressed_times(n):
    pressed_times = []
    for i in range(n):
        pressed_times.append(int(input()))
    return pressed_times

def get_stopwatch_time(pressed_times):
    current_time = 0
    for time in pressed_times:
        if current_time == time:
            current_time += 1
        else:
            current_time = time + 1
    return current_time

def main():
    n = int(input())
    pressed_times = get_pressed_times(n)
    stopwatch_time = get_stopwatch_time(pressed_times)
    print(stopwatch_time)

if __name__ == '__main__':
    main()

