
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
for i in range(len(broken_pixels)):
    for j in range(i+1, len(broken_pixels)):
        x1, y1, t1 = broken_pixels[i]
        x2, y2, t2 = broken_pixels[j]
        if x1 == x2 and y1 == y2 and t1 <= t2:
            min_time = min(min_time, t2)
            break
        elif x1 == x2 and y1 == y2 and t1 > t2:
            break
        elif x1 == x2 and y1 != y2 and abs(y1 - y2) == k - 1:
            min_time = min(min_time, t2)
            break
        elif x1 != x2 and y1 == y2 and abs(x1 - x2) == k - 1:
            min_time = min(min_time, t2)
            break
        elif x1 != x2 and y1 != y2 and abs(x1 - x2) == k - 1 and abs(y1 - y2) == k - 1:
            min_time = min(min_time, t2)
            break

if min_time == 10**9 + 1:
    print(-1)
else:
    print(min_time)

