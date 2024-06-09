
def can_take_photos(n, t, times):
    times.sort(key=lambda x: x[0])
    end_time = 0
    for i in range(n):
        start_time, end_time = times[i]
        if start_time + t > end_time:
            return "no"
        end_time = max(end_time, start_time + t)
    return "yes"

