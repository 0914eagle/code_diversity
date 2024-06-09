
n, m, k, q = map(int, input().split())

broken_pixels = []
for i in range(q):
    x, y, t = map(int, input().split())
    broken_pixels.append((x, y, t))

# Sort the broken pixels by their time of failure
broken_pixels.sort(key=lambda x: x[2])

# Initialize the minimum time the monitor became broken to a large value
min_time = 10**9 + 1

# Iterate through the broken pixels and check if there is a broken rectangle with size k × k
for i in range(len(broken_pixels)):
    for j in range(i, len(broken_pixels)):
        if j - i + 1 == k:
            # Check if the rectangle is valid
            x1, y1, t1 = broken_pixels[i]
            x2, y2, t2 = broken_pixels[j]
            if x1 <= x2 and y1 <= y2:
                # Check if the rectangle is a square
                if x1 == x2 or y1 == y2:
                    # Check if the rectangle is a square with all pixels broken
                    if all(broken_pixels[i][2] <= t for i in range(i, j+1)):
                        # Update the minimum time the monitor became broken
                        min_time = min(min_time, t1)
                        break

if min_time == 10**9 + 1:
    print(-1)
else:
    print(min_time)

