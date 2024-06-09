
def solve(n, t, *photos):
    photos = sorted(photos)
    current_time = 0
    for i in range(n):
        earliest, latest = photos[i]
        if current_time + t > latest:
            return "no"
        current_time += t
        if current_time < earliest:
            current_time = earliest + t
    return "yes"

