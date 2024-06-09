
def solve(n, t, *photos):
    photos = [(a, b) for a, b in photos]
    photos.sort(key=lambda x: x[1])
    time = 0
    for i in range(n):
        if time + t > photos[i][1]:
            return "no"
        time += t
    return "yes"

