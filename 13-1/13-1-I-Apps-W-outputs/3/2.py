
n, m, k, q = map(int, input().split())

broken_pixels = []
for i in range(q):
    x, y, t = map(int, input().split())
    broken_pixels.append((x, y, t))

# Sort the broken pixels by their time of failure
broken_pixels.sort(key=lambda x: x[2])

# Initialize the minimum time the monitor became broken to a large value
min_time = 10**9 + 1

# Iterate through the broken pixels and check if they form a broken rectangle
for i in range(len(broken_pixels) - k + 1):
    # Check if the pixels form a rectangle
    if all(broken_pixels[i][0] == broken_pixels[i + j][0] for j in range(1, k)):
        # Check if the pixels form a rectangle of size k x k
        if all(broken_pixels[i][1] == broken_pixels[i + j][1] for j in range(1, k)):
            # Check if the rectangle is the first one to break the monitor
            if broken_pixels[i][2] < min_time:
                min_time = broken_pixels[i][2]
                break

if min_time == 10**9 + 1:
    print(-1)
else:
    print(min_time)

