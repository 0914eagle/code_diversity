
def get_time_displayed(times_pressed):
    time_displayed = 0
    for time in times_pressed:
        time_displayed += 1
    return time_displayed

def get_time_still_running(times_pressed):
    time_displayed = 0
    for time in times_pressed:
        time_displayed += 1
    return "still running" if time_displayed == 0 else time_displayed

if __name__ == '__main__':
    num_times = int(input())
    times_pressed = []
    for _ in range(num_times):
        times_pressed.append(int(input()))
    print(get_time_displayed(times_pressed))
    print(get_time_still_running(times_pressed))

