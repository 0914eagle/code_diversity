
def get_time(pressed_times):
    time = 0
    for t in pressed_times:
        if time == t:
            time += 1
        else:
            time = t + 1
    return time

def main():
    n = int(input())
    pressed_times = []
    for i in range(n):
        pressed_times.append(int(input()))
    print(get_time(pressed_times))

if __name__ == '__main__':
    main()

