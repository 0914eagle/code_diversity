
n, k = map(int, input().split())
videos = []
for i in range(n):
    s, m = map(int, input().split())
    videos.append((s, m))

servers = [0] * k
current_time = 0
result = []

for video in videos:
    s, m = video
    while servers.count(0) == 0:
        current_time += 1
        for i in range(k):
            if servers[i] > 0:
                servers[i] -= 1
    servers[servers.index(0)] = m * 60
    result.append(current_time + m * 60)

print(*result, sep='\n')

