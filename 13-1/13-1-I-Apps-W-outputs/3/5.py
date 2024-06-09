
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
    x1, y1, t1 = broken_pixels[i]
    x2, y2, t2 = broken_pixels[i + k - 1]
    if x1 == x2 and y1 == y2:
        # Check if the rectangle is a square
        if x1 - 1 >= 0 and y1 - 1 >= 0 and x1 + k <= n and y1 + k <= m:
            # Check if all pixels in the rectangle are broken
            broken_count = 0
            for j in range(i, i + k):
                if broken_pixels[j][2] <= t1:
                    broken_count += 1
            if broken_count == k * k:
                # If all pixels in the rectangle are broken, update the minimum time
                min_time = min(min_time, t1)

# Print the minimum time the monitor became broken, or -1 if it's still not broken
print(-1 if min_time == 10**9 + 1 else min_time)

